from faker import Faker
import random

fake = Faker()

class FakeData:
    first_name = fake.first_name()
    last_name = fake.last_name()
    contact_number = "09" + "".join(str(random.randint(0, 9)) for _ in range(8))
    gender = random.choice(["Male", "Female"])
    email = fake.unique.email()
    username = fake.unique.user_name()
    password = fake.password(length=8)
    
    @staticmethod
    def create_client():
        return {
            "first_name": FakeData.first_name,
            "last_name": FakeData.last_name,
            "pwd": FakeData.password,
            "contact_number": FakeData.contact_number,
            "gender": FakeData.gender,
            "email": FakeData.email,
            "usr": FakeData.username
        }
        
    def create_lead():
        return {
            "first_name": FakeData.first_name,
            "last_name": FakeData.last_name,
            "contact_number": FakeData.contact_number,
            "gender": FakeData.gender,
            "email": FakeData.email
        }