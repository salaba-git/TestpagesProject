from selenium.webdriver.common.devtools.v133.service_worker import set_force_update_on_page_load

from pages.base_page import BasePage
import pytest

page = BasePage()
page_url = 'https://practice-automation.com/'

def test_page_title():
    page.open_page(page_url)
    element_class_name = 'wp-block-heading'
    page_header = page.get_elements_by_class_name(element_class_name)[0]
    assert page_header.text == 'Welcome to your software automation practice website!'

subpage_links = {
    'Form Fields': page_url+'form-fields/',
    'Popups': page_url+'popups/'
}

collected_links = page.collect_subpage_links(page_url)
print(collected_links)


def test_form_fields_link():
    assert subpage_links['Form Fields'] == collected_links['Form Fields']

