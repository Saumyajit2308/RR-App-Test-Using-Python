from appium import webdriver


def test_FailRegTCNotSelected():
    desired_cap = {
        "deviceName": "071607ec06460f03",
        "platformName": "android",
        "appPackage": "com.aimia.android.musgrave",
        "appActivity": "com.aimia.android.musgrave.MainActivity"
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
    driver.implicitly_wait(30)
    driver.find_element_by_xpath("//android.widget.TextView[@text='Register']").click()
    driver.find_element_by_xpath("//android.widget.EditText[@text='Card Number']").send_keys("00044336377")
    driver.find_element_by_xpath("//android.widget.TextView[@text='Submit']").click()
    driver.find_element_by_xpath("//android.widget.TextView[@text='Register via Email']").click()
    driver.find_element_by_xpath("//android.widget.EditText[@text='First Name']").send_keys("Sam")
    driver.find_element_by_xpath("//android.widget.EditText[@text='Last Name']").send_keys("Test")
    driver.find_element_by_xpath("//android.widget.EditText[@text='Email']").send_keys("samtest1234567@gmail.com")
    driver.find_element_by_xpath("//android.widget.EditText[@text='Password']").send_keys("Qwerty123")
    driver.find_element_by_xpath("//android.widget.TextView[@bounds='[1232,938][1320,1027]']").click()
    driver.find_element_by_xpath("//android.widget.EditText[@text='Confirm Password']").send_keys("Qwerty123")
    driver.find_element_by_xpath("//android.widget.TextView[@bounds='[1232,1118][1320,1207]']").click()
    driver.find_element_by_xpath("//android.view.ViewGroup[@bounds='[907,1522][1107,1602]']").click()
    driver.find_element_by_xpath("//android.view.ViewGroup[@bounds='[296,1522][496,1602]']").click()
    driver.find_element_by_xpath("//android.widget.TextView[@text='Terms & Conditions']").click()
    driver.find_element_by_xpath("//android.view.ViewGroup[@bounds='[1216,216][1368,369]']").click()
    driver.find_element_by_xpath("//android.widget.TextView[@text='Privacy Policy']").click()
    driver.find_element_by_xpath("//android.view.ViewGroup[@bounds='[1216,216][1368,369]']").click()
    driver.find_element_by_xpath("//android.widget.TextView[@text='Confirm']").click()

    driver.implicitly_wait(3)

    checkTC = driver.find_element_by_xpath(
        "//android.widget.ImageView[@bounds='[72,2019][168,2115]']").is_selected()

    if not checkTC:
        print("Please accept T&C and retry test")
