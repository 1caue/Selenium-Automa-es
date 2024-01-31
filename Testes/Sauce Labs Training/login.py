from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver 
import time, pyautogui

path = 'chromedriver.exe'
chrome_service = Service(path)
chrome_options = webdriver.ChromeOptions()

pyautogui.moveTo(1693, 631) # movendo o curso para não háver confusões no pyautogui
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Entrando no site
driver.get('https://www.saucedemo.com/')
pyautogui.hotkey('win', 'up')
time.sleep(0.5)

# Digitando login para entrar
log = driver.find_element(By.ID, 'user-name')
log.send_keys('standard_user')
pyautogui.press('tab')
time.sleep(0.5)

# Digitando senha para entrar
password = driver.find_element(By.ID, 'password')
password.send_keys('secret_sauce')
pyautogui.press('enter')
time.sleep(0.5)

# Adicionando produtos no carrinho
product1 = driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light')
product1.click()
time.sleep(0.5)

product2 = driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
product2.click()
time.sleep(0.5)

product3 = driver.find_element(By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)')
product3.click()
time.sleep(0.5)

# Indo até o carrinho
cart = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
cart.click()
time.sleep(0.5)

# Clicando no botão para fazer checkout
checkout = driver.find_element(By.ID, 'checkout')
checkout.click()
time.sleep(0.5)

# Digidando dados para fazer checkout
fn = driver.find_element(By.ID, 'first-name') 
fn.send_keys('Caue') 
pyautogui.press('tab')
time.sleep(0.5)

ln = driver.find_element(By.ID, 'last-name')
ln.send_keys('Santos Pereira')
pyautogui.press('tab')
time.sleep(0.5)

pc = driver.find_element(By.ID, 'postal-code')
pc.send_keys('45570')

# Clicando no "Continue" para ir no para finalização
capture = pyautogui.locateOnScreen(r'C:\Users\CAUÊ\Documents\Selenium\Testes\Sauce Labs Training\continue.png')
pyautogui.click(capture, duration=0.3)
pyautogui.scroll(-500)

# Finalizando compra
finish = pyautogui.locateOnScreen(r'C:\Users\CAUÊ\Documents\Selenium\Testes\Sauce Labs Training\finish.png')
pyautogui.click(finish, duration=0.3)

# Voltando para home
back_home = pyautogui.locateOnScreen(r'C:\Users\CAUÊ\Documents\Selenium\Testes\Sauce Labs Training\back_home.png')
pyautogui.click(back_home, duration=0.3)

time.sleep(180)

'Script criado com o intuito de Automatizar o Login, Compra e Finalização de checkout do site da Sauce Labs Training'