# drivers/db_connector.py

import sqlite3
from utils.logger import logger

class DBConnector:
    def __init__(self, config):
        self.db_path = config.get("db_path", "test.db")
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

    def execute(self, query):
        logger.info(f"Executing query: {query}")
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()

