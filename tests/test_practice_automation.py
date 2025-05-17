from time import sleep
from random import randint
from pages.base_page import BasePage
from selenium.common.exceptions import ElementClickInterceptedException

page = BasePage()
page.open_page(page.url)


def test_page_title():
    page_header = page.get_element_by_class_name(page.heading_title_class)
    assert page_header.text == 'Welcome to your software automation practice website!'


subpage_links = {
    'Form Fields': 'form-fields/',
    'Popups': 'popups/',
    'JavaScript Delays': 'javascript-delays/',
    'Calendars': 'calendars/',
    'Sliders': 'slider/',
    'Modals': 'modals/',
    'Tables': 'tables/',
    'Window Operations': 'window-operations/',
    'Hover': 'hover/',
    'Ads': 'ads/',
    'Gestures': 'gestures/',
    'File Download': 'file-download/',
    'Click Events': 'click-events/',
    'Spinners': 'spinners/',
    'File Upload': 'file-upload/',
    'Iframes': 'iframes/',
    'Broken Images': 'broken-images/',
    'Broken Links': 'broken-links/',
    'Accordions': 'accordions/'
}

for subpage in subpage_links:
    subpage_links[subpage] = page.url + subpage_links[subpage]


def test_subpage_links():
    links = page.collect_links()
    for subpage in subpage_links:
        assert links[subpage] == subpage_links[subpage]


def test_buttons_working():
    for button in subpage_links:
        page.open_page(page.url)
        page.wait_for_text_load_by_text(button)
        page.scroll_to_element_text(button)
        page.click_button_by_text(button)
        assert page.get_url() == subpage_links[button]
