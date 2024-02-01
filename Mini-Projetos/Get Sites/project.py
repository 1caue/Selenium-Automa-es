from selenium.webdriver.chrome.service import Service
from selenium import webdriver 
import time, pyautogui

path = 'chromedriver.exe'
chrome_service = Service(path)
chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

pyautogui.hotkey('win', 'up')

sites = ['https://www.terabyteshop.com.br/',  'https://www.kabum.com.br/', 
         'https://www.amazon.com.br/', 'https://www.pichau.com.br/']

for site in sites:
    driver.execute_script("window.open('" + site + "','_blank');")
    time.sleep(1)

pyautogui.click(129, 10, button='middle')
time.sleep(1)
pyautogui.click(129, 10, button='left')

time.sleep(7200)

'Abrindo abas Simultâneas Com o Pyautogui e Selenium'