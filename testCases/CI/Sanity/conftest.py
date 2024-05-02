import pytest
from selenium import webdriver
import openpyxl
import time
import allure
from allure_commons.types import AttachmentType
import pageObjects
from pageObjects.Login import Login
#from utilities.customlogger import LogGen
from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()
options.add_argument('--headless')
path = "./testData/Login_Amway_NewUI.xlsx"
workbook = openpyxl.load_workbook(path)
Sheet = workbook.get_sheet_by_name('Login')
#import logging
#logging.basicConfig(filename="automation.log",format='%(asctime)s - %(levelname)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S',
#                   level=logging.INFO)
logger=LogGen.loggen()
@pytest.fixture(params=["chrome"],scope='class')
def init_driver(request):
    logger.info("Browser is initiated")
    #Driver Initialization
    if request.param =="chrome":
        web_driver=webdriver.Chrome(options=options)
    request.cls.driver = web_driver
    #maximize and open the application
    web_driver.maximize_window()
    web_driver.get(Sheet['A2'].value)
    time.sleep(10)
    allure.attach(request.driver.get_screenshot_as_png(), name="Microsoft Login Page Page", attachment_type=AttachmentType.PNG)
    #Entering microsoft ID and Password
    driver = web_driver
    login = Login(driver)
    logger.info("Microsoft authenticator step is initiated...")
    login.enter_email(Sheet['B2'].value)
    print('Microsoft value is entered')
    logger.info("Microsoft value is entered...")
    login.click_next()
    time.sleep(7)
    #click on w3 credentials link & enter w3 user name and password
    login.click_w3credentails()
    time.sleep(3)
    allure.attach(request.driver.get_screenshot_as_png(), name="W3 Credentials Page", attachment_type=AttachmentType.PNG)
    login.enter_w3username(Sheet['B2'].value)
    print('Entered w3 mail id...')
    login.enter_w3password(Sheet['C2'].value)
    time.sleep(3)
    print('Entered w3 password...')
    time.sleep(3)
    login.click_w3signin()
    time.sleep(25)
    login.click_staysignedin()
    time.sleep(10)
    logger.info("Successfully landing into content inteliigence page..")