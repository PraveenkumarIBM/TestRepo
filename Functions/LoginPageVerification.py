import time
import allure
from allure_commons.types import AttachmentType
from hamcrest import assert_that, equal_to
from selenium.webdriver.common.by import By
from utilities.customlogger import LogGen
logger = LogGen.loggen()

class LoginpageVerification():
    def __init__(self, driver):
        self.driver = driver
    def test_loginpage_verification(self):
        logger.info("Login page verification")
        self.driver.execute_script("document.body.style.zoom='75%'")
        time.sleep(5)
        allure.attach(self.driver.get_screenshot_as_png(),name="Dashboard Page",attachment_type=AttachmentType.PNG)
        CI = self.driver.find_element(By.XPATH, "//span[contains(text(),'Content Intelligence')]")
        logger.info("******Verify the title of home page***********")
        logger.info("Title of home page is "+ CI.text)
        homepagename = CI.text
        assert_that("Content Intelligence", equal_to(homepagename))
