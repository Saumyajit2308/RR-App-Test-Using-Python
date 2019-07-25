from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction

def test_Homescreen():
    desired_cap = {
        "deviceName": "071607ec06460f03",
        "platformName": "android",
        "appPackage": "com.aimia.android.musgrave",
        "appActivity": "com.aimia.android.musgrave.MainActivity"
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
    driver.implicitly_wait(30)
    driver.find_element_by_xpath("//android.widget.TextView[@text='Login']").click()
    driver.find_element_by_xpath("//android.widget.TextView[@text='Login via Email']").click()
    driver.find_element_by_xpath("//android.widget.EditText[@text='Email']").send_keys("saumyajit230895@gmail.com")
    driver.find_element_by_xpath("//android.widget.EditText[@text='Password']").send_keys("Qwerty123")
    driver.find_element_by_xpath("//android.view.ViewGroup[@bounds='[80,1129][1360,1297]']").click()
    driver.find_element_by_xpath("//android.view.ViewGroup[@bounds='[460,1785][980,1942]']").click()
    driver.find_element_by_xpath("//android.view.ViewGroup[@bounds='[460,1612][980,1769]']").click()
    driver.find_element_by_xpath("//android.view.ViewGroup[@bounds='[460,1852][980,2009]']").click()
    driver.find_element_by_xpath("//android.view.ViewGroup[@bounds='[460,1612][980,1769]']").click()
    driver.find_element_by_xpath("//android.widget.TextView[@text='My Statements']").click()
    for i in range(2):
        touch = TouchAction(driver)
        touch.long_press(x=711, y=2419).move_to(x=711, y=1428).release().perform()
        time.sleep(2)
    driver.find_element_by_xpath("//android.view.ViewGroup[@bounds='[0,96][120,278]']").click()
    driver.find_element_by_xpath("//android.widget.TextView[@bounds='[1304,1165][1380,1242]']").click()

    for i in range(3):
        touch = TouchAction(driver)
        touch.long_press(x=711, y=2419).move_to(x=711, y=1428).release().perform()
        time.sleep(2)
    driver.find_element_by_xpath("//android.view.ViewGroup[@bounds='[1216,216][1368,369]']").click()
