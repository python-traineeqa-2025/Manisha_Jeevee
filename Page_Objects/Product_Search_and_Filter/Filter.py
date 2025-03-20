import logging
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Page_Objects.Product_Search_and_Filter.Filterproperties import Filter_Properties

class Product_Filter(Filter_Properties):

    def __init__(self,driver):
        self.driver = driver


    def filter(self):

        search_bar = self.searbar_input
        search_bar.click()
        search_bar.send_keys("Lotion")
        search_bar.send_keys(Keys.ENTER)
        time.sleep(5)

        checkbox_category = self.driver.find_element(By.XPATH,'//input[@id=\'Skin\']')
        checkbox_category.click()
        time.sleep(3)

        checkbox_brand = self.driver.find_element(By.XPATH,'//input[@id=\'Mamaearth\']')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", checkbox_brand)
        checkbox_brand.click()
        time.sleep(3)

        image_click = self.driver.find_element(By.XPATH,'//img[@alt=\'MAMAEARTH UBTAN BODY LOTION- 400ML\']')
        image_click.click()
        time.sleep(3)

        product_name = self.driver.find_element(By.XPATH,'//h1[normalize-space()=\'Mamaearth Ubtan Body Lotion- 400ml\']')
        product_name_text = product_name.text
        logging.info(f"Product bought:  {product_name_text}")
        time.sleep(3)


    def reset_filter(self):
        search_bar = self.searbar_input
        search_bar.click()
        search_bar.send_keys("Blush")
        search_bar.send_keys(Keys.ENTER)
        time.sleep(5)

        checkbox_category = self.driver.find_element(By.XPATH, '//input[@id=\'Skin\']')
        checkbox_category.click()
        time.sleep(1)

        checkbox_brand = self.driver.find_element(By.XPATH, '//input[@id=\'Hair\']')
        checkbox_brand.click()
        time.sleep(1)

        reset_button = self.driver.find_element(By.XPATH,'//span[normalize-space()=\'Reset\']')
        reset_button.click()
        time.sleep(3)

        logging.info("Filter reset successfully")




