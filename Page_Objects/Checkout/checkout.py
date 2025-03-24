import logging
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Page_Objects.Checkout.checkoutproperties import Checkout_Properties
from selenium.webdriver.support import expected_conditions as EC

class Checkout(Checkout_Properties):

    def __init__(self,driver):
        self.driver = driver
        self.wait =  WebDriverWait(self.driver, 10)

    def checkout(self):

        checkout_btn = self.checkout_button_input
        checkout_btn.click()

        add_address = self.select_address_click
        add_address.click()
        time.sleep(10)

        select_province = self.select_province_input
        select_province.click()
        select_province.send_keys("Bagmati Province")
        select_province.send_keys(Keys.ENTER)
        time.sleep(5)



        select_city=self.select_city_input
        select_city.click()
        select_city.send_keys("Banepa")
        select_city.send_keys(Keys.ENTER)
        time.sleep(5)

        select_area=self.select_area_input
        select_area.click()
        select_area.send_keys("28 Kilo")
        select_area.send_keys(Keys.ENTER)
        # time.sleep(10)


        select_address = self.select_address_input
        select_address.click()
        select_address.send_keys("Radhe Radhe")


        select_landmark = self.select_landmark_input
        select_landmark.click()
        select_landmark.send_keys("UIA School")

        add_address_btn = self.add_address_button
        add_address_btn.click()
        time.sleep(2)

        Product_name = self.driver.find_element(By.XPATH,'//p[@class=\'text-sm leading-snug\']')
        product_bought_text = Product_name.text
        logging.info(f" Product bought: {product_bought_text}")


        product_quantity = self.driver.find_element(By.XPATH,'//p[@class=\'text-xs font-light\']')
        product_quantity_text = product_quantity.text
        logging.info(f"Total {product_quantity_text}")
        time.sleep(5)
















