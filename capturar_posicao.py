import pyautogui
import time

print("Você tem 5 segundos para posicionar o mouse...")
time.sleep(5)

x, y = pyautogui.position()

print(f"Posição capturada:")
print(f"X: {x}")
print(f"Y: {y}")