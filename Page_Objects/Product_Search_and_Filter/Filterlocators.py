from selenium.webdriver.common.by import By

class Filter_Locators(object):

    SEARCHBAR = (By.XPATH,'//div[contains(@class,\'hidden sm:block grow mx-2.5 py-2.5 relative w-auto\')]//input[contains(@placeholder,\'Search for Products, Medicine...\')]')
