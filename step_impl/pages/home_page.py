from selenium.webdriver.common.by import By
from step_impl.pages.base_page import BasePage
import time


class HomePageLocators:
    """ This is the class for home page locators. All home page locators should come here """
    SIGN_OFF_LINK   = (By.XPATH, "//button[contains(text(), 'Sign out')]")
    AVATAR          = (By.XPATH, "//img[@class='avatar float-left mr-1']")


class HomePage(BasePage):
    """ Home page actions """

    def is_home_page_visible(self):
        assert self.is_displayed(HomePageLocators.AVATAR), "Avatar is not displayed" 

    def is_home_page_not_visible(self):
        assert self.is_not_displayed(HomePageLocators.AVATAR), True

    def logout(self):
        self.click(HomePageLocators.AVATAR)
        self.click(HomePageLocators.SIGN_OFF_LINK)    
