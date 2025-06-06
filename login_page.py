# modules/ui/pages/login_page.py

from locators.locator_strategy import LocatorStrategy
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = LocatorStrategy("modules/ui/locators/login_locators.yaml")

    def login(self, username, password):
        ctx = {
            "username_field": "email",
            "login_text": "Login"
        }

        # Username input
        type_u, value_u = self.locators.get("login_page", "username_input", ctx)
        by_u = By.XPATH if type_u == "xpath" else By.CSS_SELECTOR
        self.driver.find_element(by_u, value_u).send_keys(username)

        # Password input
        type_p, value_p = self.locators.get("login_page", "password_input", ctx)
        by_p = By.XPATH if type_p == "xpath" else By.CSS_SELECTOR
        self.driver.find_element(by_p, value_p).send_keys(password)

        # Click login button
        type_l, value_l = self.locators.get("login_page", "login_button", ctx)
        by_l = By.XPATH if type_l == "xpath" else By.CSS_SELECTOR
        self.driver.find_element(by_l, value_l).click()

