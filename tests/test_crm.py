import pytest
from pages.crm_page import CrmPage


class TestCrm:
    
    def test_create_opportunity(self, driver):
        """Test creating a new opportunity"""
        crm = CrmPage(driver)
        
        crm.navigate_to_crm()
        crm.click_create()
        crm.create_opportunity(
            title="Test Opportunity",
            customer_name="Test Customer",
            revenue="10000"
        )
        
        title = crm.get_opportunity_title()
        assert "Test Opportunity" in title
    
    def test_edit_opportunity(self, driver):
        """Test editing an opportunity"""
        crm = CrmPage(driver)
        
        crm.navigate_to_pipeline()
        crm.edit_opportunity(
            title="Updated Title",
            revenue="15000",
            probability="80"
        )
        
        total = crm.get_total_price()
        assert "15000" in total
    
    def test_create_and_search_customer(self, driver):
        """Test creating and searching for a customer"""
        crm = CrmPage(driver)
        
        crm.navigate_to_customers()
        crm.create_customer("ACME Corp")
        crm.search_customer("ACME Corp")
        
        assert crm.is_customer_present("ACME Corp")
