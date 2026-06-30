import json
import os


class PathFile:
    _BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    _RESOURCES_DIR = os.path.join(_BASE_DIR, "resources")

    @classmethod
    def get_string_file_path(cls, relative_path: str) -> str:
        """Trả về đường dẫn tuyệt đối từ đường dẫn tương đối trong resources/."""
        return os.path.join(cls._RESOURCES_DIR, relative_path)

    @classmethod
    def read_json_data(cls, relative_path: str) -> dict:
        """Đọc và parse file JSON từ đường dẫn tương đối trong resources/."""
        file_path = cls.get_string_file_path(relative_path)
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
