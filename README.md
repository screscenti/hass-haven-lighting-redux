# Haven Lighting Redux

A revived and modernized Home Assistant integration for **Haven Lighting** smart landscape systems.

> ℹ️ **Note:** This project is a fork and "Redux" of the original [haven-hass](https://github.com/mickeyschwab/haven-hass) integration by **@mickeyschwab**. Major thanks to him for the original work! This version has been rewritten to support the **New Haven API (2025)** and restore functionality after the cloud migration.

## 🌟 Features
* **Zone Support:** Controls individual Zones (e.g., "Left House", "Path Lights") instead of just the main controller.
* **Group Support:** Automatically imports your Haven App groups (e.g., "Evens", "Front Yard") as controllable lights.
* **Full Control:** On/Off, Brightness (0-100%), RGB Color, and White Temperature (2700K - 5000K).
* **Aggressive Sync:** Instantly updates all lights when a group is toggled (no more "janky" delays).
* **Self-Cleaning:** Automatically removes deleted groups or zones on reload.

## 🚀 Installation via HACS

1. Open **HACS** in Home Assistant.
2. Click the **three dots** (top right) > **Custom Repositories**.
3. Add the URL of this repository: `https://github.com/screscenti/hass-haven-lighting-redux`
4. Select Category: **Integration**.
5. Click **Download**.
6. Restart Home Assistant.

## ⚙️ Configuration

1. Go to **Settings > Devices & Services**.
2. Click **Add Integration** > Search for **Haven Lighting**.
3. Enter your Haven Lighting **Username** (Email) and **Password**.
4. Your zones and groups will automatically appear!

## 💡 Automations & Color Control

When creating automations in Home Assistant, the standard "Device" trigger often hides advanced color options. To control **RGB Color** and **Brightness** in an automation, you must use the **Call Service** action.

1. In your Automation, scroll to **Actions**.
2. Click **Add Action** and select **Call Service**.
3. Search for and select **`light.turn_on`**.
4. Choose your Haven entity (e.g., `light.front_yard`).
5. Check the boxes for **RGB Color** or **Brightness** to set your desired look.

## ❤️ Credits
* **Original Creator:** [Mickey Schwab (@mickeyschwab)](https://github.com/mickeyschwab)
* **2025 API Rewrite:** [Stephen Crescenti (@screscenti)](https://github.com/screscenti)
