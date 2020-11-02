from selenium import webdriver
from pages.landing.landingPage import LandingPage

class titleTest():
    
    def test_validNumber(self):
        baseUrl = "https://wl.primeraplus.com.mx/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)
        
        lp = LandingPage(driver)
        # number = lp.login("acero.david.17@gmail.com", "PrimeraPlus123")
        # driver.implicitly_wait(5)
        title = lp.getMainTitle()
        assert title == "Bienvenido a la nueva experiencia de compra"
        
        driver.quit()


cc = titleTest()
cc.test_validNumber()