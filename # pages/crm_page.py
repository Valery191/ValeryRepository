# pages/crm_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CrmPage:
    """Page Object for the CRM module"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self._init_elements()
    
    def _init_elements(self):
        """Initialize all web elements"""
        # Main navigation
        self.crm_link = (By.PARTIAL_LINK_TEXT, "CRM")
        self.pipeline_side_button = (By.XPATH, "//a[@href='/web#menu_id=274&action=365']/span")
        self.customer_side_button = (By.XPATH, "//a[@href='/web#menu_id=272&action=48']")
        
        # Action buttons
        self.create_button = (By.XPATH, "//button[@accesskey='c']")
        self.edit_button = (By.XPATH, "//button[@accesskey='a']")
        self.save_edit = (By.XPATH, "//button[@accesskey='s']")
        self.create_pipeline = (By.XPATH, "//button[@name='close_dialog']")
        
        # Form fields
        self.opportunity_title = (By.NAME, "name")
        self.customer = (By.XPATH, "//table[@class='o_group o_inner_group o_group_col_6']//div//div//input")
        self.customer_id = (By.XPATH, "//a[.='&CC']")
        self.expected_revenue = (By.XPATH, "//div[@class='o_row']//input")
        self.priority = (By.XPATH, "//table[@class='o_group o_inner_group o_group_col_6']//tr[4]//a[3]")
        
        # Edit fields
        self.opportunity_title_edit = (By.XPATH, "//input[@name='name']")
        self.expected_revenue_edit = (By.XPATH, "//input[@id='o_field_input_125']")
        self.probability_edit = (By.XPATH, "//input[@id='o_field_input_127']")
        
        # Verification elements
        self.find_title_test = (By.XPATH, "//div[@data-id='1']/div[2]//strong//span")
        self.total_price = (By.XPATH, "//div[@data-id='1']//b")
        self.button_pipeline = (By.XPATH, "//div[@data-id='1']/div[2]")
        self.progress_pipeline = (By.XPATH, "//div[@data-id='1']/div[2]")
        self.progress_pipeline_2 = (By.XPATH, "//div[@data-id='2']/div[2]")
        self.test_verify = (By.XPATH, "//div[@data-id='2']//div[2]//strong//span")
        
        # Customer management
        self.create_customer = (By.XPATH, "//button[@accesskey='c']")
        self.input_name = (By.NAME, "name")
        self.create_customer_button = (By.XPATH, "//button[@name='close_dialog']")
        self.searching_text = (By.XPATH, "//input[@class='o_searchview_input']")
        self.name_customer = (By.XPATH, "//span[.='&CC']")
        
        # Print functionality
        self.due_payment_button = (By.XPATH, "//a[@data-section='print']")
        self.print_button = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[1]/button")
    
    # === Navigation Methods ===
    def navigate_to_crm(self):
        """Navigate to the CRM module"""
        self.driver.find_element(*self.crm_link).click()
        return self
    
    def navigate_to_pipeline(self):
        """Navigate to the Pipeline view"""
        self.driver.find_element(*self.pipeline_side_button).click()
        return self
    
    def navigate_to_customers(self):
        """Navigate to the Customers section"""
        self.driver.find_element(*self.customer_side_button).click()
        return self
    
    # === Creation Methods ===
    def click_create(self):
        """Click the Create button"""
        self.driver.find_element(*self.create_button).click()
        return self
    
    def create_opportunity(self, title, customer_name, revenue, priority=None):
        """
        Create a new opportunity
        
        Args:
            title: Opportunity title
            customer_name: Customer name
            revenue: Expected revenue
            priority: Priority level (optional)
        """
        self.driver.find_element(*self.opportunity_title).send_keys(title)
        self.driver.find_element(*self.customer).send_keys(customer_name)
        self.driver.find_element(*self.expected_revenue).send_keys(revenue)
        
        if priority:
            self.driver.find_element(*self.priority).click()
            # TODO: Select priority from dropdown
            
        self.driver.find_element(*self.create_pipeline).click()
        return self
    
    def create_customer(self, name):
        """
        Create a new customer
        
        Args:
            name: Customer name
        """
        self.driver.find_element(*self.create_customer).click()
        self.driver.find_element(*self.input_name).send_keys(name)
        self.driver.find_element(*self.create_customer_button).click()
        return self
    
    # === Edit Methods ===
    def edit_opportunity(self, title=None, revenue=None, probability=None):
        """
        Edit an existing opportunity
        
        Args:
            title: New title (optional)
            revenue: New expected revenue (optional)
            probability: New probability percentage (optional)
        """
        self.driver.find_element(*self.edit_button).click()
        
        if title:
            title_field = self.driver.find_element(*self.opportunity_title_edit)
            title_field.clear()
            title_field.send_keys(title)
            
        if revenue:
            revenue_field = self.driver.find_element(*self.expected_revenue_edit)
            revenue_field.clear()
            revenue_field.send_keys(revenue)
            
        if probability:
            prob_field = self.driver.find_element(*self.probability_edit)
            prob_field.clear()
            prob_field.send_keys(probability)
            
        self.driver.find_element(*self.save_edit).click()
        return self
    
    # === Search and Verification Methods ===
    def search_customer(self, name):
        """Search for a customer by name"""
        search_field = self.driver.find_element(*self.searching_text)
        search_field.clear()
        search_field.send_keys(name)
        search_field.submit()
        return self
    
    def get_opportunity_title(self):
        """Get the opportunity title from the first card"""
        return self.driver.find_element(*self.find_title_test).text
    
    def get_total_price(self):
        """Get the total price from the first card"""
        return self.driver.find_element(*self.total_price).text
    
    def get_opportunity_title_second(self):
        """Get the opportunity title from the second card"""
        return self.driver.find_element(*self.test_verify).text
    
    def is_customer_present(self, name):
        """Check if a customer is present"""
        try:
            element = self.driver.find_element(By.XPATH, f"//span[.='{name}']")
            return element.is_displayed()
        except:
            return False
    
    # === Print Methods ===
    def click_print_due_payment(self):
        """Click the print due payment button"""
        self.driver.find_element(*self.due_payment_button).click()
        return self
    
    def click_print(self):
        """Click the print button"""
        self.driver.find_element(*self.print_button).click()
        return self
    
    # === Helper Methods ===
    def wait_for_element(self, locator, timeout=10):
        """Wait for an element to appear"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    
    def wait_for_clickable(self, locator, timeout=10):
        """Wait for an element to be clickable"""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
