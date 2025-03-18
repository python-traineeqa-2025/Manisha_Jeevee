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
        product_search.search()
        time.sleep(10)

