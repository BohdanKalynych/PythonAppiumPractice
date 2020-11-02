from appium import  webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
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

wait = WebDriverWait(driver, 25, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException,
                                                                       ElementNotSelectableException,
                                                                       NoSuchElementException])

ele = wait.until(lambda  x: x.find_element_by_android_uiautomator('new UiScrollable(new UiSelector()).scrollIntoView(text("LOGIN"))'))

actions = TouchAction(driver)
#actions.tap(None,700,1990,1)
actions.tap(ele, 640, 1700, 1)
actions.perform()

time.sleep(2)


