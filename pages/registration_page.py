from selene import browser, be, have
from selene.support.shared.jquery_style import s
from data.user import User
from utils import files


class RegistrationPage:
    def register(self, user: User):
        self.set_first_name(user.first_name)
        self.set_last_name(user.last_name)
        self.set_email(user.email)
        self.set_gender()
        self.set_phone_number(user.phone_number)
        self.set_date_of_birth()
        self.set_subject(user.subject)
        self.set_hobby()
        self.set_picture(user.picture)
        self.set_address(user.address)
        self.set_state(user.state)
        self.set_city(user.city)
        self.click_submit()

    def open(self):
        browser.open('/automation-practice-form')

    def set_first_name(self, first_name):
        browser.element('#firstName').should(be.blank).type(first_name)
        return self

    def set_last_name(self, last_name):
        browser.element('#lastName').should(be.blank).type(last_name)
        return self

    def set_email(self, email):
        browser.element('#userEmail').should(be.blank).type(email)
        return self

    def set_gender(self):
        browser.element('[for="gender-radio-1"]').click()
        return self

    def set_phone_number(self, number):
        browser.element('#userNumber').should(be.blank).type(number)
        return self

    def set_date_of_birth(self):
        browser.element('#dateOfBirthInput').click()
        browser.element(".react-datepicker__month-select>option[value='11']").click()
        browser.element(".react-datepicker__year-select>option[value='1988']").click()
        browser.element('.react-datepicker__day--019').click()
        return self

    def set_subject(self, subject):
        browser.element('#subjectsInput').should(be.blank).type(subject).press_enter()
        return self

    def set_hobby(self):
        browser.element("[for='hobbies-checkbox-3']").click()
        return self

    def set_picture(self, path):
        browser.element('#uploadPicture').send_keys(files.abs_path_from_project_root(path))
        return self

    def set_address(self, address):
        browser.element('#currentAddress').type(address)
        return self

    def set_state(self, state):
        browser.element('#react-select-3-input').type(state).press_enter()
        return self

    def set_city(self, city):
        browser.element('#react-select-4-input').type(city).press_enter()
        return self

    def click_submit(self):
        browser.element('#submit').press_enter()
        return self

    def should_have_title(self, value):
        browser.element('#example-modal-sizes-title-lg').should(have.text(value))

    def should_have_registered(self, user):

        data = [
            ('Student Name', f'{user.first_name} {user.last_name}'),
            ('Student Email', user.email),
            ('Gender', user.gender),
            ('Mobile', user.phone_number),
            ('Date of Birth', user.date_of_birth),
            ('Subjects', user.subject),
            ('Hobbies', user.hobby),
            ('Picture', user.picture),
            ('Address', user.address),
            ('State and City', f'{user.state} {user.city}')
        ]
        rows = s('.modal-content').all('tbody tr')
        for row, value in data:
            rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))
