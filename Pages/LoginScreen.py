from Pages.BasePage import BasePage
from Pages.HomeScreen import HomeScreen


class LoginScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    def login(self,mobileNumber,pin):
        self.click("permissionDialog_XPATH")
        self.click("existingUser_XPATH")
        self.type("enterMobileNumber_XPATH", mobileNumber)
        self.type("enterSixDigitPin_XPATH", pin)
        self.click("signIN_XPATH")
        return HomeScreen(self.driver)


