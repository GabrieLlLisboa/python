import win32api
import win32con
import time

def clicar(x, y):
    win32api.SetCursorPos((x, y))
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.03)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def clicar_5x(x, y):
    win32api.SetCursorPos((x, y))
    time.sleep(0.05)
    for _ in range(5):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.03)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(0.05)

print("Começando em 5 segundos...")
time.sleep(5)

while True:
    print("Primeiro")
    clicar(871, 181)

    print("Esperando 2s")
    time.sleep(2)

    print("5 cliques no primeiro")
    clicar_5x(871, 181)

    print("Esperando 3s")
    time.sleep(3)

    print("Segundo")
    clicar(958, 908)

    print("Esperando 120s")
    time.sleep(120)

    print("Quarto")
    clicar(993, 716)

    print("Esperando 25s")
    time.sleep(25)