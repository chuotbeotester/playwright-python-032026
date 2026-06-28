from dataclasses import dataclass
from utils.path_helper import PathFile
from utils.text_data import TextData


@dataclass
class Client:
    """Bộ dữ liệu của một Client phục vụ chức năng Manage Clients."""

    first_name: str
    last_name: str
    contact_number: str
    email: str
    username: str
    password: str

    @staticmethod
    def create_text_data(input_file: str = "input_data/client.json") -> "Client":
        """Tạo dữ liệu Client duy nhất từ file input, dùng TextData để sinh phần unique.

        Args:
            input_file (str): Đường dẫn (tương đối từ resources) tới file JSON dữ liệu Client.

        Returns:
            Client: Đối tượng Client với first_name / email / username duy nhất; các trường còn lại
                lấy từ file.
        """
        data = PathFile.read_json_data(input_file)
        email_name, _, email_domain = data["email"].partition("@")
        return Client(
            first_name=TextData.create_text_data(data["first_name"]),
            last_name=data["last_name"],
            contact_number=str(data["contact"]),
            email=f'{TextData.create_text_data(email_name).replace("-", "")}@{email_domain}',
            username=TextData.create_text_data(data["username"]).replace("-", ""),
            password=str(data["password"]),
        )
