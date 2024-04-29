import time
import pytest
import allure
from allure_commons.types import AttachmentType
from hamcrest import assert_that, equal_to
from selenium.webdriver.common.by import By

from Functions.TopFilter import TopFilterFunctionality
from Functions.LoginPageVerification import LoginpageVerification
from utilities.customlogger import LogGen
@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


logger = LogGen.loggen()


class Test_VerifyTopFilterFunctionality(BaseTest):

    def test_TC018_verify_top_filter_functionality(self):
        #login page verification
        loginverify=LoginpageVerification(self.driver)
        loginverify.test_loginpage_verification()
        time.sleep(6)
        # TopFilter Functionality validation
        topfilter=TopFilterFunctionality(self.driver)
        topfilter.top_filter()



















