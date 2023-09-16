from selenium.webdriver.common.by import By

def clickar_vagas(driver):

    driver.implicitly_wait(0.5)
    txt_vagas = driver.find_elements(by=By.CLASS_NAME, value="global-nav__primary-item")
    x = 0
    for i in txt_vagas:
        if i.text == "Vagas":
            txt_vagas = txt_vagas[x]
            break
        x = x+1    

    txt_vagas.click()