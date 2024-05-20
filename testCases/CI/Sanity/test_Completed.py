import time

import pytest
from Functions.TL_Dashboard import Dashboard
from utilities.customlogger import LogGen

@pytest.mark.usefixtures("init_driver2")
class BaseTest:
    pass
logger = LogGen.loggen()

class Test_VerifytheCompletedDocument(BaseTest):
    def test_dashboardVerification(self):
        dashboard = Dashboard(self.driver)
        dashboard.clearexcelvaues()
        dashboard.verificationOfCompletedDocumentusingScanID()
        time.sleep(3)
        self.driver.close()