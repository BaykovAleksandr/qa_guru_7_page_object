import os

from selene import browser, be, have

from utils import files


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, name):
        browser.element('#firstName').should(be.blank).type(name)

    def fill_second_name(self, family):
        browser.element('#lastName').should(be.blank).type(family)

    def fill_email(self, email):
        browser.element('#userEmail').should(be.blank).type(email)

    def choose_gender(self):
        browser.element('[for="gender-radio-1"]').click()

    def fill_phone_number(self, phone):
        browser.element('#userNumber').should(be.blank).type(phone)

    def choose_birthday(self):
        browser.element('#dateOfBirthInput').click()
        browser.element(".react-datepicker__month-select>option[value='11']").click()
        browser.element(".react-datepicker__year-select>option[value='1988']").click()
        browser.element('.react-datepicker__day--019').click()

    def fill_interests(self, subject):
        browser.element('#subjectsInput').should(be.blank).type(subject).press_enter()

    def choose_hobbies(self):
        browser.element("[for='hobbies-checkbox-3']").click()

    def upload_file(self, path):
        browser.element('#uploadPicture').send_keys(files.abs_path_from_project_root(path))

    def fill_current_address(self, address):
        browser.element('#currentAddress').type(address)

    def choose_state(self, state):
        browser.element('#react-select-3-input').type(state).press_enter()

    def choose_city(self, city):
        browser.element('#react-select-4-input').type(city).press_enter()

    def click_submit(self):
        browser.element('#submit').press_enter()

    def assert_title(self, text):
        browser.element('#example-modal-sizes-title-lg').should(have.text(text))

    def assert_body(self, *result):
        browser.element('.table').all('td').even.should(
            have.exact_texts(result))


