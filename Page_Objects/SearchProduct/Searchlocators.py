from selenium.webdriver.common.by import By

class Search_Locators(object):

    SEARCHBAR = (By.XPATH,'//div[contains(@class,\'hidden sm:block grow mx-2.5 py-2.5 relative w-auto\')]//input[contains(@placeholder,\'Search for Products, Medicine...\')]')
    AUTOSUGGESTION = (By.XPATH,"//div[@class='pt-2']//span")
    SEARCH_RESULT = (By.XPATH,'//div//p[contains(@class,\'text-sm sm:text-base break-word\')][normalize-space()=\'No match found\']')
