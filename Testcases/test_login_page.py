import logging
import time

from Setup.Basetest import BaseTest


from Page_Objects.Login.Loginpage import Login_page

class Test_login(BaseTest):

    def test_login(self):

        url = self.creds["BaseUrl"]
        self.driver.get(url)
        logging.info("Opened Site:")

        login_in = Login_page(self.driver)

        logging.info("Got the credentials")

        mobile_num = self.creds["Mobile_Number"]
        pass_word = self.creds["Password"]

        logging.info("Now logging in to the system")

        login_in.login(mobile_num,pass_word)


        logging.info("Logged In Successfully")

        time.sleep(10)










