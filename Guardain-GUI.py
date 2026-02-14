import time
import subprocess
import threading
import os
import customtkinter as ctk
from pynput import keyboard

SPEED_THRESHOLD = 0.06  # Logic: Attack detection limit (0.06s)
WINDOW_SIZE = 10         # Logic: Sliding window size (Sample size)
COOLDOWN_SECONDS = 1    # Control: Prevention delay
LOG_FILE = "attack_logs.txt"

def toggle_safe_mode(self):
        """Toggle: Alert-only vs Active Lockdown."""
        self.safe_mode = not self.safe_mode
        text = "SAFE MODE: ON" if self.safe_mode else "SAFE MODE: OFF"
        color = "#27ae60" if self.safe_mode else "#e67e22"
        self.safe_btn.configure(text=text, fg_color=color)
