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
        time.sleep(5)

        select_province = self.select_province_input
        select_province.click()
        select_province.send_keys("Bagmati Province")
        time.sleep(1)
        select_province.send_keys(Keys.ENTER)
        time.sleep(5)


        select_city = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.ID,'react-select-cities-placeholder'))

        )
        # select_city.click()
        select_city.send_keys("Banepa")
        select_province.send_keys(Keys.ENTER)
        time.sleep(5)


        # time.sleep(2)
        # city_dropdown = self.select_city_input
        # self.driver.execute_script("arguments[0].value = 'Banepa';", city_dropdown)



