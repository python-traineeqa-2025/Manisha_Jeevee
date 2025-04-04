from Page_Objects.Navbar.NavbarLocators import Navbar_Locators

class Navbar_Properties(Navbar_Locators):

    @property
    def skin_hover(self):
        return self.driver.find_element(Navbar_Locators.SKIN)

    @property
    def cleansers_link(self):
        return self.driver.find_element(Navbar_Locators.CLEANSERS)