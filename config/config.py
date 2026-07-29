# config/config.py
import os

class Config:
    # Base URL
    BASE_URL = os.getenv("BASE_URL", "https://your-app-url.com")
    
    # Test credentials
    VALID_EMAIL = os.getenv("VALID_EMAIL", "test@example.com")
    VALID_PASSWORD = os.getenv("VALID_PASSWORD", "validPassword123")
    INVALID_EMAIL = os.getenv("INVALID_EMAIL", "invalid@example.com")
    INVALID_PASSWORD = os.getenv("INVALID_PASSWORD", "wrongPassword")
    
    # Timeouts
    DEFAULT_TIMEOUT = 10
    IMPLICIT_WAIT = 5
    
    # Browser configuration
    BROWSER = os.getenv("BROWSER", "chrome")
    HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"
