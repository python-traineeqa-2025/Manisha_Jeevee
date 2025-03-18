from selenium.webdriver.common.by import By


class Cart_locators(object):

    ADD_CART_BUTTON = (By.XPATH,'//button[normalize-space()=\'Add to Cart\']')
    CART_ICON = (By.XPATH,'//div[@class=\'cursor-pointer relative pr-2 shrink-0\']')
    CART_INCREMENT = (By.XPATH,'//div[@class=\'bg-white app-rounded space-y-3 mb-2\']//div[3]//*[name()=\'svg\']')
    CART_DECREMENT = (By.XPATH,'//div[@class=\'flex space-x-3 items-center\']//div[1]//*[name()=\'svg\']')
    TOTAL_PRICE = (By.XPATH,'//div[contains(@class,\'border-b pb-3 mb-3 mg-x-sm\')]//div[contains(@class,\'text-sm lg:text-base\')][normalize-space()=\'NPR 9520\']')