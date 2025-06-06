# tests/ui/test_login.py

from core.base_test import BaseTest

class TestLogin(BaseTest):
    def test_example(self):
        self.driver.get(self.config["base_url"])
        assert "Example" in self.driver.title

