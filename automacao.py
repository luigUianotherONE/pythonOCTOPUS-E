import pyautogui
import time 

pyautogui.PAUSE = 0.5

# pegar posicoes do mouse e tela
# print(pyautogui.position())
# print(pyautogui.size())

# ---- funcoes do mouse ----
time.sleep(5)
# pyautogui.moveTo(x=486, y=202, duration=1)
# pyautogui.click(x=1271, y=338)
# pyautogui.scroll(-300) # numero negativo scroll para baixo

# pyautogui.click(x=267, y=211) # clica em algum lugar

# pyautogui.click(x=267, y=211, button="right",clicks=2,interval=2)
# Aqui sao só os parametros extras que voce pode passar, 
# qual botao vai ser clicado e quantos clicks serao dados e o intervalo entre eles


# ---- funcoes teclado ----
pyautogui.write("Me observe subir")
pyautogui.hotkey()
pyautogui.press()
