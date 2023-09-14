from selenium.webdriver.common.by import By
class UserNamePwd():

    def __init__(self,driver):
        self.driver=driver


        self.email="//input[@type='email']"
        self.Next_button= "//input[@id='idSIButton9']"
        self.Credential_SignIn= "(//span[@id='credentialSignin']/following::span)[1]"
        self.User_Name= "//input[@id='user-name-input']"
        self.Password_Input="//input[@id='password-input']"
       
    

    def enter_Email(self,user):
        self.driver.find_element(By.XPATH, self.email).send_keys(user)


    def next_Button(self):
        self.driver.find_element(By.XPATH, self.Next_button).click()

    
    def credential_SignIn(self):
        self.driver.find_element(By.XPATH, self.Credential_SignIn).click()

    def userName(self,user):
         self.driver.find_element(By.XPATH, self.User_Name).send_keys(user)

    def password_Input(self,pwd):
        self.driver.find_element(By.XPATH, self.Password_Input).send_keys(pwd)

   

