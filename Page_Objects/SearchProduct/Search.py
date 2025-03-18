import time

from Page_Objects.SearchProduct.Searchproperties import Search_Properties

class Searchbar(Search_Properties):

    def __init__(self , driver):
        self.driver = driver


    def search(self):

        search_bar = self.searchbar_input
        search_bar.click()
        search_bar.send_keys("Sunscreen")
        time.sleep(2)

        autosuggestion_dropdown = self.autosuggestion_input

        for item in autosuggestion_dropdown:
            # print(item.text)
            if item.text.strip() == "Ethisun sunscreen-100gm":
                item.click()
                break
        time.sleep(5)