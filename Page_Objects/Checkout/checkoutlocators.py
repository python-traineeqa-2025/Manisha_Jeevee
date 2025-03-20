from selenium.webdriver.common.by import By

class Checkout_Locators(object):

    CHECKOUT_BUTTON = (By.XPATH,'//button[contains(@class,\'w-full\')]')
    ADD_ADDRESS = (By.XPATH,'//div[contains(@class,\'link-sm\')][normalize-space()=\'Add Address\']')
    SELECT_PROVINCE = (By.XPATH, "//input[@id='react-select-province-input']")
    PROVINCE_DROPDOWN = (By.XPATH,'//div[contains(@class, \'css-ackcql\')]')
    SELECT_CITY = (By.XPATH,'//div[@id=\'react-select-cities-placeholder\']')
    # CITY_DROPDOWN = (By.XPATH,'//div[contains(@class,\' css-ackcql\')]')

