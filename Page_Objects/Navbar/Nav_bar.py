import time

from selenium.webdriver import ActionChains

from Page_Objects.Navbar.Navbarproperties import Navbar_Properties

class navbar(Navbar_Properties):

    def __init__(self, driver):
        self.driver = driver


    def nav_bar(self):

        skin = self.skin_hover

        cleanser = self.cleansers_link

        actions = ActionChains(self.driver)

        actions.move_to_element(skin).perform()
        time.sleep(3)

