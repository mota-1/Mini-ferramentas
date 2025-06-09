import pyautogui
import sys

def update_console(message):
    sys.stdout.write('\r' + message)
    sys.stdout.flush()

while True:
    x, y = pyautogui.position()
    update_console(f"Coordenadas do mouse: ({x}, {y})")