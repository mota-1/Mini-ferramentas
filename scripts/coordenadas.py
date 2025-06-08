import pyautogui
import sys

def atualizar_console(mensagem):
    sys.stdout.write('\r' + mensagem)
    sys.stdout.flush()

while True:
    x, y = pyautogui.position()
    atualizar_console(f"Coordenadas do mouse: ({x}, {y})")