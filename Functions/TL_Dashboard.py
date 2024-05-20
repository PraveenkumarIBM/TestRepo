import time
import pytest
from hamcrest import *
# assert_that, equal_to)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
#from pynput.keyboard import Controller, Key
import openpyxl
from utilities.customlogger import LogGen
from pageObjects.Graphs import graphs
import allure
from allure_commons.types import AttachmentType
from Functions.ScreenshotFile import screenshotfile
path = "./testData/Login_shrri.xlsx"
workbook = openpyxl.load_workbook(path)
Sheet = workbook.get_sheet_by_name('Login')
Execution = workbook.get_sheet_by_name('Execution')

logger = LogGen.loggen()
@pytest.mark.usefixtures("init_driver2")
class BaseTest:
    pass

class Dashboard(BaseTest):
    def __init__(self, driver):
       self.driver = driver

    global totalcount

    def clearexcelvaues(self):
        for x in range(2,10):
            Execution['B' + str(x)].value = ''
        workbook.save(path)
    def getSourcevsReceivedTotalItemsCount(self):
        totalitemscount_str = self.driver.find_element(By.XPATH, "(//div[@class='_card_sub_title_1pdi6_31'])[1]").text
        totalitemscount_list = totalitemscount_str.split()
        totalitemscount = int(totalitemscount_list[0])
        print("Total count in sourcevsreceived", totalitemscount)
        logger.info("Got total counts in source vs received graph")
        return totalitemscount
    def verificationOfAppliedFiltersInPopups(self):
        filters = self.driver.find_element(By.XPATH,"(//div[@class='_filters_applied_list_193b9_97'])[2]")
        time.sleep(2)
        Confscorefilter = self.driver.find_element(By.XPATH,"(//fieldset[@class='cds--checkbox-group _filter_by_confidence_score_wrapper_193b9_36'])[2]")
        time.sleep(2)
        search = self.driver.find_element(By.XPATH,"(//div[@class='cds--search cds--search--lg _search_input_193b9_143 cds--toolbar-search-container-expandable'])[2]")
        time.sleep(2)
        filtericon = self.driver.find_element(By.XPATH,"(//div[@class='_grid_action_btn_193b9_59'])[3]")
        time.sleep(2)
        download = self.driver.find_element(By.XPATH,"(//div[@class='_grid_action_btn_193b9_59'])[4]")
        time.sleep(2)
        if filters.is_displayed() and Confscorefilter.is_displayed() and search.is_displayed() and filtericon.is_displayed() and download.is_displayed():
            logger.info("Filters , confidence score filters, search, filter icon and download button are disaplyed in popups")
            print("Filters , confidence score filters, search, filter icon and download button are disaplyed in popups")
    def getDocumentStatusTotalItemsCount(self):
        time.sleep(5)
        totalitemscount_str = self.driver.find_element(By.XPATH, "(//div[@class='_card_sub_title_1pdi6_31'])[2]").text
        totalitemscount_list = totalitemscount_str.split()
        totalitemscount = int(totalitemscount_list[2])
        print("Total count in document status", totalitemscount)
        logger.info("Got total counts in document status graph")
        return totalitemscount

    def getDocumentchartCount(self, i):
        time.sleep(5)
        totalitemscount_str = self.driver.find_element(By.XPATH, "(//div[@class='_card_sub_title_1pdi6_31'])["+str(i)+ "]").text
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, "(//div[@class='_card_sub_title_1pdi6_31'])["+str(i)+ "]")).perform()
        totalitemscount_list = totalitemscount_str.split()
        totalitemscount = int(totalitemscount_list[1])
        print("Total count in graph", totalitemscount)
        logger.info("Got total counts graph")
        return totalitemscount
    def clickBarandGetCountMatch(self,totalcount,barvalue,title):
        g = graphs(self.driver)
        d = Dashboard(self.driver)
        time.sleep(3)
        modalheader = self.driver.find_element(By.XPATH, "//div[@class='_modal_title_1joia_29']").text
        assert_that(title, equal_to(modalheader))
        time.sleep(3)
        d.verificationOfAppliedFiltersInPopups()
        time.sleep(3)
        itemscount_str = self.driver.find_element(By.XPATH,
                                                  "(//div[@class='cds--pagination__left']/span)[2]").text
        itemscount_list = itemscount_str.split()
        totalcount += int(itemscount_list[2])
        print("list strings in itemscount", itemscount_list)
        print("total count", totalcount)
        assert_that(barvalue, equal_to(int(itemscount_list[2])))
        time.sleep(3)
        g.closebutton()
        time.sleep(3)
        return totalcount

    def verificationOfSourcevsReceived(self):
        #g = graphs(self.driver)
        d = Dashboard(self.driver)
        s = screenshotfile(self.driver)
        barvalue = 0
        totalcount = 0
        itemscount = d.getSourcevsReceivedTotalItemsCount()
        title = 'Source vs Received documents'
        time.sleep(5)
        for i in range(0, 3):
            if i == 0:
                bars = self.driver.find_element(By.CSS_SELECTOR, "path.bar.fill-2-1-1:nth-of-type(1)")
                # bars.get_attribute('aria-label')
                barvalue = int(bars.get_attribute("aria-label"))
                print("Bar count", barvalue)
                if barvalue > 1:
                    self.driver.find_element(By.CSS_SELECTOR, "path.bar.fill-2-1-1:nth-of-type(1)").click()
                    logger.info("Clicked Email bar in source vs received")
                    totalcount = d.clickBarandGetCountMatch(totalcount, barvalue, title)
                    logger.info("Verified counts between bar and popup for Email upload")
            if i == 1:
                bars = self.driver.find_element(By.CSS_SELECTOR, "path.bar.fill-2-1-1:nth-of-type(2)")
                barvalue = int(bars.get_attribute("aria-label"))
                print("Bar count", barvalue)
                if barvalue > 1:
                    self.driver.find_element(By.CSS_SELECTOR, "path.bar.fill-2-1-1:nth-of-type(2)").click()
                    logger.info("Clicked SFTP bar in source vs received")
                    totalcount = d.clickBarandGetCountMatch(totalcount,barvalue,title)
                    logger.info("Verified counts between bar and popup for SFTP upload")
                    '''time.sleep(5)
                    modalheader = self.driver.find_element(By.XPATH, "//div[@class='_modal_title_1joia_29']").text
                    assert_that("Source vs Received documents", equal_to(modalheader))
                    time.sleep(3)
                    itemscount_str = self.driver.find_element(By.XPATH,
                                                              "(//div[@class='cds--pagination__left']/span)[2]").text
                    itemscount_list = itemscount_str.split()
                    totalcount += int(itemscount_list[2])
                    print("list strings in itemscount", itemscount_list)
                    time.sleep(5)
                    g.closebutton()'''
            if i == 2:
                bars = self.driver.find_element(By.CSS_SELECTOR, "path.bar.fill-2-1-1:nth-of-type(3)")
                barvalue = int(bars.get_attribute("aria-label"))
                print("Bar count", barvalue)
                if barvalue > 1:
                    self.driver.find_element(By.CSS_SELECTOR, "path.bar.fill-2-1-1:nth-of-type(3)").click()
                    logger.info("Clicked Manual bar in source vs received")
                    totalcount = d.clickBarandGetCountMatch(totalcount,barvalue,title)
                    logger.info('Verified counts between bar and popup for manual upload')
                    '''modalheader = self.driver.find_element(By.XPATH, "//div[@class='_modal_title_1joia_29']").text
                    assert_that("Source vs Received documents", equal_to(modalheader))
                    time.sleep(3)
                    itemscount_str = self.driver.find_element(By.XPATH,"(//div[@class='cds--pagination__left']/span)[2]").text
                    itemscount_list = itemscount_str.split()
                    totalcount += int(itemscount_list[2])
                    print("list strings in itemscount", itemscount_list)
                    time.sleep(5)
                    g.closebutton()'''
        time.sleep(5)
        print("total items count", totalcount)
        #assert_that(totalitemscount, equal_to(totalcount))
        assert_that(itemscount, equal_to(totalcount))
        Execution['B2'].value = 'yes'
        workbook.save(path)
        s.takescreenshot("SourceVsReceived")

    def verifyTheCountsMatchingForCompletedInDocumentStatusGraph(self):
        count = self.driver.find_element(By.XPATH,"//div[@class='_chart_tile_wrapper_1636t_17']/div[1]/div[2]").text
        print("count for completed graph",count)
        return int(count)
    def verifyTheCountsMatchingForPendingInDocumentStatusGraph(self):
        count = self.driver.find_element(By.XPATH,"//div[@class='_chart_tile_wrapper_1636t_17']/div[2]/div[2]").text
        print("count for pending graph", count)
        return int(count)
    def verifyTheCountsMatchingForReworkInDocumentStatusGraph(self):
        count = self.driver.find_element(By.XPATH,"//div[@class='_chart_tile_wrapper_1636t_17']/div[3]/div[2]").text
        print("count for rework graph", count)
        return int(count)
    def verifyTheCountsMatchingForNotAssignedInDocumentStatusGraph(self):
        count = self.driver.find_element(By.XPATH,"//div[@class='_chart_tile_wrapper_1636t_17']/div[4]/div[2]").text
        print("count for Not assigned graph", count)
        return int(count)

    def verificationOfDocumentStatusGraph(self):
        d = Dashboard(self.driver)
        s = screenshotfile(self.driver)
        totalcount = 0
        title = 'Document status'
        itemscount = d.getDocumentStatusTotalItemsCount()
        for i in range(0, 4):
            if i == 0:
                count = d.verifyTheCountsMatchingForCompletedInDocumentStatusGraph()
                if count > 0:
                    self.driver.find_element(By.XPATH,
                                             "//div[@class='_chart_tile_wrapper_1636t_17']/div[1]/div[2]").click()
                    totalcount = d.clickBarandGetCountMatch(totalcount,count,title)
            time.sleep(5)
            if i == 1:
                count = d.verifyTheCountsMatchingForPendingInDocumentStatusGraph()
                if count > 0:
                    self.driver.find_element(By.XPATH,
                                             "//div[@class='_chart_tile_wrapper_1636t_17']/div[2]/div[2]").click()
                    totalcount = d.clickBarandGetCountMatch(totalcount, count, title)
            time.sleep(5)
            if i == 2:
                count = d.verifyTheCountsMatchingForReworkInDocumentStatusGraph()
                if count > 0:
                    self.driver.find_element(By.XPATH,
                                             "//div[@class='_chart_tile_wrapper_1636t_17']/div[3]/div[2]").click()
                    totalcount = d.clickBarandGetCountMatch(totalcount, count, title)
            time.sleep(5)
            if i == 3:
                count = d.verifyTheCountsMatchingForNotAssignedInDocumentStatusGraph()
                if count > 0:
                    self.driver.find_element(By.XPATH,
                                             "//div[@class='_chart_tile_wrapper_1636t_17']/div[4]/div[2]").click()
                    totalcount = d.clickBarandGetCountMatch(totalcount, count, title)
        time.sleep(5)
        print("total items count", totalcount)
        assert_that(itemscount, equal_to(totalcount))
        Execution['B3'].value = 'yes'
        workbook.save(path)
        s.takescreenshot("DocumentStatus")
        #allure.attach(self.driver.get_screenshot_as_png(), name='documentstatus', attachment_type=AttachmentType.PNG)

    def verification_of_urgent_graph(self):
        d = Dashboard(self.driver)
        s = screenshotfile(self.driver)
        title = 'Urgent documents status'
        totalcount = 0
        itemscount = d.getDocumentchartCount(3)
        barcounts_list = self.driver.find_elements(By.XPATH,"(//*[local-name() ='svg' and @class='cds--cc--stacked-bar']/*[local-name()='g'])[3]/*[local-name()='path']")
        barcounts = len(barcounts_list)
        for i in range(barcounts):
            if i != barcounts:
                barcount = int(self.driver.find_element(By.XPATH,"((//*[local-name() ='svg' and @class='cds--cc--stacked-bar']/*[local-name()='g'])[3]/*[local-name()='path'])["+ str(i+1)+"]").get_attribute("aria-label"))
                if barcount > 0:
                    self.driver.find_element(By.XPATH,"((//*[local-name() ='svg' and @class='cds--cc--stacked-bar']/*[local-name()='g'])[3]/*[local-name()='path'])[" + str(i+1) + "]").click()
                    totalcount = d.clickBarandGetCountMatch(totalcount,barcount,title)
        time.sleep(5)
        print("total items count", totalcount)
        assert_that(itemscount, equal_to(totalcount))
        Execution['B4'].value = 'yes'
        workbook.save(path)
        s.takescreenshot("UrgentDocument")
        #allure.attach(self.driver.get_screenshot_as_png(), name='Urgentdocument', attachment_type=AttachmentType.PNG)

    def verification_of_Document_Indexing(self):
        d = Dashboard(self.driver)
        s = screenshotfile(self.driver)
        title = 'My Documents indexed'
        totalcount = 0
        itemscount = d.getDocumentchartCount(4)
        barcounts_list = self.driver.find_elements(By.XPATH,"(//*[local-name() ='svg' and @class='cds--cc--grouped-bar']/*[local-name()='g'])/*[local-name()='path']")
        barcounts = len(barcounts_list)
        actions = ActionChains(self.driver)
        actions.move_to_element(
            self.driver.find_element(By.XPATH, "((//*[local-name() ='svg' and @class='cds--cc--grouped-bar']/*[local-name()='g'])/*[local-name()='path'])[1]")).perform()

        for i in range(barcounts):
                barcount = int(self.driver.find_element(By.XPATH,"((//*[local-name() ='svg' and @class='cds--cc--grouped-bar']/*[local-name()='g'])/*[local-name()='path'])[" + str(
                                                            i + 1) + "]").get_attribute("aria-label"))
                if barcount == 1 or barcount == 2 or barcount == 3:
                    totalcount += barcount
                    print("total count if less than 3",totalcount)
                elif barcount >3 :
                    self.driver.find_element(By.XPATH,"((//*[local-name() ='svg' and @class='cds--cc--grouped-bar']/*[local-name()='g'])/*[local-name()='path'])[" + str(i + 1) + "]").click()
                    totalcount = d.clickBarandGetCountMatch(totalcount, barcount, title)

        time.sleep(5)
        print("total items count", totalcount)
        assert_that(itemscount, equal_to(totalcount))
        Execution['B5'].value = 'yes'
        workbook.save(path)
        s.takescreenshot("Document_Indexing")
        #allure.attach(self.driver.get_screenshot_as_png(), name='documentIndexing', attachment_type=AttachmentType.PNG)

    def verification_of_By_Ageing_graph(self):
        d = Dashboard(self.driver)
        s = screenshotfile(self.driver)
        title = 'By ageing'
        totalcount = 0
        barcounts_list = self.driver.find_elements(By.XPATH,"//div[@class='_tiles_wrapper_1cpkh_8 undefined ']")
        barcounts = len(barcounts_list)
        actions = ActionChains(self.driver)
        actions.move_to_element(
            self.driver.find_element(By.XPATH,"//div[@class='_tiles_wrapper_1cpkh_8 undefined ']")).perform()

        for i in range(barcounts):
            barcount = int(self.driver.find_element(By.XPATH,"(//div[@class='_tiles_wrapper_1cpkh_8 undefined ']/div[2])["+str(i+1)+"]").text)
            print("bar counts is ", barcount)
            if barcount > 0:
              self.driver.find_element(By.XPATH,"(//div[@class='_tiles_wrapper_1cpkh_8 undefined '])[" + str(
                                                 i + 1) + "]").click()
              totalcount = d.clickBarandGetCountMatch(totalcount, barcount, title)

        time.sleep(5)
        print("total items count", totalcount)
        #assert_that(itemscount, equal_to(totalcount))
        s.takescreenshot("ByAgeing")
        Execution['B6'].value = 'yes'
        workbook.save(path)
        #allure.attach(self.driver.get_screenshot_as_png(), name='ByAgeing', attachment_type=AttachmentType.PNG)

    def verificationOfCompletedDocumentusingScanID(self):
        g = graphs(self.driver)
        s = screenshotfile(self.driver)
        scanid = Sheet['J2'].value
        time.sleep(5)
        g.clickRestFilter()
        g.clickPendingcheckbox()
        #adding snippet for date range selection
        g.clickDateRangeTab()
        g.setScanStartDate('03/01/2024')
        g.clickApplyFilter()
        g.clickCompletedInDocumentStatus()
        g.clickSearchAndEnterScanIdInModals(scanid)
        g.movetoelementofcompleted()
        completed = self.driver.find_element(By.XPATH, "(//table[@class='cds--data-table cds--data-table--lg cds--data-table--sort'])[2]/tbody/tr/td[13]/span").text
        time.sleep(2)
        assert_that(completed,equal_to('Completed'))
        logger.info("The mentioned scan id is completed")
        g.closebutton()
        s.takescreenshot("Doc_Completed")
        Execution['B7'].value = 'yes'
        workbook.save(path)

    def verificationOfCountChangesinDocumentIndexingGraph(self):
        d=Dashboard(self.driver)