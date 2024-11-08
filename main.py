import pyautogui
import keyboard
import ctypes
import time

# Constants for hiding and showing the mouse cursor
class CURSOR:
    HIDE = 0
    SHOW = 1

def hide_cursor():
    ctypes.windll.user32.ShowCursor(False)

def show_cursor():
    ctypes.windll.user32.ShowCursor(True)

def main():
    print("Press '0' to start registering right clicks.")
    print("Press '0' again to exit the program.")
    
    right_clicking = False
    last_mouse_position = pyautogui.position()
    
    while True:
        if keyboard.is_pressed('0'):
            if not right_clicking:
                right_clicking = True
                hide_cursor()
                print("Right-clicking started. Press '0' again to stop.")
            else:
                right_clicking = False
                show_cursor()
                print("Right-clicking stopped.")
                break  # Exit the program

        if right_clicking:
            current_mouse_position = pyautogui.position()
            if current_mouse_position != last_mouse_position:
                # If the mouse is moving, register a right click
                pyautogui.click(button='right')
                last_mouse_position = current_mouse_position
            else:
                # If the mouse is idle, do not register clicks
                time.sleep(0.1)  # Sleep to reduce CPU usage

        time.sleep(0.1)  # Sleep to reduce CPU usage

if __name__ == "__main__":
    main()
