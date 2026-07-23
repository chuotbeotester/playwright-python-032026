import json

def test_print_local_storage(logged_in_home):
#    local_data = logged_in_home.page.evaluate("() => Object.entries(localStorage)")
#    print(local_data)
    logged_in_home.page.context.storage_state(
        path = "tests/storage_stage.json"
    )
   