import pytest
from utils.path_helper import PathFile
import time


def test_add_new_lead(logged_in_lead, get_lead_infor, get_avatar_path):
    logged_in_lead.go_to_lead_page()
    logged_in_lead.add_a_new_lead(
        get_lead_infor["firsname"],
        get_lead_infor["lastname"],
        get_lead_infor["gender"],
        get_lead_infor["contactNumer"],
        get_lead_infor["email"],
        str(get_avatar_path)
    )

    logged_in_lead.verify_added_lead(
        get_lead_infor["email"],
        get_lead_infor["firsname"],
        get_lead_infor["lastname"],
        get_lead_infor["contactNumer"],
        get_lead_infor["gender"],
        )
    
time.sleep(5)