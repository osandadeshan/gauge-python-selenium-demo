from selenium.webdriver.common.by import By
from step_impl.pages.base_page import BasePage
import time


class LoginPageLocators:
    """ This is the class for login page locators. All login page locators should come here """
    USER_NAME_TEXT      = (By.XPATH, "//input[@id='login_field']")
    PASSWORD_TEXT       = (By.XPATH, "//input[@id='password']")
    SIGN_IN_BUTTON      = (By.XPATH, "//input[@value='Sign in']")


class LoginPage(BasePage):
    URL = '{}/login'.format(BasePage.MAIN_URL)
    
    """ Login page actions """
    def visit(self):
        self.driver.get(self.URL)
    
    def login(self, user_name, password):
        self.set(LoginPageLocators.USER_NAME_TEXT, user_name)
        self.set(LoginPageLocators.PASSWORD_TEXT, password)
        self.click(LoginPageLocators.SIGN_IN_BUTTON)
        
