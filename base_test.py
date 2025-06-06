# core/base_test.py

from utils.logger import logger
from utils.config_loader import get_config
from drivers.browser_driver import BrowserDriver
from drivers.api_client import APIClient
from drivers.db_connector import DBConnector

class BaseTest:
    """
    Base class for all UI/API/DB tests.
    Injects config, logger, driver, and handles test lifecycle events.
    """

    def setup_method(self, method):
        self.test_name = method.__name__
        logger.info(f"🧪 Starting test: {self.test_name}")

        self.config = get_config()
        self.driver = BrowserDriver().get_driver()
        self.api = APIClient(self.config)
        self.db = DBConnector(self.config)

    def teardown_method(self, method):
        logger.info(f"✅ Finishing test: {self.test_name}")
        if self.driver:
            self.driver.quit()

