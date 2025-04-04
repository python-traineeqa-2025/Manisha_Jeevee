from selenium.webdriver.common.by import By

class Navbar_Locators(object):
    SKIN = (By.XPATH,'(//div[@class=\'menu_mainCategory___SGsv\'])[1]')
    CLEANSERS = (By.XPATH,'//a[normalize-space()=\'Cleanser\']')