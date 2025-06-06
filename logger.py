# utils/logger.py

from loguru import logger
import os
from datetime import datetime

# Create logs directory if not exists
LOG_DIR = "reports/logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Timestamped log file
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
LOG_PATH = os.path.join(LOG_DIR, f"test_log_{timestamp}.log")

# Configure loguru
logger.remove()
logger.add(
    LOG_PATH,
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
    level="INFO",
    rotation="1 MB",
    compression="zip"
)

logger.info(f"📂 Log initialized at {LOG_PATH}")

