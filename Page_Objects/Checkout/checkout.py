import time

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
        time.sleep(5)

        # select_province = self.select_province_input
        # select_province.click()
        # province_dropdown = self.province_dropdown_input
        # self.driver.execute_script("arguments[0].value = 'Bagmati Province';", province_dropdown)
        # # select_province.send_keys("Bagmati Province")
        # time.sleep(5)

        select_city = self.select_city_input
        select_city.click()
        # time.sleep(2)
        # city_dropdown = self.select_city_input
        # self.driver.execute_script("arguments[0].value = 'Banepa';", city_dropdown)



