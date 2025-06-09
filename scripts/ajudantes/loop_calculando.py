import threading
import time

def start_calculating_message(msg="Calculando"):
    stop_event = threading.Event()

    def animate():
        dots = 0
        while not stop_event.is_set():
            print(f"\r{msg}{'.' * dots}{' ' * (3 - dots)}", end='', flush=True)
            dots = (dots + 1) % 4
            time.sleep(0.5)

    thread = threading.Thread(target=animate)
    thread.start()
    return stop_event