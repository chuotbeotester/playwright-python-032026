from utils.path_hepler import PathFile
from utils.text_data import TextData
from utils.faker_helper import FakerHelper
from models.lead import Lead
import random

class LeadFactory:

    @staticmethod
    def create_leadfactory():
        data = PathFile.read_json_data("user_data/data_lead.json")
        return Lead(
            firstname = data["FIRST_NAME"],
            lastname = TextData.create_text_data(data["LAST_NAME"]),
            gender = random.choice(['Male', 'Female']),
            contactnumber = FakerHelper.contactnumber(),
            email = FakerHelper.email(),
            image_path = PathFile.get_string_file_path("upload_files/image.jpg")
        )