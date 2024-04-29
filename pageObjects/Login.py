from selenium.webdriver.common.by import By
class Login:
    def __init__(self,driver):
        self.driver = driver
        self.email = "//input[@type='email']"
        self.next ="//input[@type='submit']"
        self.w3credentails ="//label[contains(text(),'Use your w3id and password')]"
        self.w3username="//input[@name='username']"
        self.w3password= "//input[@name='password']"
        self.w3signin ="//button[contains(text(),'Sign in')]"
        self.W3staysignedYesNo = "//input[@type='submit']"
    def enter_email(self,email):
        self.driver.find_element(By.XPATH,self.email).send_keys(email)

    def click_next(self):
        self.driver.find_element(By.XPATH,self.next).click()

    def click_w3credentails(self):
        self.driver.find_element(By.XPATH,self.w3credentails).click()

    def enter_w3username(self,w3username):
        self.driver.find_element(By.XPATH,self.w3username).send_keys(w3username)

    def enter_w3password(self,w3password):
        self.driver.find_element(By.XPATH,self.w3password).send_keys(w3password)

    def click_w3signin(self):
        self.driver.find_element(By.XPATH,self.w3signin).click()

    def click_staysignedin(self):
        self.driver.find_element(By.XPATH,self.W3staysignedYesNo).click()

