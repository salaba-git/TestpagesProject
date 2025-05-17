from pages.base_page import BasePage


class FormFields(BasePage):

    form_fields_url = 'https://practice-automation.com/form-fields/'
    name_input_id = 'name-input'
    password_input_type = 'input[type=password]'

    def __init__(self):
        super().__init__()

