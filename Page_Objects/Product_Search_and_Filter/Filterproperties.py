from Page_Objects.Product_Search_and_Filter.Filterlocators import Filter_Locators

class Filter_Properties(Filter_Locators):

    @property
    def searbar_input(self):
        return self.driver.find_element(*Filter_Locators.SEARCHBAR)