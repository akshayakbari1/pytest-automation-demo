import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

CHROMEDRIVER_PATH = "C:/Users/aksha/driver/chromedriver.exe"
LOGIN_URL = "https://www.ambitionbox.com/reviews/stridely-solutions-reviews"
#USERNAME = "admin"
#PASSWORD = "Ak601@mokxa"


@pytest.mark.ambitionbox
def test_joget_login_and_open_app():
    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service)

    driver.get(LOGIN_URL)
    time.sleep(2)

    # Login
#    searchbox=driver.find_element(By.XPATH, "(//input[contains(@class,'css-11aywtz')])[1]")
    searchboxs = driver.find_elements(By.CSS_SELECTOR, "input.css-11aywtz")
    print(len(searchboxs))
    searchbox = searchboxs[1]

    searchbox.click()
    searchbox.send_keys("QA")
    time.sleep(5)
    searchbox.clear()
    searchbox.send_keys("QA")
  #  driver.find_element(By.NAME, "j_password").send_keys(PASSWORD + Keys.RETURN)
    time.sleep(3)

    # Go to app directly or click it

    time.sleep(3)


    # Check success
    assert "Success" in driver.page_source
    print("✅ App test passed")

    driver.quit()

    #kjsbvkjsnbv



if __name__ == "__main__":
    test_joget_login_and_open_app()
