import time
import pyautogui

time.sleep(3)
captcha_location = pyautogui.locateCenterOnScreen(r'program_automatization\captcha.png')
pyautogui.click(captcha_location)