from Pages.BasePage import BasePage


class HomeScreen(BasePage):

    def __init__(self,driver):
        super().__init__(driver)



    def click_on_my_products(self):
        self.click("myProducts_ANDROID_UIAUTOMATOR")
