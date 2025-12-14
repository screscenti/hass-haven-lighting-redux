from typing import Dict, Any, Optional
import requests
import logging
from .exceptions import AuthenticationError, ApiError
from .config import DEVICE_ID, API_TIMEOUT

# GIADA FIX: Pointing both to Production API (was stg-api)
AUTH_API_BASE = "https://api.havenlighting.com/api"
PROD_API_BASE = "https://api.havenlighting.com/api"

logger = logging.getLogger(__name__)

class Credentials:
    """Handles authentication and request credentials."""
    
    def __init__(self):
        self._token: Optional[str] = None
        self._refresh_token: Optional[str] = None
        self._user_id: Optional[int] = None
        logger.debug("Initialized Credentials")
        
    @property
    def is_authenticated(self) -> bool:
        return bool(self._token and self._user_id)
        
    def authenticate(self, email: str, password: str) -> bool:
        """Authenticate with the Haven Lighting service."""
        logger.debug("Attempting authentication for user: %s", email)
        
        # FIX: Payload uses userName instead of email
        payload = {
            "userName": email,
            "password": password
        }
        
        try:
            response = self._make_request_internal(
                "POST",
                "/Auth/Authenticate", 
                json=payload,
                auth_required=False
            )
            
            # FIX: Check for token directly in the root response
            if not response or "token" not in response:
                logger.error("Authentication failed: No token returned for user %s", email)
                return False
                
            self._update_credentials(response)
            logger.info("Successfully authenticated user: %s", email)
            return True
            
        except ApiError as e:
            logger.error("Authentication failed for user %s: %s", email, str(e))
            return False
            
    def refresh_token(self) -> bool:
        """Refresh the authentication token."""
        if not self._refresh_token or not self._user_id:
            logger.debug("Cannot refresh token - missing refresh token or user ID")
            return False
        
        try:
            logger.debug("Attempting token refresh for user ID: %s", self._user_id)
            response = self._make_request_internal(
                "POST",
                "/Auth/Refresh",
                json={
                    "refreshToken": self._refresh_token,
                    "userId": self._user_id
                },
                auth_required=False
            )
            self._update_credentials(response)
            logger.debug("Token refresh successful")
            return True
            
        except ApiError as e:
            logger.error("Token refresh failed: %s", str(e))
            return False
            
    def _update_credentials(self, data: Dict[str, Any]) -> None:
        """Update stored credentials from API response."""
        self._token = data.get("token")
        self._refresh_token = data.get("refreshToken")
        self._user_id = data.get("id")
        
    def make_request(
        self, 
        method: str, 
        path: str, 
        auth_required: bool = True,
        use_prod_api: bool = False,
        timeout: int = API_TIMEOUT,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Make an authenticated API request with automatic token refresh."""
        try:
            return self._make_request_internal(
                method=method, 
                path=path, 
                auth_required=auth_required,
                use_prod_api=use_prod_api,
                timeout=timeout,
                **kwargs
            )
        except AuthenticationError:
            logger.info("Authentication error, attempting token refresh")
            if self.refresh_token():
                logger.info("Token refresh successful, retrying request")
                return self._make_request_internal(
                    method=method, 
                    path=path, 
                    auth_required=auth_required,
                    use_prod_api=use_prod_api,
                    timeout=timeout,
                    **kwargs
                )
            logger.error("Token refresh failed, unable to retry request")
            raise AuthenticationError("Token refresh failed")
        
    def _make_request_internal(
        self, 
        method: str, 
        path: str, 
        auth_required: bool = True,
        use_prod_api: bool = False,
        timeout: int = API_TIMEOUT,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Internal method for making API requests."""
        if auth_required and not self.is_authenticated:
            raise AuthenticationError("Authentication required")
            
        base_url = PROD_API_BASE if use_prod_api else AUTH_API_BASE
        url = f"{base_url}{path}"
        
        if self._token:
            headers = kwargs.pop("headers", {})
            headers["Authorization"] = f"Bearer {self._token}"
            kwargs["headers"] = headers
            
        try:
            response = requests.request(method, url, timeout=timeout, **kwargs)
            
            if response.status_code == 401:
                raise AuthenticationError("Received 401 Unauthorized response")
            
            response.raise_for_status()
            
            if response.status_code == 204:
                return {}
                
            data = response.json()
            return data
            
        except requests.exceptions.RequestException as e:
            logger.error("Request failed: %s", str(e))
            raise ApiError(f"Request failed: {str(e)}")
