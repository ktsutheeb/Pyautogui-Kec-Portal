import pyautogui
import pyautogui
import time

print("Press Ctrl-C to stop.")

try:
    while True:
        # x, y = pyautogui.position()  # Get the current mouse position
        # # print(f"Mouse position: x={x}, y={y}", end="\r")  # Print position
        # # time.sleep(0)  # Delay for a short time to avoid spamming the console
        # pyautogui.moveTo(100,100,duration=3)
        x,y=pyautogui.position()
        print(x,y)
        # print(pyautogui.size())
        
except KeyboardInterrupt:
    print("\nProgram stopped.")

