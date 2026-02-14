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

    # Function that simulates the attack
    def run_attack(self):
        # Update status before starting
        self.status.configure(text="Status: Launching in 3s...")
        time.sleep(3)  # Wait 3 seconds before execution

        # Update status to show injection phase
        self.status.configure(text="Status: INJECTING...")

        # Payload to simulate keystroke injection (like Rubber Ducky)
        payload = "echo 'System Breached!' && cat /etc/passwd\n"

        # Types payload automatically at high speed
        pyautogui.write(payload, interval=0.01) 

        # Reset status after attack completes
        self.status.configure(text="Status: Ready")
        

# Entry point of the program
if __name__ == "__main__":
    app = AttackSimulator()  # Create app instance
    app.mainloop()           # Run GUI event loop
