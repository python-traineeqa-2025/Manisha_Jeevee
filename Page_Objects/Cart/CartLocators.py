from selenium.webdriver.common.by import By


class Cart_locators(object):

    ADD_CART_BUTTON = (By.XPATH,'//button[normalize-space()=\'Add to Cart\']')
    CART_ICON = (By.XPATH,'//div[@class=\'cursor-pointer relative pr-2 shrink-0\']')
    CART_INCREMENT = (By.XPATH,'//div[@class=\'bg-white app-rounded space-y-3 mb-2\']//div[3]//*[name()=\'svg\']')
    CART_DECREMENT = (By.XPATH,'//div[@class=\'flex space-x-3 items-center\']//div[1]//*[name()=\'svg\']')
    TOTAL_PRICE = (By.CSS_SELECTOR,'//div[contains(@class,\'flex space-x-3 items-center\')]//div[1]')