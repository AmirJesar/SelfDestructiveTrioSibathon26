import customtkinter as ctk     # For modern GUI using Tkinter
import pyautogui                # To simulate keyboard typing (payload injection)
import time                     # For delays (sleep)
import threading                # To run attack in a separate thread (keeps GUI responsive)

# Starts the attack in a separate thread
    # This prevents GUI from freezing while attack runs
    def start_attack_thread(self):
        threading.Thread(target=self.run_attack, daemon=True).start()
