import os
import time
from dotenv import load_dotenv
from selenium.webdriver.common.by import By

load_dotenv()
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')


def login(driver):
    try:
        title = driver.title
        assert 'LinkedIn: entre ou cadastre-se' in title

        driver.implicitly_wait(0.5)

        text_box_email = driver.find_element(by=By.ID, value="session_key")
        text_box_email.send_keys(EMAIL)

        text_box_password = driver.find_element(by=By.ID,  value="session_password")
        text_box_password.send_keys(PASSWORD)

        submit_button = driver.find_elements(by=By.CSS_SELECTOR, value="button")
        x = 0
        for button in submit_button:
            if button.text == "Entrar":
                submit_button = submit_button[x]
                break
            x = x+1

        submit_button.click()

        check_login(driver)

    except Exception as e:
        print('Error', format(e))

def check_login(driver):

    try:
        driver.implicitly_wait(0.5)
        box_check = driver.find_element(by=By.ID, value="securedDataExchange")

        while box_check is not None:
            print("Resolva a catch")
            time.sleep(1)
            box_check = driver.find_element(by=By.ID, value="securedDataExchange")
    
    except:
        pass

