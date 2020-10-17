from selenium import webdriver

class browserInteractions():
    def test(self):
        baseUrl = "https://futura.com.mx/"
        driver = webdriver.Chrome()
        
        # Maximize Window
        driver.maximize_window()
        
        # OpenUrl
        driver.get(baseUrl)
        
        # GetTitle
        title = driver.title
        print("Title is: " + title)
        
        # CurrentUrl
        currentUrl = driver.current_url
        print("CurrentUrl: " + currentUrl)
        
        # Refresh
        driver.refresh()
        
        # Open Another URL
        driver.get("http://google.com")
        
        # One Step Back
        driver.back()
        driver.forward()
        
        # Quit
        driver.close()
        
cc = browserInteractions()
cc.test()
