import pytest

from Pages.LoginScreen import LoginScreen
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider


class Test_Login(BaseTest):

    @pytest.fixture()
    @pytest.mark.parametrize("mobileNumber, pin", dataProvider.get_data("loginTest"))
    def test_login(self,mobileNumber,pin):
        login = LoginScreen(self.driver)
        login.login(mobileNumber, pin)




