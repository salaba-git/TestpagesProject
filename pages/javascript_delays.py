from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

class JavascriptDelays(BasePage):

    url = 'https://practice-automation.com/javascript-delays/'
    wait_element_id = 'delay'
    expected_text = 'Liftoff!'
    #ignore_errors = [NoSuchElementException, ElementNotInteractableException]

    def __init__(self):
        super().__init__()

    def wait_for_text(self, wait_element_id=wait_element_id, expected_text=expected_text):
        self.open_page(self.url)
        self.click_button('start')
        wait = WebDriverWait(self, 10)
        is_text_present = wait.until(ec.text_to_be_present_in_element((By.ID, wait_element_id), expected_text))
        return is_text_present