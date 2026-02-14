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

class HIDGuardPro(ctk.CTk):
    def __init__(self):
        super().__init__()

        # UI Initialization
        self.title("HID-Guard | Fast Response")
        self.geometry("600x650")
        ctk.set_appearance_mode("dark")

        # Core State Variables
        self.attack_count = 0        # Counter: Total incidents
        self.last_attack_time = 0    # Check: Cooldown state
        self.safe_mode = False       # Feature: Lock bypass toggle
        
        # Dashboard Components
        self.label = ctk.CTkLabel(self, text="HID-GUARD DASHBOARD", font=("Roboto", 24, "bold"))
        self.label.pack(pady=20)

        self.counter_label = ctk.CTkLabel(self, text="Attacks Prevented: 0", font=("Roboto", 14), text_color="#3498db")
        self.counter_label.pack()

        # Input Control: Toggle Mitigation
        self.safe_btn = ctk.CTkButton(self, text="SAFE MODE: OFF", fg_color="#e67e22", command=self.toggle_safe_mode)
        self.safe_btn.pack(pady=10)

        # Status: Security Shield
        self.status_box = ctk.CTkLabel(self, text="SHIELD STATUS: SECURED", text_color="#2ecc71", font=("Roboto", 16, "bold"))
        self.status_box.pack(pady=10)

        # Analytics: Real-time delay display
        self.speed_label = ctk.CTkLabel(self, text="Inter-Keystroke Delay: --")
        self.speed_label.pack()
        
        # Visualization: Health bar for keystrokes
        self.progress = ctk.CTkProgressBar(self, width=400)
        self.progress.set(1.0) 
        self.progress.pack(pady=10)

        # Forensic Terminal
        self.console = ctk.CTkTextbox(self, width=500, height=150)
        self.console.pack(pady=15)
        self.console.insert("0.0", "[System] Ultra-Fast Monitoring Active...\n")

        # Navigation Buttons
        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack(pady=10)
        self.log_btn = ctk.CTkButton(self.btn_frame, text="View Logs", command=self.open_logs)
        self.log_btn.grid(row=0, column=0, padx=10)
        self.restore_btn = ctk.CTkButton(self.btn_frame, text="Reset Shield", command=self.restore_system)
        self.restore_btn.grid(row=0, column=1, padx=10)

        # Behavioral Biometrics Data
        self.last_key_time = time.time() # Last event timestamp
        self.intervals = []              # Timing data buffer
        
        # Multithreading: Background listener execution
        self.listener_thread = threading.Thread(target=self.start_listener, daemon=True)
        self.listener_thread.start()

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

    def lock_system(self):
        """Action: Operating System Lockdown."""
            try:
                subprocess.run(["gnome-screensaver-command", "-l"]) # GNOME Lock
            except Exception:
                subprocess.run(["loginctl", "lock-session"])       # Systemd Fallback

    def on_press(self, key):
        """Event: Keystroke timing capture."""
        current_time = time.time()
        delay = current_time - self.last_key_time
        self.last_key_time = current_time
        self.intervals.append(delay)

        # Sliding Window Implementation
        if len(self.intervals) > WINDOW_SIZE:
            self.intervals.pop(0) # FIFO Buffer
            avg_delay = sum(self.intervals) / len(self.intervals)
            
            # Thread Safety: UI update
            self.after(0, self.update_dashboard, avg_delay)
            
            # Reset buffer on breach
            if avg_delay < SPEED_THRESHOLD:
                self.intervals = [] 


if __name__ == "__main__":
    app = HIDGuardPro()
    app.mainloop()
