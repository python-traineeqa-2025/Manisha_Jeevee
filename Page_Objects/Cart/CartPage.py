from Page_Objects.Cart.CartProperties import Cart_Properties

class Cart(Cart_Properties):

    def __init__(self,driver):

        self.driver = driver

    def cart(self):

        cart_btn = self.add_to_cart_button_input
        cart_btn.click()
