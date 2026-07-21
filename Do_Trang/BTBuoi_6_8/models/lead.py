from dataclasses import dataclass
from utils.path_helper import PathFile
from utils.text_data import TextData

@dataclass
class Lead:
    first_name: str
    last_name: str
    contact_number: str
    email: str
    gender: str
    profile_picture: str

    @staticmethod
    def create_data_lead(input_file: str = "input_data/leads.json"):
        """Tạo dữ liệu Lead từ file input

        Args:
            input_file (str): Đường dẫn (tương đối từ resources) tới file JSON dữ liệu Lead.

        Returns:
            Lead: Lead với email sinh duy nhất và các trường thông tin còn lại lấy từ Json.
        """
        data = PathFile.read_json_data(input_file)
        name_random = TextData.create_text_data("trang")
        lead = Lead(
            first_name=data["first_name"],
            last_name=data["last_name"],
            contact_number=data["contact_number"],
            email=f"{name_random}{data['email']}",
            gender=data["gender"],
            profile_picture=data["profile_picture"]
        )
        return lead