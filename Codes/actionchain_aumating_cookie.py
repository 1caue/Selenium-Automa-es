from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time, pyautogui

path = 'chromedriver.exe'
cs = Service(path)
co = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=cs, options=co)

driver.get('https://orteil.dashnet.org/cookieclicker/')

time.sleep(5)
pyautogui.click(483, 472)

driver.implicitly_wait(5)

cookie = driver.find_element(By.ID, 'bigCookie')
cookie_count = driver.find_element(By.ID, 'cookies')
items = [driver.find_element(By.ID, 'productPrice' + str(i)) for i in range(1, -1, -1)]

actions = ActionChains(driver)
actions.click(cookie)

for i in range(12000):
    actions.click(cookie)
    time.sleep(0.0001)
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    print(f'Contagem: {count}')
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()

time.sleep(100)
