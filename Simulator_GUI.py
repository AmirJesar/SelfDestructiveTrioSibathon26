import customtkinter as ctk     # For modern GUI using Tkinter
import pyautogui                # To simulate keyboard typing (payload injection)
import time                     # For delays (sleep)
import threading                # To run attack in a separate thread (keeps GUI responsive)

# Main GUI class inheriting from CustomTkinter window
class AttackSimulator(ctk.CTk):
    def __init__(self):
        super().__init__()  # Initialize the parent CTk class
        
        # Window title and size
        self.title("HID-Guard | Attack Simulator")
        self.geometry("400x300")
        
        # Heading label
        self.label = ctk.CTkLabel(self, text="ATTACK SIMULATOR", font=("Roboto", 20, "bold"))
        self.label.pack(pady=20)

        # Button to start the simulated attack
        self.btn = ctk.CTkButton(
            self,
            text="LAUNCH RUBBER DUCKY ATTACK",
            fg_color="#e74c3c",                 # Red color for warning/attack feel
            command=self.start_attack_thread    # Calls function when clicked
        )
        self.btn.pack(pady=20)

        # Status label to show current state
        self.status = ctk.CTkLabel(self, text="Status: Ready")
        self.status.pack(pady=10)

    # Starts the attack in a separate thread
    # This prevents GUI from freezing while attack runs
    def start_attack_thread(self):
        threading.Thread(target=self.run_attack, daemon=True).start()
