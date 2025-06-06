# drivers/api_client.py

import requests
from utils.logger import logger

class APIClient:
    def __init__(self, config):
        self.base_url = config.get("base_url", "")
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json"
        })

    def get(self, endpoint, params=None, retries=3):
        url = f"{self.base_url}{endpoint}"
        for attempt in range(retries):
            try:
                logger.info(f"GET Request: {url}")
                response = self.session.get(url, params=params)
                response.raise_for_status()
                return response
            except requests.exceptions.RequestException as e:
                logger.warning(f"GET attempt {attempt+1} failed: {e}")
                if attempt == retries - 1:
                    raise

