from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

USERNAME = "YOUR USERNAME"
PASSWORD = "YOUR PASSWORD"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Here I'm setting the browser and the location of the driver
driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))

driver.get("http://extranet.unsa.edu.pe/encuesta2/")

#
# Getting Selenium elements
userInput = driver.find_element(By.NAME, value='txt_usuario')
passwordInput = driver.find_element(By.NAME, value="txt_password")

userInput.click()
userInput.send_keys(USERNAME)

passwordInput.click()
passwordInput.send_keys(PASSWORD)

# Opening surveys
driver.find_element(By.NAME, value="logueo").click()


# I'm in !!!!
# Waithing for 1 sec
time.sleep(1)

numberOfIterations = driver.find_elements(By.CSS_SELECTOR, 'a[href="#"]')

for number in numberOfIterations:
    # # MASTER KEY
    linkList = driver.find_element(By.CSS_SELECTOR, 'a[href="#"]')
    linkList.click()

    time.sleep(1)
    listButtons = driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")
    for button in listButtons:
        button.click()

    driver.find_element(By.NAME, "agrega").click()
    time.sleep(1)

print("ENCUESTA CONTESTADA EXITOSAMENTE!!!")





