from pages.base_page import BasePage

page = BasePage()

def test_page_title():
    page.open_page(page.url)
    page_header = page.get_element_by_class_name(page.heading_title_class)
    assert page_header.text == 'Welcome to your software automation practice website!'

subpage_links = {
    'Form Fields': page.url+'form-fields/',
    'Popups': page.url+'popups/',
    'JavaScript Delays': page.url+'javascript-delays/',
    'Calendars': page.url+'calendars/',
    'Sliders': page.url+'sliders/',
    'Modals': page.url+'modals/',
    'Tables': page.url+'tables/',
    'Window Operations': page.url+'window-operations/',
    'Hover': page.url+'hover/',
    'Ads': page.url+'ads/',
    'Gestures': page.url+'gestures/',
    'File Download': page.url+'file-download/',
    'Click Events': page.url+'click-events/',
    'Spinners': page.url+'spinners/',
    'File Upload': page.url+'file-upload/',
    'Iframes': page.url+'iframes/',
    'Broken Images': page.url+'broken-images/',
    'Broken Links': page.url+'broken-links/',
    'Accordions': page.url+'accordions/',
}

def test_subpage_links():
    page.open_page(page.url)
    links = page.collect_links()
    assert links['Form Fields'] == subpage_links['Form Fields']
    assert links['File Upload'] == subpage_links['File Upload']
    assert links['Click Events'] == subpage_links['Click Events']
    assert links['Modals'] == subpage_links['Modals']
    assert links['Ads'] == subpage_links['Ads']

