import time

from Page_Objects.Login.Loginproperties import Login_Properties
from selenium.webdriver import ActionChains

# from Testcases.Demotest import actions


class Login_page(Login_Properties):

    def __init__(self,driver):
        self.driver = driver



    def login(self,mobile_number,password):

        create_account = self.create_account_input

        login_dropdown = self.login_input

        actions = ActionChains(self.driver)

        actions.move_to_element(create_account).move_to_element(login_dropdown).click().perform()
        time.sleep(5)

        mobile_num = self.mobile_number_input
        mobile_num.click()
        mobile_num.send_keys(mobile_number)

        pwd = self.password_input
        pwd.click()
        pwd.send_keys(password)

        signin_button = self.login_btn_input
        signin_button.click()







