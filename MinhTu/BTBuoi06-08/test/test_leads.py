def test_manage_client(logged_in_home, leads):
    #Login the home page
    logged_in_home.verify_login_success("admin_example")
    
    #Select Leads under the left menu
    logged_in_home.choose_left_menu("Leads")

    #Add new lead
    new_lead = leads.create_new_lead()
    
    #Verify lead has been added
    leads.verify_toast_message("Lead added.")

    # Verify the created lead detail as expected
    leads.verify_created_lead_details(new_lead)
    