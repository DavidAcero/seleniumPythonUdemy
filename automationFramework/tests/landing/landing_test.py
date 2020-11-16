from selenium import webdriver
from pages.landing.landingPage import LandingPage
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class titleTest(unittest.TestCase):
    
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LandingPage(self.driver)
    
    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("Admin", "admin123")
        result = self.lp.verifyLoginSuccesful()
        assert result == True

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("Admin", "wrongPassword")
        # title = lp.checkUser()
        result = self.lp.verifyLoginFailed()
        assert result == True
