from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time as t

PATH = 'chromedriver.exe'
chrome_service = Service(PATH)
chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get('https://form.jotform.com/240224663961658')

t.sleep(0.5)
name1 = driver.find_element(By.NAME, 'q7_nome[first]')
name1.send_keys('Cauê')

t.sleep(0.5)
name2 = driver.find_element(By.ID, 'last_7')
name2.send_keys('Santos Pereira')

t.sleep(0.5)
btn1 = driver.find_element(By.ID, 'label_input_3_0')
btn1.click()

t.sleep(0.5)
btn2 = driver.find_element(By.ID, 'label_input_4_0')
btn2.click()

t.sleep(0.5)
submit = driver.find_element(By.ID, 'input_2').click()
submit.click()

element = WebDriverWait(driver, 3)
element.until(Ec.element_to_be_clickable((By.XPATH, '/html/body/form/div[1]/ul/li[7]/div/div/button"]'))).click()

t.sleep(5)