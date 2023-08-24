from data.user import User
from pages.registration_page import RegistrationPage


def test_positive(open_browser):
    registration_page = RegistrationPage()
    alex = User(
        first_name='Aleksandr',
        last_name='Baykov',
        email='test@yandex.com',
        gender='Male',
        phone_number='1234567890',
        date_of_birth='19 December,1988',
        subject='Maths',
        hobby='Music',
        picture='san-diego-night-view-united-states-boats.jpeg',
        address='Moscow Region',
        state='NCR',
        city='Delhi'
    )

    registration_page.open()
    registration_page.register(alex)
    registration_page.should_have_registered(alex)



