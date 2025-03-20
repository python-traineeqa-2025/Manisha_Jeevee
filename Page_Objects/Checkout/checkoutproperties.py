from Page_Objects.Checkout.checkoutlocators import Checkout_Locators

class Checkout_Properties(Checkout_Locators):

    @property
    def checkout_button_input(self):
        return self.driver.find_element(*Checkout_Locators.CHECKOUT_BUTTON)

    @property
    def select_address_click(self):
        return self.driver.find_element(*Checkout_Locators.ADD_ADDRESS)

    @property
    def select_province_input(self):
        return self.driver.find_element(*Checkout_Locators.SELECT_PROVINCE)

    @property
    def province_dropdown_input(self):
        return self.driver.find_element(*Checkout_Locators.PROVINCE_DROPDOWN)

    @property
    def select_city_input(self):
        return self.driver.find_element(*Checkout_Locators.SELECT_CITY)

    @property
    def select_area_input(self):
        return self.driver.find_element(*Checkout_Locators.SELECT_AREA)

    @property
    def select_address_input(self):
        return self.driver.find_element(*Checkout_Locators.SELECT_ADDRESS)

    @property
    def select_landmark_input(self):
        return self.driver.find_element(*Checkout_Locators.SELECT_LANDMARK)

    @property
    def select_number_input(self):
        return self.driver.find_element(*Checkout_Locators.SELECT_NUMBER)

    @property
    def add_address_button(self):
        return self.driver.find_element(*Checkout_Locators.ADD_ADDRESS_BUTTON)