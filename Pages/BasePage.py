import logging

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from Utilities import configReader
from  Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, configReader.readConfig("locator", locator)).click()
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_element(MobileBy.ACCESSIBILITY_ID. configReader.readConfig("locator", locator)).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, configReader.readConfig("locator", locator)).click()
        elif str(locator).endswith("_ANDROID_UIAUTOMATOR"):
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, configReader.readConfig("locator", locator)).click()
        log.logger.info("Clicking on an Element " + str(locator))

    def type(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, configReader.readConfig("locator", locator)).send_keys(value)
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_element(MobileBy.ACCESSIBILITY_ID, configReader.readConfig("locator", locator)).send_keys(value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, configReader.readConfig("locator", locator)).send_keys(value)
        log.logger.info("Type in an Element " + str(locator) + " entered the value as: " + str(value))

    def getText(self, locator):
        if str(locator).endswith("_XPATH"):
            text = self.driver.find_element(By.XPATH, configReader.readConfig("locator", locator)).text
        elif str(locator).endswith("_ACCESSIBILITYID"):
            text = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, configReader.readConfig("locator", locator)).text
        elif str(locator).endswith("_ID"):
            text = self.driver.find_element(By.ID,configReader.readConfig("locator", locator)).text
        log.logger.info("Getting text from an Element", str(locator))
        return text








