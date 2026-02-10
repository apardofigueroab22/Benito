---
name: pi-temp-monitor
description: Monitors the Raspberry Pi's CPU temperature and sends alerts if a threshold is exceeded.
version: 0.1.0
---

# Pi Temperature Monitor

## Usage
This skill monitors your Raspberry Pi's CPU temperature. If the temperature goes above 70°C, it will send an alert to your configured WhatsApp number.

### Commands

**pi-temp-monitor run**
Checks the current CPU temperature and sends an alert if necessary.
```bash
openclaw pi-temp-monitor run
```

## Configuration
The temperature threshold is currently hardcoded to 70°C within the `main.py` script. The alert recipient is also hardcoded to your WhatsApp number (`+17864789404`).

## Dependencies
This skill uses standard Raspberry Pi OS commands and Python modules. No external `npm` dependencies are required.
