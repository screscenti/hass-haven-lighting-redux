# hass-haven-lighting-redux
A revived Home Assistant integration for Haven Lighting. Updated for the 2025 Cloud API with support for Zones, Groups, Color, and White Temperature.

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

## 🎄 Creating Light Shows (Christmas/Halloween)

The native "Light Show" feature requires the Series 9 Pro controller. However, you can create **better** shows using Home Assistant scripts!

**Example: "Whimsical Christmas" Script**
Create a script that loops while an `input_boolean` is On. Send random colors (Red/Green/White) to your lights with random delays (10-20s) and a 5-second transition. This creates a gentle, organic "twinkling" effect that avoids API rate limits.

## ❤️ Credits
* **Original Creator:** [Mickey Schwab (@mickeyschwab)](https://github.com/mickeyschwab)
* **2025 API Rewrite:** [Stephen Crescenti (@screscenti)](https://github.com/screscenti)
