import pyautogui
import webbrowser
from time import sleep


def logout():
    pyautogui.click(144, 365, duration=1)
    sleep(1)
    pyautogui.click(78, 679, duration=1)
    sleep(1)
    pyautogui.click(69, 621, duration=1)


while (True):
    # entrar no instagram
    webbrowser.open('https://www.instagram.com/')
    sleep(5)
    # digitar telefone, usuario, ou email
    pyautogui.click(779, 303, duration=2)
    pyautogui.typewrite('55984089885')
    sleep(2)
    pyautogui.press('tab')
    sleep(2)
    # digitar a senha
    pyautogui.typewrite('D@241708i')
    sleep(2)
    # clicar em log in
    pyautogui.click(877, 399, duration=2)
    sleep(10)
    # clicar em not now
    pyautogui.click(799, 461, duration=2)
    sleep(10)
    # clicar em search
    pyautogui.click(90, 286, duration=2)
    sleep(2)
    # digitar a conta que deseja curtir e entrar
    pyautogui.typewrite('nike')
    sleep(3)
    pyautogui.press('enter')
    sleep(3)
    pyautogui.scroll(-400)
    sleep(2)
    # clicar no ultimo post
    pyautogui.click(450, 467, duration=2)
    sleep(5)
    if not pyautogui.locateCenterOnScreen('coracao.png'):
        # curtir
        pyautogui.click(598, 567, duration=2)
        sleep(2)
        pyautogui.click(671, 678, duration=1)
        # comentar
        pyautogui.typewrite('top!')
        sleep(1)
        # postar
        pyautogui.click(1040, 678, duration=1)
        sleep(1)
    logout()
    sleep(86400)
