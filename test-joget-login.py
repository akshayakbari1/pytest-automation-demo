from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

CHROMEDRIVER_PATH = "C:/Users/aksha/driver/chromedriver.exe"
LOGIN_URL = "https://akshay.on.mymokxa.com/jw/web/login"
USERNAME = "admin"
PASSWORD = "Ak601@mokxa"

def test_joget_login_and_open_app():
    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service)

    driver.get(LOGIN_URL)
    time.sleep(2)

    # Login
    driver.find_element(By.NAME, "j_username").send_keys(USERNAME)
    driver.find_element(By.NAME, "j_password").send_keys(PASSWORD + Keys.RETURN)
    time.sleep(3)

    # Go to app directly or click it
    driver.get("https://akshay.on.mymokxa.com/jw/web/userview/sampleApp/v")
    time.sleep(3)


    # Check success
    assert "Success" in driver.page_source
    print("✅ App test passed")

    driver.quit()

if __name__ == "__main__":
    test_joget_login_and_open_app()
