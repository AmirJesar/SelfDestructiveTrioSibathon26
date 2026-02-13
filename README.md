# SelfDestructiveTrio
Project Idea: HID-Guard

Proposed Solution / Idea Description:
HID-Guard is a software-based security prototype designed to neutralize Keystroke Injection Attacks (like those from a USB Rubber Ducky). The system operates on the principle of Behavioral Biometrics rather than traditional file scanning.

How it works:

    Real-Time Monitoring: The application runs as a lightweight background service that listens to the timing of every incoming keystroke at a millisecond level.

    Speed Analysis: It calculates the "inter-keystroke delay." While human typing is naturally variable and relatively slow, malicious scripts inject characters with near-zero latency.

    Automated Response: If the average typing speed crosses a predefined "inhuman" threshold (e.g., more than 50 characters per second), the system identifies a threat and immediately triggers a system-level lock or disables the input device to prevent the payload from executing.

Innovation:
Instead of trying to block the hardware (which is difficult due to OS trust), this solution blocks the malicious behavior, providing an immediate defense against physical "plug-and-hack" threats without requiring any additional hardware.


## 🚀 How to Run the Demo

1. **Install Dependencies:**
   bash:
   pip install -r requirements.txt --break-system-packages
2. **Start the Guardian:**
    Open a terminal and run:
    python3 guardian.py
3. **Simulate an Attack:**
    Open a second terminal and run:
    python3 simulator.py
    
