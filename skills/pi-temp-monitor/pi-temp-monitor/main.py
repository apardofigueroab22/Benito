
import os
import subprocess
import json

# Define the temperature threshold
TEMPERATURE_THRESHOLD_C = 70.0
# Define the recipient for alerts (your WhatsApp number)
# This should be fetched from MEMORY.md in a real-world scenario or passed as an argument.
# For simplicity, I'm hardcoding it for now, based on previous context.
ALERT_RECIPIENT = "+17864789404"

def get_cpu_temperature():
    try:
        # Read the raw temperature from /sys/class/thermal/thermal_zone0/temp
        # This path is standard for Raspberry Pi CPU temperature
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            raw_temp = int(f.read().strip())
        # Convert to Celsius
        temperature_c = raw_temp / 1000.0
        return temperature_c
    except FileNotFoundError:
        return "Error: Temperature sensor file not found. Is this a Raspberry Pi?"
    except Exception as e:
        return f"Error reading temperature: {e}"

def send_alert(message):
    try:
        # Use the OpenClaw message tool to send a WhatsApp message
        # This requires the 'message' tool to be available to the agent.
        command = [
            "openclaw", "message",
            "action=send",
            f"to={ALERT_RECIPIENT}",
            f"message={message}"
        ]
        # Execute the command
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(f"Alert sent successfully: {result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error sending alert: {e.stderr}")
    except Exception as e:
        print(f"General error in send_alert: {e}")

if __name__ == "__main__":
    current_temp = get_cpu_temperature()

    if isinstance(current_temp, float):
        print(f"Current Raspberry Pi CPU Temperature: {current_temp:.2f}°C")
        if current_temp > TEMPERATURE_THRESHOLD_C:
            alert_message = f"🚨 Raspberry Pi Alert: CPU temperature is {current_temp:.2f}°C, which exceeds the threshold of {TEMPERATURE_THRESHOLD_C}°C!"
            send_alert(alert_message)
            print(alert_message)
        else:
            print("Temperature is within acceptable limits.")
    else:
        # Handle the error message returned from get_cpu_temperature
        print(current_temp)
        # Optionally, send an alert about the error itself if critical
        # send_alert(f"⚠️ Raspberry Pi Monitor Error: {current_temp}")

# The OpenClaw skill execution environment might require a specific output format
# to indicate success/failure or to return data.
# For this simple monitoring script, printing to stdout is sufficient.
