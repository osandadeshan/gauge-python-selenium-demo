from getgauge.python import before_suite, after_suite
from selenium import webdriver
from step_impl.pages.login_page import LoginPage
from step_impl.pages.home_page import HomePage


class PageFactory:
    driver = None
    login_page = None
    home_page = None

    
@before_suite
def init():
    PageFactory.driver = webdriver.Chrome()
    PageFactory.driver.maximize_window()
    PageFactory.login_page = LoginPage(PageFactory.driver)   
    PageFactory.home_page = HomePage(PageFactory.driver)


@after_suite
def close():
    PageFactory.driver.close()
