from pages.javascript_delays import JavascriptDelays

page = JavascriptDelays()

def test_button_click():
    page.open_page(page.javascript_delays_url)
    page.click_button(page.start_element_id)
    result = page.wait_for_text_load(page.wait_element_id, 'Liftoff!')
    print(result)
