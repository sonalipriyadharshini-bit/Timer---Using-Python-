import time
import os

# For Windows sound alert
try:
    import winsound
    sound_available = True
except ImportError:
    sound_available = False

print("⏳ Countdown Timer with Sound Alert ⏳")

# Get input from user
seconds = int(input("Enter time in seconds: "))

while seconds > 0:
    mins = seconds // 60
    secs = seconds % 60
    
    timer = f"{mins:02d}:{secs:02d}"
    print(timer)   # <-- Now prints in next line
    
    time.sleep(1)
    seconds -= 1

print("⏰ Time's up!")

# Sound Alert
if sound_available:
    for i in range(3):
        winsound.Beep(1000, 700)
        time.sleep(0.3)
else:
    print("\a\a\a")
