import logging
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from Setup.Basetest import BaseTest
from Page_Objects.Login.Loginpage import Login_page



class Test_Multiple(BaseTest):

   def test_multiple(self):

       url = self.creds['BaseUrl']
       self.driver.get(url)
       logging.info("JEEVEE Site opened")

       list_creds = self.creds['users']

       invalid_test = Login_page(self.driver)

       for mn,pw in list_creds.items():

           invalid_test.login(mn,pw)
           time.sleep(10)
           self.driver.refresh()

       # try:
       #     result = self.driver.find_element(By.XPATH, '//div[@class=\'flex flex-1 items-center\']/span/following-sibling::text()')
       #     logging.info(f"{result.text}")
       # except NoSuchElementException:
       #     logging.error(f"Element not found for user {mn}"

#

