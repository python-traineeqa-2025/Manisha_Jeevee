import logging
import time

from Setup.Basetest import BaseTest
from Page_Objects.SearchProduct.Search import Searchbar

class Test_search(BaseTest):

    def test_search(self):

        url = self.creds["BaseUrl"]
        self.driver.get(url)
        logging.info("Opened Site:")

        product_search = Searchbar(self.driver)
        product_search.search("Sunscreen, SUNSCREEN")
        logging.info("Search result for the Sunscreen")
        time.sleep(2)

        product_invalid_search = Searchbar(self.driver)
        product_invalid_search.search("hdasdgasda")
        self.driver.back()
        # self.driver.back()

        empty_search = Searchbar(self.driver)
        empty_search.search(" ")

