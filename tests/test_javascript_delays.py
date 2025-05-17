from pages.javascript_delays import JavascriptDelays

page = JavascriptDelays()


def test_button_click():
    page.open_page(page.javascript_delays_url)
    start_object = page.get_element_by_id(page.start_element_id)
    page.scroll_to_element(start_object)
    page.click_button(page.start_element_id)
    page.wait_for_text_load_by_id(page.wait_element_id, 'Liftoff!')
    wait_object = page.get_element_by_id(page.wait_element_id)
    assert wait_object.text == 'Liftoff!'
