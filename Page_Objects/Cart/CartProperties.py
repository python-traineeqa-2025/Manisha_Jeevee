from Page_Objects.Cart.CartLocators import Cart_locators

class Cart_Properties(Cart_locators):

    @property
    def add_to_cart_button_input(self):
        return self.driver.find_element(*Cart_locators.ADD_CART_BUTTON)

    @property
    def carticon_input(self):
        return self.driver.find_element(*Cart_locators.CART_ICON)

    @property
    def cart_increment_icon(self):
        return self.driver.find_element(*Cart_locators.CART_INCREMENT)

    @property
    def cart_decrement_icon(self):
        return self.driver.find_element(*Cart_locators.CART_DECREMENT)

    @property
    def total_price_input(self):
        return self.driver.find_element(*Cart_locators.TOTAL_PRICE)