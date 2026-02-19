import pyautogui
import time

#abrindo o google (imagine estar na tela inicial)
time.sleep(5)
pyautogui.PAUSE = 2
pyautogui.click(x=1294, y=1052, button="right")
pyautogui.click(x=1258, y=900)


# pesquisar a pagina da hashtag
time.sleep(5)
pyautogui.click(x=201, y=82)
pyautogui.write("Hashtag treinamentos")
pyautogui.press("enter")

# entrando na pagina da hashtag
pyautogui.click(x=371, y=520)

# dentro da pagina procurando o curso
pyautogui.moveTo(x=485, y=209)

pyautogui.click(x=454, y=336)
# se cadastrando
time.sleep(3)
pyautogui.click(x=287, y=702)
pyautogui.write("Teste bot")
pyautogui.click(x=292, y=759)

pyautogui.write("botmail123@gmail.com")
pyautogui.click(x=291, y=823)
pyautogui.write("11 99991-1415")
pyautogui.press("enter")
# login pronto
# pyautogui.moveTo(x=288, y=895, duration=1)
# pyautogui.click(x=542, y=897)



