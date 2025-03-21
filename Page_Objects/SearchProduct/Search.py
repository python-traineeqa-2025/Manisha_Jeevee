import time

from selenium.webdriver.common.by import By

from Page_Objects.SearchProduct.Searchproperties import Search_Properties

class Searchbar(Search_Properties):

    def __init__(self , driver):
        self.driver = driver

    def search(self, product):

        try:
            overlay = self.driver.find_element(By.XPATH, '//div[@class="fixed top-0 left-0 w-full h-full z-1"]')
            if overlay.is_displayed():
                self.driver.execute_script("arguments[0].click();", overlay)
                time.sleep(1)
        except:
            pass

        search_bar = self.searchbar_input
        search_bar.click()
        search_bar.clear()
        search_bar.send_keys(product)
        time.sleep(2)

        if product.strip() == "":
            print("Empty search query")
            return

        autosuggestion_dropdown = self.autosuggestion_input

        for item in autosuggestion_dropdown:
            if item.text.strip() == "Ethisun sunscreen-100gm":
                item.click()
                break
        time.sleep(5)

        try:
            invalid_search_result = self.search_result
            invalid_search_text = invalid_search_result.text
            print(f"Search Result: {invalid_search_text}")
        except:
            print("")

