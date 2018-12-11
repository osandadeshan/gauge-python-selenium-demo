from getgauge.python import step, DataStoreFactory
from step_impl.step_def.page_factory import PageFactory


@step('User navigates to the home page')
def is_home_page_visible():
    PageFactory.home_page.is_home_page_visible()

@step('User cannot navigate to the home page')
def is_home_page_not_visible():
    PageFactory.home_page.is_home_page_not_visible()

@step('Logout from the application')
def logout_from_the_application():
    PageFactory.home_page.logout()
    
    