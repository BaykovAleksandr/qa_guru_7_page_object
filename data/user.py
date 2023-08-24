import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    date_of_birth: str
    subject: str
    hobby: str
    picture: str
    address: str
    state: str
    city: str
