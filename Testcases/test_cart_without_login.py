import logging
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Page_Objects.SearchProduct.Search import Searchbar
from Setup.Basetest import BaseTest

from Page_Objects.Cart.CartPage import Cart
from selenium.webdriver.support import expected_conditions as EC

class Test_cart(BaseTest):

    def test_cart_without_login(self):

        url = self.creds["BaseUrl"]
        self.driver.get(url)
        logging.info("Site Opened:")

        product_search = Searchbar(self.driver)
        product_search.search("Sunscreen")
        time.sleep(5)

        cart_button = Cart(self.driver)
        cart_button.cart()
        # time.sleep(5)

        logging.info("Login Pape poped up:")
