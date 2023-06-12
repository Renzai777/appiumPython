import pytest

from Pages.HomeScreen import HomeScreen
from TestCases.BaseTest import BaseTest


class Test_Home_Screen(BaseTest):


    def test_home_screen(self):
        home = HomeScreen(self.driver)
        home.click_on_my_products()