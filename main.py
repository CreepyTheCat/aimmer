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
    screen_width, screen_height = pyautogui.size()
    center_x, center_y = screen_width // 2, screen_height // 2
    distance_threshold = 100  # Set a distance threshold (in pixels)

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

                # Check if the mouse has moved too far from the last position
                distance = ((current_mouse_position[0] - last_mouse_position[0]) ** 2 + 
                            (current_mouse_position[1] - last_mouse_position[1]) ** 2) ** 0.5
                if distance > distance_threshold:
                    # Move the mouse back to the center of the screen
                    pyautogui.moveTo(center_x, center_y)
                    print("Mouse moved too far, resetting to center.")

            else:
                # If the mouse is idle, do not register clicks
                time.sleep(0.1)  # Sleep to reduce CPU usage

        time.sleep(0.1)  # Sleep to reduce CPU usage

if __name__ == "__main__":
    main()
