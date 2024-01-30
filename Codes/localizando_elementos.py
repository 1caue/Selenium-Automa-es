from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

path = 'chromedriver.exe'
chrome_service = Service(path)
chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get('https://form.jotform.com/240175075976666')
print(driver.title)

pesquisa = driver.find_element(By.NAME, 'q3_fullName3[first]')
pesquisa.send_keys('Cauê')

sobrenome = driver.find_element(By.ID, 'last_3')
sobrenome.send_keys('Santos Pereira')

time.sleep(10)

try:
    main = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'last_3'))
    ) 
    
    email_element = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, '.form-input[data-type="control_email"] input'))
    )

    email_value = email_element.get_attribute('value')
    print(email_value)

finally:
    driver.quit() 
    
