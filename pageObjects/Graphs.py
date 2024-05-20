from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

class graphs:
    def __init__(self, driver):
        self.driver = driver

        self.bargraph = "path.bar.fill-2-1-1"
        self.getmodalheader = "//div[@class='_modal_title_1joia_29']"
        self.itemscount = "(//div[@class='cds--pagination__left']/span)[2]"
        self.modalclose = "//button[@class='cds--modal-close']"

    def BarinSrc(self):
        self.driver.find_element(By.CSS_SELECTOR, self.bargraph)

    def clickBarinSrc(self):
        bar = self.driver.find_element(By.CSS_SELECTOR, self.bargraph)
        bar.click()
        #self.driver.execute_script("arguments[0].click()", bar)
    def getModalHeaderTitle(self):
        self.driver.find_element(By.XPATH, self.getmodalheader)

    def getItemsCount(self):
        self.driver.find_element(By.CSS_SELECTOR,self.itemscount)

    def closebutton(self):
        close = self.driver.find_element(By.XPATH,self.modalclose)
        #close.click()
        self.driver.execute_script("arguments[0].click()", close)

    def clickRestFilter(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Reset filter')]").click()

    def clickPendingcheckbox(self):
        actions = ActionChains(self.driver)
        time.sleep(2)
        checkbox = self.driver.find_element(By.ID, "allPending1")
        actions.move_to_element(checkbox).perform()
        time.sleep(2)
        #checkbox.click()
        self.driver.execute_script("arguments[0].click();",checkbox)
    def clickDateRangeTab(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[@class='cds--tabs__nav-item cds--tabs__nav-link tab-btn']").click()
    def setScanStartDate(self,date):
        time.sleep(5)
        self.driver.find_element(By.ID, "scan-date-start").clear()
        time.sleep(1)
        self.driver.find_element(By.ID, "scan-date-start").send_keys(date)

    def clickApplyFilter(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Apply filter')]").click()

    def clickSearchAndEnterScanIdInModals(self,scanid):
        time.sleep(5)
        self.driver.find_element(By.XPATH, "(//input[@class='cds--search-input'])[2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//input[@class='cds--search-input'])[2]").send_keys(scanid)

    def clickCompletedInDocumentStatus(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@class='_chart_tile_wrapper_1636t_17']/div[1]/div[2]").click()

    def movetoelementofcompleted(self):
        actions = ActionChains(self.driver)
        time.sleep(2)
        completed = self.driver.find_element(By.XPATH, "(//table[@class='cds--data-table cds--data-table--lg cds--data-table--sort'])[2]/tbody/tr/td[13]/span")
        actions.move_to_element(completed).perform()
        time.sleep(2)
        #checkbox.click()
        #self.driver.execute_script("arguments[0].click();",checkbox)
