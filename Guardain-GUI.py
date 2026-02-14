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


def update_dashboard(self, avg_delay):
        """Engine: Real-time Analysis & Mitigation."""
        self.speed_label.configure(text=f"Delay: {avg_delay:.4f}s")
        meter_val = min(avg_delay / 0.2, 1.0) 
        self.progress.set(meter_val)
        
        current_time = time.time()
        # Decision Logic: Threshold check & Cooldown verification
        if avg_delay < SPEED_THRESHOLD and (current_time - self.last_attack_time > COOLDOWN_SECONDS):
            self.last_attack_time = current_time
            self.attack_count += 1
            self.counter_label.configure(text=f"Attacks Prevented: {self.attack_count}")
            self.status_box.configure(text="BREACH DETECTED!", text_color="#e74c3c")
            
            # Mitigation Trigger
            if not self.safe_mode:
                self.lock_system()
                self.console.insert("end", f"[!] LOCK TRIGGERED: Delay {avg_delay:.4f}s\n")
            
            # Data Persistence: Forensic Logging
            with open(LOG_FILE, "a") as f:
                f.write(f"[{time.ctime()}] ATTACK #{self.attack_count} BLOCKED: {avg_delay:.4f}s\n")
