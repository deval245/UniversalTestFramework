# locators/smart_locator.py

import re
from typing import Dict

class SmartLocator:
    """
    Resolves locators dynamically based on provided context.
    Useful for dynamic UI automation in FAANG-scale applications.
    """

    @staticmethod
    def resolve(locator_template: str, context: Dict[str, str]) -> str:
        """
        Replace placeholders like {username} in a locator template with actual values from context.

        Args:
            locator_template (str): The locator with placeholders, e.g., "//div[text()='{username}']"
            context (Dict[str, str]): The key-value map to substitute in the template

        Returns:
            str: Fully resolved locator string
        """
        resolved = locator_template
        for key, value in context.items():
            pattern = r"\{" + re.escape(key) + r"\}"
            resolved = re.sub(pattern, str(value), resolved)

        if "{" in resolved or "}" in resolved:
            raise ValueError(f"Unresolved placeholders in locator: {resolved}")

        return resolved

