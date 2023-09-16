#libraries
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#files
from authentication.login import login


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.linkedin.com/")

def execute():

    login(driver)

    time.sleep(500000)
    driver.quit()


execute()

