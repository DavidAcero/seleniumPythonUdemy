from selenium import webdriver
from selenium.webdriver.common.by import By



class LandingPage():
    
    def __init__(self, driver):
        self.driver = driver
        
    def getMainTitle(self):
        title = self.driver.find_element(By.TAG_NAME, "h2").text
        return title
    
    def login(self, username, password):
        self.driver.find_element(By.CLASS_NAME, "signin-button").click()
        self.driver.find_element(By.NAME, "email").send_keys(username)
        self.driver.find_element(By.CLASS_NAME, "w-modal-button").click()
        

        