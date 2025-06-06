# locators/locator_strategy.py

import yaml
from locators.smart_locator import SmartLocator
from utils.logger import logger

class LocatorStrategy:
    def __init__(self, locator_file_path):
        self.locators = self._load_locator_file(locator_file_path)

    def _load_locator_file(self, path):
        try:
            with open(path, "r") as f:
                return yaml.safe_load(f)
        except Exception as e:
            logger.error(f"❌ Failed to load locators: {e}")
            raise

    def get(self, page, element, context={}):
        try:
            locator_data = self.locators[page][element]
            locator_type = locator_data.get("type")
            template = locator_data.get("value")
            resolved = SmartLocator.resolve(template, context)

            logger.info(f"📍 Resolved {page}.{element} as [{locator_type}] {resolved}")
            return locator_type, resolved

        except Exception as e:
            logger.error(f"❌ Locator resolution failed for {page}.{element}: {e}")
            raise


