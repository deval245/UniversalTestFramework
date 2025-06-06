# drivers/browser_driver.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utils.config_loader import get_config

class BrowserDriver:
    def __init__(self):
        self.driver = None
        self.config = get_config()

    def get_driver(self):
        browser = self.config.get("browser", "chrome").lower()

        if browser == "chrome":
            options = ChromeOptions()
            options.add_argument("--start-maximized")
            self.driver = webdriver.Chrome(options=options)

        elif browser == "firefox":
            options = FirefoxOptions()
            options.add_argument("--start-maximized")
            self.driver = webdriver.Firefox(options=options)

        else:
            raise ValueError(f"Unsupported browser: {browser}")

        return self.driver


