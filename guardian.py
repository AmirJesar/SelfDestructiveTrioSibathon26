import time
import subprocess
import threading
import json
from pynput import keyboard
import pyudev

# CONFIGURATION
SPEED_THRESHOLD = 0.05
WINDOW_SIZE = 10
BURST_THRESHOLD = 8
SUSPICION_LIMIT = 10

SUSPICIOUS_KEYWORDS = [
    "powershell", "curl", "wget",
    "bash", "chmod", "nc", "python -c"
]


class HIDGuardian:
    def __init__(self):
        self.last_key_time = time.time()
        self.intervals = []
        self.keystroke_buffer = ""
        self.burst_count = 0
        self.suspicion_score = 0
        self.new_usb_detected = False

       
        threading.Thread(target=self.monitor_usb, daemon=True).start()

   
    def monitor_usb(self):
        context = pyudev.Context()
        monitor = pyudev.Monitor.from_netlink(context)
        monitor.filter_by(subsystem='input')

        for device in monitor:
            if device.action == 'add':
                if 'ID_INPUT_KEYBOARD' in device:
                    print("[USB] New keyboard device detected!")
                    self.new_usb_detected = True
                    self.suspicion_score += 6


    def lock_system(self):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        log_data = {
            "timestamp": timestamp,
            "suspicion_score": self.suspicion_score,
            "burst_count": self.burst_count,
            "usb_recent": self.new_usb_detected
        }

        with open("attack_logs.json", "a") as f:
            f.write(json.dumps(log_data) + "\n")

        print("\n🚨 SECURITY ALERT TRIGGERED 🚨")
        print(log_data)

        subprocess.run(["xdg-screensaver", "lock"])


if _name_ == "_main_":
    guardian = HIDGuardian()
    guardian.start()


