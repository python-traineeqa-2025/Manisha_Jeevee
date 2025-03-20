from selenium.webdriver.common.by import By

class Checkout_Locators(object):

    CHECKOUT_BUTTON = (By.XPATH,'//button[contains(@class,\'w-full\')]')
    ADD_ADDRESS = (By.XPATH,'//div[contains(@class,\'link-sm\')][normalize-space()=\'Add Address\']')
    SELECT_PROVINCE = (By.XPATH, "//input[@id='react-select-province-input']")
    PROVINCE_DROPDOWN = (By.XPATH,'//div[contains(@class, \'css-ackcql\')]')
    SELECT_CITY = (By.XPATH,"//input[contains(@id,'react-select-cities-input')]")
    SELECT_AREA = (By.XPATH,'//input[contains(@id,\'react-select-areas-input\')]')
    SELECT_ADDRESS = (By.XPATH,'//input[@placeholder=\'Enter Label (eg: Home, Office etc...)\']')
    SELECT_LANDMARK = (By.XPATH,'//input[@placeholder=\'Enter Landmark\']')
    SELECT_NUMBER = (By.XPATH,'//input[@placeholder=\'Enter Alternate Number\']')
    ADD_ADDRESS_BUTTON = (By.XPATH,'//button[normalize-space()=\'Add Address\']')


