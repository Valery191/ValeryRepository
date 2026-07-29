# pages/logout_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogoutPage:
    """Page Object for Logout functionality"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self._init_elements()
    
    def _init_elements(self):
        """Initialize all web elements"""
        # User menu/avatar
        self.popup_button = (By.XPATH, "//button[@class='user-menu']")
        self.user_avatar = (By.CLASS_NAME, "avatar")
        self.user_menu = (By.CLASS_NAME, "dropdown-menu")
        
        # Logout options
        self.logout_button = (By.XPATH, "//a[contains(text(), 'Log out')]")
        self.logout_option = (By.LINK_TEXT, "Logout")
        self.sign_out_button = (By.XPATH, "//button[contains(text(), 'Sign Out')]")
        
        # Confirmation dialogs
        self.confirm_logout = (By.XPATH, "//button[@class='confirm']")
        self.warning_message = (By.CLASS_NAME, "warning-message")
        self.error_message = (By.CLASS_NAME, "error")
        
        # Login dashboard elements
        self.login_dashboard_title = (By.XPATH, "//h1[contains(text(), 'Login')]")
        self.dashboard_logo = (By.CLASS_NAME, "logo")
    
    def click_user_menu(self):
        """Click on user menu/avatar"""
        self.wait.until(EC.element_to_be_clickable(self.popup_button)).click()
        return self
    
    def click_logout(self):
        """Click logout button from dropdown"""
        self.wait.until(EC.element_to_be_clickable(self.logout_button)).click()
        return self
    
    def confirm_logout_action(self):
        """Confirm logout if confirmation dialog appears"""
        try:
            self.wait.until(EC.element_to_be_clickable(self.confirm_logout)).click()
        except:
            pass  # No confirmation dialog needed
        return self
    
    def wait_for_login_page(self):
        """Wait for login page after logout"""
        self.wait.until(EC.visibility_of_element_located(self.login_dashboard_title))
        return self
    
    def wait_for_logout_button(self):
        """Wait for logout button to be visible"""
        self.wait.until(EC.visibility_of_element_located(self.logout_button))
        return self
    
    def is_warning_message_displayed(self):
        """Check if warning message is displayed"""
        try:
            return self.driver.find_element(*self.warning_message).is_displayed()
        except:
            return False
    
    def get_warning_message_text(self):
        """Get warning message text"""
        try:
            return self.driver.find_element(*self.warning_message).text
        except:
            return None
    
    def is_logout_successful(self, expected_title):
        """
        Verify logout was successful
        
        Args:
            expected_title: Expected page title after logout
        
        Returns:
            bool: True if logout successful
        """
        return self.driver.title == expected_title
