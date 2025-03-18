from Page_Objects.Cart.CartLocators import Cart_locators

class Cart_Properties(Cart_locators):

    @property
    def add_to_cart_button_input(self):
        return self.driver.find_element(*Cart_locators.ADD_CART_BUTTON)