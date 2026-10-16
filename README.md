# Raspberry Pi temperature skill example

This small repository contains the skill at
`skills/pi-temp-monitor/pi-temp-monitor/SKILL.md` and its Python entrypoint
`main.py` in the same directory. The default branch is `master`.

The example reads the Pi thermal sensor and can send an OpenClaw WhatsApp alert.
The source contains a fixed alert destination; review that configuration before
any use. Do not execute it as a generic test or use it to resume a retired runtime.

For source validation, compile Python text without importing or running it.
Actual monitoring and alert delivery require explicit authorization and a verified
recipient/tool configuration. Do not publish personal contact details in new examples.
