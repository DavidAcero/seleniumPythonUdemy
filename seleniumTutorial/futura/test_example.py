from selenium import webdriver

def test_label():
        baseUrl = "https://futura.com.mx/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        
        driver.get(baseUrl)
        initial_test = driver.find_element_by_xpath("//h1[contains(text(),'Compra tus boletos en línea')]").text
        assert initial_test == "Compra tus boletos en línea"
        driver.close()
