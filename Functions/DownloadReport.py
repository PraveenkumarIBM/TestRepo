from selenium.webdriver.common.by import By

from pageObjects.DownloadReport import DownloadReport
from utilities.customlogger import LogGen
logger = LogGen.loggen()


class DownloadReportDashboard():
    def __init__(self, driver):
        self.driver = driver

    def download_report(self):
        report=DownloadReport(self.driver)
        report.click_download()





