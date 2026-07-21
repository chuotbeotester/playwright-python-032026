from dataclasses import dataclass
from utils.path_helper import PathFile
from utils.text_data import TextData

@dataclass
class Client:
    first_name: str
    last_name: str
    password: str
    contact_number: str
    email: str
    username: str
    gender: str
    profile_picture: str

    @staticmethod
    def create_data_manage_lient(input_file: str = "input_data/client.json") -> "Client":
        """Tạo dữ liệu Client duy nhất từ file input, dùng TextData để sinh phần unique.

        Args:
            input_file (str): Đường dẫn (tương đối từ resources) tới file JSON dữ liệu Client.

        Returns:
            Client: Client với email / username duy nhất và các trường thông tin còn lại lấy từ Json.
        """
        data = PathFile.read_json_data(input_file)
        name_random = TextData.create_text_data("trang")
        client = Client(
            first_name=data["first_name"],
            last_name=data["last_name"],
            password=data["password"],
            contact_number=data["contact_number"],
            email=f"{name_random}{data['email']}",
            username=f"{data['username']}{name_random}",
            gender=data["gender"],
            profile_picture=data["profile_picture"]
        )
        return client