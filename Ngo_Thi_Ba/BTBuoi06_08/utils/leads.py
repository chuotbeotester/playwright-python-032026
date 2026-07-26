from utils.path_helper import PathFile
from utils.text_data import TextData

def create_lead_data():
    """Tạo dữ liệu khách hàng tiềm năng từ file JSON.

    Returns:
        dict: Dữ liệu khách hàng.
    """
    return PathFile.read_json_data("input_data/leads.json")

