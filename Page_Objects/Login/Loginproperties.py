from Page_Objects.Login.Loginlocators import Login_Locators

class Login_Properties(Login_Locators):

    @property
    def create_account_input(self):
        return self.driver.find_element(*Login_Locators.CREATE_ACCOUNT)

    @property
    def login_input(self):
        return self.driver.find_element(*Login_Locators.LOGIN)

    @property
    def mobile_number_input(self):
        return self.driver.find_element(*Login_Locators.MOBILE_NUMBER)

    @property
    def password_input(self):
        return self.driver.find_element(*Login_Locators.PASSWORD)

    @property
    def login_btn_input(self):
        return self.driver.find_element(*Login_Locators.LOGIN_BTN)