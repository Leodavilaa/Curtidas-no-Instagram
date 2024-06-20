import webbrowser
import pyautogui
from time import sleep

# Navegar até o site
webbrowser.open_new('https://www.instagram.com')
sleep(3)

# Entrar com usuário e senha
pyautogui.click(1137,380, duration=2)
pyautogui.typewrite ('lxxxxxx@gmail.com')
sleep(2)
pyautogui.press('tab')
sleep(2)
pyautogui.typewrite('xxxxxx')
sleep(2)

# Clicar em login
pyautogui.move(0,100, duration=2)
pyautogui.click()
sleep(5)

#Carregar codigo de verificação de 2 fatores
pyautogui.click(811,1058, duration=2)
pyautogui.click(902,940, duration=2)
pyautogui.click(720,1056, duration=2)
pyautogui.click(882,411,duration=2)
pyautogui.keyDown('ctrl')
pyautogui.keyDown('v')
pyautogui.keyUp('ctrl')
pyautogui.keyUp('v')
pyautogui.move(0,40, duration=2)
pyautogui.click()
sleep(10)
#clicar em não salvar informações de login
pyautogui.click(1126,630, duration=2)
sleep(10)
# Pesquisar conta 
pyautogui.click(96,304, duration=2)
pyautogui.moveTo(115,232, duration=2)
sleep(2)
pyautogui.click()
sleep(2)
pyautogui.typewrite('Nike')
sleep(2)
pyautogui.click(210,297, duration=2)

#Se já tiver curtido, fazer nada, e pausar por 24hs
pyautogui.click(782,779, duration=2)

# coracao = pyautogui.locateCenterOnScreen('coracao.png', confidence=0.8)
# sleep(2)

# if coracao is not None:
#     sleep(86400)
# elif coracao == None:
pyautogui.click(976,885, duration=2)
sleep(2)
#Se não estiver curtido, comentar na foto
pyautogui.click(1032,988, duration=2)
sleep(1)
pyautogui.typewrite('Topzera')
pyautogui.click(1411,984, duration=2)

#Fazer logout
pyautogui.click(288,834, duration=2)
pyautogui.click(83,995, duration=2)
pyautogui.move(0,-50, duration=2)
pyautogui.click()
#
#
#
