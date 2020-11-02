from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8'
desired_caps['deviceName'] = 'Pixel'
desired_caps['automatorName'] = 'UiAutomator2'
desired_caps['noSign'] = 'true'
desired_caps['app'] = ('/Users/bkalynych/Documents/TestApps/Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

ele_id = driver.find_element_by_id("com.code2lead.kwad:id/EnterValue")
ele_id.click()
time.sleep(3)
inp_field = driver.find_element_by_id("com.code2lead.kwad:id/Et1")
inp_field.send_keys("testTEXT")