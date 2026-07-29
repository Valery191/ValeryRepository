# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Page Object for Login functionality"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self._init_elements()
    
    def _init_elements(self):
        """Initialize all web elements"""
        # Login form elements
        self.email_input = (By.ID, "login")  # Adjust selector as needed
        self.password_input = (By.ID, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")
        
        # Error messages
        self.error_message = (By.CLASS_NAME, "alert-danger")
        self.warning_message = (By.CLASS_NAME, "warning")
        
        # Remember me checkbox
        self.remember_me = (By.ID, "remember-me")
        
        # Forgot password link
        self.forgot_password = (By.LINK_TEXT, "Forgot Password?")
    
    def login(self, email, password):
        """
        Perform login action
        
        Args:
            email: User email or username
            password: User password
        
        Returns:
            self for method chaining
        """
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        return self
    
    def get_error_message(self):
        """Get error message text"""
        try:
            return self.driver.find_element(*self.error_message).text
        except:
            return None
    
    def is_error_displayed(self):
        """Check if error message is displayed"""
        try:
            return self.driver.find_element(*self.error_message).is_displayed()
        except:
            return False
    
    def wait_for_login_page(self):
        """Wait for login page to load"""
        self.wait.until(EC.visibility_of_element_located(self.login_button))
        return self
    
    def get_page_title(self):
        """Get current page title"""
        return self.driver.title
    
    def is_login_button_visible(self):
        """Check if login button is visible"""
        try:
            return self.driver.find_element(*self.login_button).is_displayed()
        except:
            return False
