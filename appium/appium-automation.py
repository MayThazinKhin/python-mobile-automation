from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

desired_caps = {
    "platformName": "Android",   
    "deviceName": "DeviceSerial",
    "appPackage": "com.instagram.android",
    "appActivity": "com.instagram.android/com.instagram.mainactivity.InstagramMainActivity",  
    "automationName": "UiAutomator2",   
    "noReset": True,
    "newCommandTimeout": 600,
    "orientation": "PORTRAIT"
}

driver = webdriver.Remote('http://127.0.0.1:4723', 
    options=AppiumOptions().load_capabilities(desired_caps))
wait = WebDriverWait(driver, 20)


def login():
    login_button = driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Log in']")
    login_button.click()

    time.sleep(10)

def navigate_to_menu():
    menu = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.view.View[@content-desc='Search and explore']")))
    menu.click()

def change_orientation():
    if driver.orientation == "PORTRAIT":
        driver.orientation = "LANDSCAPE"
    else:
        driver.orientation = "PORTRAIT"

login()
navigate_to_menu()
change_orientation()

driver.quit()
