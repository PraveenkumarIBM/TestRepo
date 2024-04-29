import time
import pytest
import allure
from allure_commons.types import AttachmentType
from hamcrest import assert_that, equal_to
from selenium.webdriver.common.by import By

from pageObjects.DownloadReport import DownloadReport
from Functions.DownloadReport import DownloadReportDashboard
from Functions.LoginPageVerification import LoginpageVerification
from utilities.customlogger import LogGen
@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


logger = LogGen.loggen()


class Test_VerifyDownloadReport(BaseTest):

    def test_TC011_verify_downloadreport(self):
        #login page verification
        loginverify=LoginpageVerification(self.driver)
        loginverify.test_loginpage_verification()
        time.sleep(2)
        #Download Report
        self.driver.execute_script("document.body.style.zoom='100%'")
        time.sleep(3)
        report=DownloadReportDashboard(self.driver)
        report.download_report()
        # self.driver.execute_script("document.body.style.zoom='100%'")
        # self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[2]/div[4]/div[1]/div[1]/div[1]/section[1]/div[1]/div[4]/*[1]").click()
        logger.info("Dashboard Report is downloaded...")
        time.sleep(5)














