def test_manage_client(logged_in_home, manage_client):
    #Login the home page
    logged_in_home.verify_login_success("admin_example")
    
    #Select Manage Clients under the left menu
    logged_in_home.choose_left_menu("Manage Clients")
    
    #Add new client
    new_client = manage_client.create_new_client()
    
    #Verify client has been added
    manage_client.verify_toast_message("Client added.")

    # Verify the created client detail as expected
    manage_client.verify_created_client_details(new_client)
    