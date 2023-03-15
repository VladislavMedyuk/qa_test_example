from pages.form_page import FormPage


class TestFormPage:
    def test_form(self, browser):
        form_page = FormPage(browser, 'https://demoqa.com/automation-practice-form')
        form_page.open()
        person = form_page.fill_fields_and_submit()
        result = form_page.form_result()
        print(person)
        print(result)
        assert f"{person.first_name} {person.last_name}" == result[0], 'the form has not been filled'
        assert person.email == result[1], 'the form has not been filled'
