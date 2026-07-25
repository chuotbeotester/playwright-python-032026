from utils.text_data import TextData
from utils.path_hepler import PathFile

data = PathFile.read_json_data("user_data/data_lead.json")
LASTNAME = TextData.create_text_data(data["LAST_NAME"])
EMAIL = f'{TextData.create_text_data(data["EMAIL_NAME"]).replace("-","")}@gmail.com'
file_path = PathFile.get_string_file_path("upload_files/image.jpg")

def test_create_lead(logged_in_lead):
    logged_in_lead.goto(data["URL"])
    logged_in_lead.add_lead(data["FIRST_NAME"], LASTNAME, data["GENDER"], data["CONTACT_NUMBER"], EMAIL, file_path)
    logged_in_lead.verify_lead(EMAIL, LASTNAME)