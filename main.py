from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
import time

CHROME_DRIVER_PATH = r"C:\Users\erick\system32\Chrome_Driver\chromedriver_win32\chromedriver.exe"
USERNAME = "Your CUI"
PASSWORD = "Your Password"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get("http://extranet.unsa.edu.pe/encuesta2/")
driver.find_element_by_xpath('//*[@id="cuerpo"]/fieldset/table/tbody/tr/td/fieldset/form/table/tbody/tr[2]/td[2]/input').send_keys(USERNAME)
driver.find_element_by_xpath('//*[@id="cuerpo"]/fieldset/table/tbody/tr/td/fieldset/form/table/tbody/tr[3]/td[2]/input').send_keys(PASSWORD)
driver.find_element_by_xpath('//*[@id="logueo"]').click()
time.sleep(1)

lista_enlaces_encuestas = []
elems = driver.find_elements_by_tag_name("a")
# elems[3].click() prueba para cliclear una encuesta
# Obtengo los enlaces
elems[2].click()
time.sleep(1)
datos = driver.find_elements_by_css_selector("input[type='radio']")
for i in datos:
    i.click()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="agrega"]').click()




    # print(elem.get_attribute("href"))
# print(lista_enlaces_encuestas)
