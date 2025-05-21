from pages.form_fields import FormFields

page = FormFields()
page.open_page(FormFields.form_fields_url)

name = 'Sylwia'
password = '!123AbC'
drink = 'Wine'
color = 'Blue'
email = 'a123@nicos.com'


def test_name_field():
    # page.open_page(FormFields.form_fields_url)
    name_field = page.get_element_by_id(page.name_input_id)
    page.input_text(name_field, name)
    value = page.get_attribute_value(name_field)
    assert value == name


def test_password_field():
    # page.open_page(FormFields.form_fields_url)
    password_field = page.get_element_by_css_selector(page.password_input_type)
    page.input_text(password_field, password)
    value = page.get_attribute_value(password_field)
    assert value == password


checkboxes = {
    'Water': 'drink1',
    'Milk': 'drink2',
    'Coffee': 'drink3',
    'Wine': 'drink4',
    'Ctrl-Alt-Delight': 'drink5'
}


def test_water_checked():
    checkbox = page.get_element_by_id(checkboxes['Water'])
    page.select_checkbox(checkbox)
    assert checkbox.is_selected() is True


def test_milk_unchecked():
    checkbox = page.get_element_by_id(checkboxes['Milk'])
    page.deselect_checkbox(checkbox)
    assert checkbox.is_selected() is False


def test_wine_checked():
    checkbox = page.get_element_by_id(checkboxes['Wine'])
    page.select_checkbox(checkbox)
    assert checkbox.is_selected() is True


def test_coffee_unchecked():
    checkbox = page.get_element_by_id(checkboxes['Coffee'])
    page.deselect_checkbox(checkbox)
    assert checkbox.is_selected() is False


def test_delight_checked():
    checkbox = page.get_element_by_id(checkboxes['Ctrl-Alt-Delight'])
    page.select_checkbox(checkbox)
    assert checkbox.is_selected() is True


def test_delight_unchecked():
    checkbox = page.get_element_by_id(checkboxes['Ctrl-Alt-Delight'])
    page.deselect_checkbox(checkbox)
    assert checkbox.is_selected() is False

radio_buttons = {
    'Red': 'color1',
    'Blue': 'color2',
    'Yellow': 'color3',
    'Green': 'color4',
    '#FFC0CB': 'color5',
}


def test_red_selected():
    radio = page.get_element_by_id(radio_buttons['Red'])
    page.select_radio_button(radio)
    assert radio.is_selected() is True

def test_blue_selected():
    radio = page.get_element_by_id(radio_buttons['Blue'])
    page.select_radio_button(radio)
    assert radio.is_selected() is True

def test_red_not_selected():
    radio = page.get_element_by_id(radio_buttons['Red'])
    assert radio.is_selected() is False

def test_email():
    email_element = page.input_email(email)
    assert page.get_attribute_value(email_element) == email


message = 'one cheesecake please!'


def test_message_box():
    page.clear_message()
    textarea_element = page.input_message(message)
    assert page.get_attribute_value(textarea_element) == message

