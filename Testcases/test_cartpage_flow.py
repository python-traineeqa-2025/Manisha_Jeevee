import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Page_Objects.SearchProduct.Search import Searchbar
from Setup.Basetest import BaseTest
from Page_Objects.Login.Loginpage import Login_page
from Page_Objects.Cart.CartPage import Cart
from selenium.webdriver.support import expected_conditions as EC

class Test_Cart(BaseTest):

    def test_cart(self):

        url = self.creds["BaseUrl"]
        self.driver.get(url)
        logging.info("Site Opened:")

        logged_in = Login_page(self.driver)
        mobile_num = self.creds["Mobile_Number"]
        pass_word = self.creds["Password"]


        logging.info("Now logging in to the system")

        logged_in.login(mobile_num, pass_word)
        time.sleep(10)

        product_search = Searchbar(self.driver)
        product_search.search("Sunscreen")
        time.sleep(2)

        cart_button =  Cart(self.driver)
        cart_button.cart()
        time.sleep(5)

        carticon = Cart(self.driver)
        carticon.cart_icon()
        # time.sleep(5)

      
        product_name = "Ethisun Sunscreen-100gm"
        if carticon.is_product_in_cart(product_name):
            logging.info(f"{product_name} is in the cart.")
        else:
            logging.info(f"{product_name} is not in the cart.")


        cart_increment = Cart(self.driver)
        cart_increment.cart_increment_update()

        logging.info("one more item added to the cart successfully")

        cart_decrement = Cart(self.driver)
        cart_decrement.cart_decrement_update()
        logging.info("one item removed from the cart successfully")

        totalprice = Cart(self.driver)
        totalprice.total_price()

        product_remove = Cart(self.driver)
        product_remove.remove_product_from_cart()








