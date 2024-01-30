from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium import webdriver 
import time, pyautogui

path = 'chromedriver.exe'
chrome_service = Service(path)
chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get('https://colorlib.com/etc/lf/Login_v1/index.html')
pyautogui.hotkey('win', 'up')

log = driver.find_element(By.NAME, 'email')
log.send_keys('caue@gmail.com')
time.sleep(0.5)

password = driver.find_element(By.NAME, 'pass')
password.send_keys('1234')
time.sleep(0.5)

button = driver.find_element(By.CLASS_NAME, 'login100-form-btn')
button.click()

time.sleep(7200)