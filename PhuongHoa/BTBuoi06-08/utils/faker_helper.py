from faker import Faker

fake = Faker('vi_VN')

class FakerHelper:

    @staticmethod
    def email():
        return fake.unique.email()

    @staticmethod
    def contactnumber():
        return fake.numerify("09########")