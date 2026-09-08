from dataclasses import dataclass

@dataclass
class Lead:
    firstname: str
    lastname: str
    gender: str
    contactnumber: str
    email: str
    image_path: str