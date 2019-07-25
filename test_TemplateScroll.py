import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

def test_Scroll():
        desired_cap = {
            "deviceName": "LGH870c027e397",
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
        driver.find_element_by_xpath("//android.view.ViewGroup[@bounds='[68,932][1372,1065]']").click()
        driver.find_element_by_xpath("//android.view.ViewGroup[@bounds='[499,1361][941,1487]']").click()
        driver.find_element_by_xpath("//android.view.ViewGroup[@bounds='[499,1353][941,1478]']").click()
        driver.find_element_by_xpath("//android.view.ViewGroup[@bounds='[499,1557][941,1682]']").click()
        driver.find_element_by_xpath("//android.view.ViewGroup[@bounds='[499,1353][941,1478]']").click()
        driver.find_element_by_xpath("//android.view.ViewGroup[@bounds='[133,694][551,838]']").click()
        driver.find_element_by_xpath("//android.view.ViewGroup[@bounds='[0,82][102,224]']").click()

        for i in range(3):
            touch = TouchAction(driver)
            touch.long_press(x=711, y=2419).move_to(x=711, y=1428).release().perform()
            time.sleep(2)