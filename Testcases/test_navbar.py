import logging
import time

from Setup.Basetest import BaseTest

from Page_Objects.Navbar.Nav_bar import navbar

class Testlog(BaseTest):

    def test_navbar(self):

        url = self.creds["BaseUrl"]
        self.driver.get(url)
        logging.info("Opened Site:")
        time.sleep(5)

        # NavBar = navbar(self.driver)
        #
        # NavBar.nav_bar()