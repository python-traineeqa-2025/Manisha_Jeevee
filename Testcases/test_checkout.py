import logging
import time

from Page_Objects.Cart.CartPage import Cart
from Page_Objects.Checkout.checkout import Checkout
from Page_Objects.Login.Loginpage import Login_page
from Page_Objects.SearchProduct.Search import Searchbar
from Setup.Basetest import BaseTest


class Test_checkout(BaseTest):

    def test_checkout(self):

        url = self.creds["BaseUrl"]
        self.driver.get(url)
        logging.info("Site Opened:")

        logged_in = Login_page(self.driver)
        mobile_num = self.creds["Mobile_Number"]
        pass_word = self.creds["Password"]

        logging.info("Now logging in to the system")

        logged_in.login(mobile_num, pass_word)
        time.sleep(10)

        # product_search = Searchbar(self.driver)
        # product_search.search("Sunscreen")
        # time.sleep(10)

        # cart_button = Cart(self.driver)
        # cart_button.cart()
        # time.sleep(5)

        carticon = Cart(self.driver)
        carticon.cart_icon()
        time.sleep(10)


        Checkout_BTN = Checkout(self.driver)
        Checkout_BTN.checkout()