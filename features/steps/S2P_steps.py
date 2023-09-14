from behave import *
import unittest
from selenium import webdriver
import time
@given('I launch Chrome Browser')
def Chrome_Launch(context):
    context.driver = webdriver.Chrome();
    context.driver.maximize_window();
@when('I opened CI URL')
def Open_URL(context):
    context.driver.get('https://app-goldenplatform-ciui-qa-weurope-001.azurewebsites.net/')
    time.sleep(10)


