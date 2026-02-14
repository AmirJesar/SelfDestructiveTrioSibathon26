🛡️ HID-Guard: Behavioral Biometric Defense

HID-Guard is a proactive cybersecurity suite designed to neutralize HID Injection Attacks (like Rubber Ducky and BadUSB) by analyzing typing rhythm and cadence in real-time.

🚀 The Problem: The "Trust Gap"

Standard Operating Systems inherently trust any Human Interface Device (HID) as a legitimate input source.

    The Vulnerability: Malicious USB devices (BadUSB/Rubber Ducky) mimic keyboards to inject commands at 1,000+ WPM.

    The Failure: Traditional Antivirus cannot block these because they appear as "trusted" user keystrokes.

✨ The Solution: Behavioral Biometrics

HID-Guard shifts the focus from what is being typed to how it is being typed.

    Timing Analysis: It monitors Inter-Keystroke Delay (IKD) to detect "inhuman" injection speeds.

    Autonomous Mitigation: Once an attack is detected, the system triggers an immediate lockdown to neutralize the threat.

🛠️ Technical Architecture

    Frontend: Built with CustomTkinter for a professional Security Operations Center (SOC) dashboard.

    Background Monitoring: Uses Python Multithreading to ensure constant surveillance without lag.

    Detection Engine: Implements a Sliding Window Algorithm that averages the last 10-15 keys to eliminate false positives.

    Mitigation Layer: Communicates with Linux kernel hooks (gnome-screensaver / loginctl) for instant OS locking.


⚙️ Installation & Usage
    Dependencies
    sudo pip3 install customtkinter pynput packaging --break-system-packages

    Run the Guardian
    sudo -E python3 guardian.py
    Note: (Root privileges are required to interface with system-level lock commands)

 🔮 Future Scope

    Machine Learning: Transitioning to unique user typing profiles for advanced identity verification.

    Hardware Interruption: Developing Phase 2 to physically unbind malicious USB drivers from the kernel.

    Cross-Platform Support: Expanding protection to Windows and macOS environments.

 👥 The Team

    Developed for SIBATHON '26 by:

    Sandesh kumar (Lead Developer)

    Amir Khan (Project Partner)
