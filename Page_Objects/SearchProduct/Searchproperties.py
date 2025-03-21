from Page_Objects.SearchProduct.Searchlocators import Search_Locators

class Search_Properties(Search_Locators):

    @property
    def searchbar_input(self):
        return self.driver.find_element(*Search_Locators.SEARCHBAR)

    @property
    def autosuggestion_input(self):
        return self.driver.find_elements(*Search_Locators.AUTOSUGGESTION)

    @property
    def search_result(self):
        return self.driver.find_element(*Search_Locators.SEARCH_RESULT)