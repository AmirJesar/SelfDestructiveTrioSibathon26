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
