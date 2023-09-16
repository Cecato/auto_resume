#libraries
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By

#files
from authentication.login import login
from utils.vagas import clickar_vagas

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.linkedin.com/")


try:
    
    login(driver)
    
    clickar_vagas(driver)

    time.sleep(50)
    driver.quit()
except Exception as e:
    print('Error', format(e))
    driver.quit()

sys.exit()