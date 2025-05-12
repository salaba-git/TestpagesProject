from pages.javascript_delays import JavascriptDelays

page = JavascriptDelays()

def test_button_click():
    #page.open_page(page.url)
    #page.click_button('start')
    result = page.wait_for_text()
    print(result)
