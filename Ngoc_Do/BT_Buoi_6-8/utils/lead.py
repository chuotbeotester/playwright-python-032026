from dataclasses import dataclass
from utils.path_helper import PathFile
from utils.text_data import TextData


@dataclass
class Lead:
    """Bộ dữ liệu của một Lead phục vụ chức năng Leads."""

    first_name: str
    last_name: str
    contact_number: str
    email: str

    @staticmethod
    def create_text_data(input_file: str = "input_data/lead.json") -> "Lead":
        """Tạo dữ liệu Lead duy nhất từ file input, dùng TextData để sinh phần unique.

        Args:
            input_file (str): Đường dẫn (tương đối từ resources) tới file JSON dữ liệu Lead.

        Returns:
            Lead: Đối tượng Lead với first_name / email duy nhất, last_name / contact lấy từ file.
        """
        data = PathFile.read_json_data(input_file)
        email_name, _, email_domain = data["email"].partition("@")
        return Lead(
            first_name=TextData.create_text_data(data["first_name"]),
            last_name=data["last_name"],
            contact_number=str(data["contact"]),
            email=f'{TextData.create_text_data(email_name).replace("-", "")}@{email_domain}',
        )
