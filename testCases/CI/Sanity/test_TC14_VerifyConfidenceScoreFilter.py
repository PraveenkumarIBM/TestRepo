import time
import pytest
import allure
from allure_commons.types import AttachmentType
from hamcrest import assert_that, equal_to
from selenium.webdriver.common.by import By

from Functions.ConfidencescoreFilter import ConfidencescoreFilter
from Functions.LoginPageVerification import LoginpageVerification
from utilities.customlogger import LogGen
from selenium.webdriver import ActionChains
@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


logger = LogGen.loggen()


class Test_VerifyConfidencescoreFilter(BaseTest):

    def test_TC014_verify_confidence_score_filter(self):
        #login page verification
        loginverify=LoginpageVerification(self.driver)
        loginverify.test_loginpage_verification()
        time.sleep(6)
        #confidencescore filter Functionality
        confidencescore=ConfidencescoreFilter(self.driver)
        confidencescore.confidence_score_filter()

















