import pytest
from utils.lead import Lead


NEW_LEAD = Lead.create_text_data()


def test_add_new_lead(logged_in_manage_leads):
    logged_in_manage_leads.go_to_manage_leads_page()
    logged_in_manage_leads.create_lead(NEW_LEAD)
    logged_in_manage_leads.verify_create_success(NEW_LEAD)
