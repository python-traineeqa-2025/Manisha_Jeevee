from selenium.webdriver.common.by import By

class Login_Locators(object):

    CREATE_ACCOUNT = (By.XPATH,'//div[contains(@class,\'user_greetings__29Sj5 md:block relative\')]//div[contains(@class,\'flex space-x-0.5 sm:space-x-1 lg:space-x-1.5 items-center cursor-pointer shrink\')]//*[name()=\'svg\']//*[name()=\'path\' and contains(@d,\'M47.76 482\')]')
    LOGIN = (By.XPATH,'//*[@id="__next"]/div[2]/div/div[1]/div/div[1]/div[2]/div/div[4]/div[1]/div[2]/div[2]/div[9]')
    MOBILE_NUMBER = (By.XPATH,'//input[@placeholder=\'Mobile Number *\']')
    PASSWORD = (By.XPATH,'//input[@placeholder=\'Password *\']')
    LOGIN_BTN = (By.XPATH,'//button[normalize-space()=\'Sign In\']')