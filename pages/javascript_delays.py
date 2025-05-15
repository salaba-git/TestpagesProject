from pages.base_page import BasePage

class JavascriptDelays(BasePage):

    javascript_delays_url = 'https://practice-automation.com/javascript-delays/'
    wait_element_id = 'delay'
    start_element_id = 'start'
    #ignore_errors = [NoSuchElementException, ElementNotInteractableException]

    def __init__(self):
        super().__init__()



