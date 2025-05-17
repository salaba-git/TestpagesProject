from pages.form_fields import FormFields

page = FormFields()

name = 'Sylwia'
password = '!123AbC'
drink = 'Wine'
color = 'Blue'


def test_name_field():
    page.open_page(FormFields.form_fields_url)
    name_field = page.get_element_by_id(page.name_input_id)
    page.input_text(name_field, name)
    value = page.get_attribute_value(name_field)
    assert value == name


def test_password_field():
    page.open_page(FormFields.form_fields_url)
    password_field = page.get_element_by_css_selector(page.password_input_type)
    page.input_text(password_field, password)
    value = page.get_attribute_value(password_field)
    assert value == password
