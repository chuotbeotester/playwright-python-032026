
def test_create_lead(logged_in_lead, lead):
    logged_in_lead.goto()
    logged_in_lead.add_lead(lead)
    logged_in_lead.verify_lead(lead)