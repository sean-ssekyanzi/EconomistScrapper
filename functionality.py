import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




url = "https://www.economist.com/"


def fetch_data(url):
    try:
        page = requests.get(url)
        response = page.text
        if page.status_code == 200:
            print("Data fetched successfully.")
        elif page.status_code == 404:
            print("Error 404: Page not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return response

def login():
    
    options = Options()
    options.headless = True
    options.add_experimental_option("detach", False)
    service = Service(executable_path=r'/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)
    try:
        driver.implicitly_wait(10)
        driver.get("https://www.economist.com")

        print("check1")
        
        print("check2")
        # WebDriverWait(driver, 5).until(
        #     EC.presence_of_element_located((By.XPATH, '//*[@id="notice"]/div[4]/div[2]/button'))
        # ).click()
        print("...check")
        driver.find_element(By.XPATH,'//*[@id="notice"]/div[4]/div[2]/button').click()
        print("check3")
        logger = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div[2]/header/div/div[2]/div/div/div/a[2]').click()
        print("check4")
        email_field = driver.find_element(By.XPATH,'//*[@id="input-7"]')
        email_field.send_keys("ramichael18@gmail.com")
        print("Email entered.")
        password_field = driver.find_element(By.XPATH,'//*[@id="input-9"]')
        password_field.send_keys("sekyanzi481")
        print("Password entered.")
        login_button = driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div[1]/div/div/div/div[2]/div/div/c-lwc-login-form/div/lightning-card/article/div[2]/slot/div[2]/div[6]/lightning-button/button').click()
        print("Login button clicked.")
        WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="SoGDz7"]/div/label/input')))
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="SoGDz7"]/div/label/input'))).click()
        print("By passed cloudflare")
        logged_in = "just a stmnt"
        print(logged_in)
    except Exception as e:
        print(e)
    return logged_in


# data = fetch_data(url)
# print(data)

play = login()
print(play)
