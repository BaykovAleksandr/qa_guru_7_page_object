
from pages.registration_page import RegistrationPage


def test_positive(open_browser):
    registration_page = RegistrationPage()

    registration_page.open()

    registration_page.fill_first_name('Aleksandr')

    registration_page.fill_second_name('Baykov')

    registration_page.fill_email('test@yandex.com')

    registration_page.choose_gender()

    registration_page.fill_phone_number('1234567890')

    registration_page.choose_birthday()

    registration_page.fill_interests('Maths')

    registration_page.choose_hobbies()

    registration_page.upload_file('san-diego-night-view-united-states-boats.jpeg')

    registration_page.fill_current_address("Moscow Region")

    registration_page.choose_state('ncr')

    registration_page.choose_city('Delhi')

    registration_page.click_submit()

    registration_page.assert_title('Thanks for submitting the form')

    registration_page.assert_body(
        'Aleksandr Baykov',
        'test@yandex.com',
        'Male',
        '1234567890',
        '19 December,1988',
        'Maths',
        'Music',
        'san-diego-night-view-united-states-boats.jpeg',
        'Moscow Region',
        'NCR Delhi')



