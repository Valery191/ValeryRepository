# tests/test_login_logout.py
import pytest
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from config.config import Config


class TestLoginLogout:
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Setup for each test"""
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.logout_page = LogoutPage(driver)
        self.driver.get(Config.BASE_URL)
        yield
        # Cleanup if needed
    
    # ===== LOGIN TESTS =====
    
    def test_successful_login(self, driver):
        """Test successful login with valid credentials"""
        # Perform login
        self.login_page.login(Config.VALID_EMAIL, Config.VALID_PASSWORD)
        
        # Verify login was successful
        assert "dashboard" in driver.current_url.lower()
        assert "Dashboard" in driver.title
    
    def test_login_with_invalid_credentials(self, driver):
        """Test login with invalid credentials"""
        self.login_page.login("invalid@email.com", "wrongpassword")
        
        # Verify error message appears
        assert self.login_page.is_error_displayed()
        error_text = self.login_page.get_error_message()
        assert "Invalid" in error_text or "error" in error_text.lower()
    
    def test_login_with_empty_fields(self, driver):
        """Test login with empty username and password"""
        self.login_page.login("", "")
        
        # Should show validation messages
        assert "required" in driver.page_source.lower() or self.login_page.is_error_displayed()
    
    def test_login_with_empty_password(self, driver):
        """Test login with empty password"""
        self.login_page.login("validuser@email.com", "")
        
        # Should show password required message
        assert "required" in driver.page_source.lower() or "password" in driver.page_source.lower()
    
    def test_login_page_title(self, driver):
        """Verify login page title"""
        expected_title = "Login | Best solution for startups"
        assert self.login_page.get_page_title() == expected_title
    
    def test_login_button_visible(self, driver):
        """Verify login button is visible"""
        assert self.login_page.is_login_button_visible()
    
    def test_remember_me_checkbox(self, driver):
        """Test remember me functionality"""
        # Check if remember me checkbox exists and is clickable
        # This depends on your specific implementation
        pass
    
    # ===== LOGOUT TESTS =====
    
    def test_successful_logout(self, driver):
        """Test successful logout"""
        # First login
        self.login_page.login(Config.VALID_EMAIL, Config.VALID_PASSWORD)
        
        # Then logout
        self.logout_page.click_user_menu()
        self.logout_page.click_logout()
        self.logout_page.wait_for_login_page()
        
        # Verify logout was successful
        expected_title = "Login | Best solution for startups"
        assert self.logout_page.is_logout_successful(expected_title)
        assert "login" in driver.current_url.lower()
    
    def test_logout_and_back_button(self, driver):
        """Test back button after logout (User cannot go back)"""
        # Login
        self.login_page.login(Config.VALID_EMAIL, Config.VALID_PASSWORD)
        
        # Logout
        self.logout_page.click_user_menu()
        self.logout_page.click_logout()
        self.logout_page.wait_for_login_page()
        
        # Try to go back
        driver.back()
        
        # Verify warning or login page is displayed
        assert self.logout_page.is_warning_message_displayed() or "login" in driver.current_url.lower()
    
    def test_logout_confirmation_dialog(self, driver):
        """Test logout with confirmation dialog"""
        # Login
        self.login_page.login(Config.VALID_EMAIL, Config.VALID_PASSWORD)
        
        # Click logout and confirm
        self.logout_page.click_user_menu()
        self.logout_page.click_logout()
        self.logout_page.confirm_logout_action()
        self.logout_page.wait_for_login_page()
        
        # Verify logout
        assert "login" in driver.current_url.lower()
    
    def test_user_cannot_access_dashboard_after_logout(self, driver):
        """Test user cannot access protected pages after logout"""
        # Login
        self.login_page.login(Config.VALID_EMAIL, Config.VALID_PASSWORD)
        
        # Logout
        self.logout_page.click_user_menu()
        self.logout_page.click_logout()
        self.logout_page.wait_for_login_page()
        
        # Try to access dashboard directly
        driver.get(Config.BASE_URL + "/dashboard")
        
        # Should redirect to login
        assert "login" in driver.current_url.lower()
    
    def test_multiple_login_logout_cycles(self, driver):
        """Test multiple login/logout cycles"""
        for i in range(3):
            # Login
            self.login_page.login(Config.VALID_EMAIL, Config.VALID_PASSWORD)
            assert "dashboard" in driver.current_url.lower()
            
            # Logout
            self.logout_page.click_user_menu()
            self.logout_page.click_logout()
            self.logout_page.wait_for_login_page()
            
            # Verify logout
            assert "login" in driver.current_url.lower()
    
    def test_logout_button_visibility(self, driver):
        """Test logout button is visible after login"""
        # Login
        self.login_page.login(Config.VALID_EMAIL, Config.VALID_PASSWORD)
        
        # Click user menu
        self.logout_page.click_user_menu()
        
        # Verify logout button is visible
        assert self.logout_page.wait_for_logout_button()
    
    def test_session_expiry_after_logout(self, driver):
        """Test session expires after logout"""
        # Login
        self.login_page.login(Config.VALID_EMAIL, Config.VALID_PASSWORD)
        
        # Get session cookie
        session_cookie = driver.get_cookie("sessionid")
        assert session_cookie is not None
        
        # Logout
        self.logout_page.click_user_menu()
        self.logout_page.click_logout()
        self.logout_page.wait_for_login_page()
        
        # Verify session cookie is cleared
        session_cookie_after = driver.get_cookie("sessionid")
        assert session_cookie_after is None
    
    def test_keyboard_navigation_logout(self, driver):
        """Test logout using keyboard navigation"""
        # Login
        self.login_page.login(Config.VALID_EMAIL, Config.VALID_PASSWORD)
        
        # Use keyboard shortcuts (implementation depends on your app)
        # This is a placeholder for more complex keyboard interactions
        pass
