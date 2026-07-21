from utils.path_helper import PathFile
from utils.text_data import TextData

def create_client_data():
    """Tạo dữ liệu khách hàng từ file JSON.

    Returns:
        dict: Dữ liệu khách hàng.
    """
    return PathFile.read_json_data("input_data/manage_client.json")
    
