from selenium import webdriver

class dropdown():
    def test(self):
    
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://futura.com.mx/")
        
        driver.implicitly_wait(3)
        origen = driver.find_element_by_id('origin-input')
        origen.send_keys("Acapulco")

cc = dropdown()
cc.test()