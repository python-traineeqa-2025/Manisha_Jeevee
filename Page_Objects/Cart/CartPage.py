import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Page_Objects.Cart.CartProperties import Cart_Properties
from selenium.webdriver.support import expected_conditions as EC



class Cart(Cart_Properties):

    def __init__(self,driver):

        self.driver = driver

    def cart(self):

        cart_btn = self.add_to_cart_button_input
        cart_btn.click()

    def cart_icon(self):

        carticon = self.carticon_input
        carticon.click()

    def is_product_in_cart(self, product_name):
        try:
            # Wait for the cart items to be visible
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f'//div[contains(text(), "{product_name}")]'))
            )
            # product = self.driver.find_element(By.XPATH, f'//div[contains(text(), "{product_name}")]')
            return True
        except:
            return False

    def cart_increment_update(self):

        cart_increment_button = self.cart_increment_icon
        cart_increment_button.click()
        time.sleep(5)

        quantity = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            'body > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)'))
        )
        quantity_text = quantity.text
        print(f"Quantity of the product after product added: {quantity_text}")

    def cart_decrement_update(self):

        cart_decrement_button = self.cart_decrement_icon
        cart_decrement_button.click()

        quantity = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            'body > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)'))
        )
        quantity_text = quantity.text
        print(f"Quantity of the product after product added: {quantity_text}")
        time.sleep(5)


    # def total_price(self):
    #
    #
    #     total_price = self.total_price_input
    #     total_price_text = total_price.text  # Correct method to get the text
    #     return total_price_text









