from selenium import webdriver
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
class LandingPage(SeleniumDriver):  
    
    log = cl.customLogger(logging.DEBUG)

    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    # Locators
    _email_field    = "txtUsername"
    _password_field = "txtPassword"
    _login_button   = "btnLogin"
    
    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)
        
    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)
        
    def clickLogin(self):
        self.elementClick(self._login_button)       

    def checkUser(self):
        title = self.driver.find_element(By.ID, "welcome").text
        return title
    
    def login(self, email="", password=""):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLogin()
        
    def verifyLoginSuccesful(self):
        result = self.isElementPresent("welcome")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("spanMessage")
        return result