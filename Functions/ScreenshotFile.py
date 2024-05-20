import allure
from allure_commons.types import AttachmentType
class BaseTest:
    pass

class screenshotfile(BaseTest):
    def __init__(self, driver):
       self.driver = driver

    def takescreenshot(self,tcname):
        allure.attach(self.driver.get_screenshot_as_png(), name=tcname, attachment_type=AttachmentType.PNG)