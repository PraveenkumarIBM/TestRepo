import time
import pytest
import allure
from allure_commons.types import AttachmentType
from hamcrest import assert_that, equal_to
from selenium.webdriver.common.by import By
from Functions.SearchFunctionality import SearchFunctionalityverification
from Functions.LoginPageVerification import LoginpageVerification
from utilities.customlogger import LogGen
@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


logger = LogGen.loggen()


class Test_VerifySearchFunctionality(BaseTest):

    def test_TC10_verify_search_functionality(self):
        #login page verification
        loginverify=LoginpageVerification(self.driver)
        loginverify.test_loginpage_verification()
        time.sleep(3)
        #search functionality
        search=SearchFunctionalityverification(self.driver)
        search.search_functionality()















