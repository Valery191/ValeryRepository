import os
import re
from datetime import datetime

from config.config import Config


def take_screenshot(driver, name: str) -> str:
    os.makedirs(Config.SCREENSHOT_DIR, exist_ok=True)
    safe_name = re.sub(r"[^A-Za-z0-9_\-]+", "_", name)[:80]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(Config.SCREENSHOT_DIR, f"{safe_name}_{timestamp}.png")
    driver.save_screenshot(path)
    return path
