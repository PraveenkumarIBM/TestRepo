import time
import pytest
import allure
from allure_commons.types import AttachmentType
from hamcrest import assert_that, equal_to
from selenium.webdriver.common.by import By

from Functions.ResetFilters import ResetFilters
from Functions.LoginPageVerification import LoginpageVerification
from utilities.customlogger import LogGen
from selenium.webdriver import ActionChains
@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


logger = LogGen.loggen()


class Test_VerifyResetFunctionality(BaseTest):

    def test_TC012_verify_reset_functionality(self):
        #login page verification
        loginverify=LoginpageVerification(self.driver)
        loginverify.test_loginpage_verification()
        time.sleep(6)
        #Reset Functionality
        reset=ResetFilters(self.driver)
        reset.reset_filters()

















