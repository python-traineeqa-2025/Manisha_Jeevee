from selenium.webdriver.common.by import By


class Cart_locators(object):

    ADD_CART_BUTTON = (By.XPATH,'//button[normalize-space()=\'Add to Cart\']')
    CART_ICON = (By.XPATH,'//div[@class=\'cursor-pointer relative pr-2 shrink-0\']')
    CART_INCREMENT = (By.XPATH,'//div[@class=\'bg-white app-rounded space-y-3 mb-2\']//div[3]//*[name()=\'svg\']')
    CART_DECREMENT = (By.XPATH,'//div[@class=\'flex space-x-3 items-center\']//div[1]//*[name()=\'svg\']')
    QUANTITY = (By.CSS_SELECTOR,'body > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)')
    TOTAL_PRICE = (By.XPATH,'//div[@class=\'mg-x-sm\']//div[@class=\'font-bold text-sm sm:text-lg leading-none sm:leading-none shrink-0\']')

