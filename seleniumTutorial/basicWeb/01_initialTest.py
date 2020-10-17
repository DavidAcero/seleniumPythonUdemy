from selenium import webdriver

class initialTest():
    def test(self):
        driver = webdriver.Chrome()
        driver.get("https://futura.com.mx/")
        
cc = initialTest()
cc.test()
