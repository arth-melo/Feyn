import keyboard as ky
import pyperclip as pc
import time
import threading
import keyboard as ky
import pyperclip as pc
import time
import threading

busy = threading.Lock()

def copiar():
    if not busy.acquire(blocking=False):
        return  # já está processando, ignora disparo duplicado
    try:
        old_text = pc.paste()
        ky.press_and_release('ctrl+c')

        timeout = time.time() + 1.0
        new_text = pc.paste()
        while new_text == old_text and time.time() < timeout:
            time.sleep(0.02)
            new_text = pc.paste()

        return new_text
    finally:
        busy.release()

if __name__ == "__main__":
    ky.add_hotkey('alt+a', copiar, suppress=True)
    ky.wait()