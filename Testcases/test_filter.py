import logging
import time

from Setup.Basetest import BaseTest
from Page_Objects.Product_Search_and_Filter.Filter import Product_Filter



class Test_filter(BaseTest):

    def test_filter(self):

        url = self.creds["BaseUrl"]
        self.driver.get(url)
        logging.info("Jeevee Site Opened:")

        filter_page = Product_Filter(self.driver)
        filter_page.filter()
        time.sleep(5)

        reset_filter_page = Product_Filter(self.driver)
        reset_filter_page.reset_filter()


