import logging
import time

from selenium.common import TimeoutException
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

        quantity = self.quamtity_input
        quantity_text = quantity.text
        print(f"Quantity of the product after product added: {quantity_text}")

    def cart_decrement_update(self):

        cart_decrement_button = self.cart_decrement_icon
        cart_decrement_button.click()

        quantity = self.quamtity_input
        quantity_text = quantity.text
        print(f"Quantity of the product after product added: {quantity_text}")
        time.sleep(5)


    def total_price(self):

        # cart_decrement_button = self.cart_decrement_icon
        # cart_decrement_button.click()

        total_price = self.total_price_input
        total_price_text = total_price.text
        print(f"Total Price of the product is: {total_price_text}")

    def remove_product_from_cart(self):

        product = WebDriverWait(self.driver,2).until(
            EC.presence_of_element_located((By.XPATH,'//div[contains(@class,\'flex space-x-2 justify-between items-start\')]//span[contains(@class,\'select-none text-lg leading-none flex items-center justify-center\')]//*[name()=\'svg\']'))

        )
        product.click()

        WebDriverWait(self.driver, 2).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()  # or alert.dismiss()
        time.sleep(5)















