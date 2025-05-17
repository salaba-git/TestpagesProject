from time import sleep
from pages.driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(Driver):
    """Collection of generic methods to use throughout the framework:

        - Locator methods: ID, CLASS NAME, NAME, TAG NAME, CSS SELECTOR, XPATH
        - Cookie popup handler
        - basic

    """
    url = 'https://practice-automation.com/'
    heading_title_class = 'wp-block-heading'
    links_css_selector = 'a.wp-block-button__link.wp-element-button'
    button_id = ''

    def __init__(self):
        super().__init__()
        self.wait = WebDriverWait(self.driver, 20)

    def open_page(self, url):
        return self.driver.get(url)

    def get_element_by_id(self, element_id):
        """Locator method to find webpage elements based on ID

        :param element_id:
        :return: 1st element found matching criteria
        """
        return self.driver.find_element(By.ID, element_id)

    def get_element_by_class_name(self, element_class_name):
        """Locator method to find webpage elements based on CLASS NAME

        :param element_class_name:
        :return: 1st element found matching criteria
        """
        return self.driver.find_element(By.CLASS_NAME, element_class_name)

    def get_element_by_css_selector(self, element_css_selector):
        """Locator method to find webpage elements based on CSS SELECTOR

        :param element_css_selector:
        :return: 1st element found matching criteria
        """
        return self.driver.find_element(By.CSS_SELECTOR, element_css_selector)

    def get_element_by_name(self, element_name):
        """Locator method to find webpage elements based on NAME

        :param element_name:
        :return: 1st element found matching criteria
        """
        return self.driver.find_element(By.NAME, element_name)

    def get_element_by_tag_name(self, element_tag_name):
        """Locator method to find webpage elements based on TAG NAME

        :param element_tag_name:
        :return: 1st element found matching criteria
        """
        return self.driver.find_element(By.TAG_NAME, element_tag_name)

    def get_element_by_link_text(self, href_text):
        """Locator method to find webpage elements based on TAG NAME

        :param href_text:
        :return: 1st element found matching criteria
        """
        return self.driver.find_element(By.LINK_TEXT, href_text)

    def get_element_by_xpath(self, element_xpath):
        """Locator method to find webpage elements based on XPATH

        :param element_xpath:
        :return: 1st element found matching criteria
        """
        return self.driver.find_element(By.XPATH, element_xpath)

    def get_elements_by_id(self, element_id):
        """Locator method to find webpage elements based on ID

        :param element_id:
        :return: list of elements
        """
        return self.driver.find_elements(By.ID, element_id)

    def get_elements_by_class_name(self, element_class_name):
        """Locator method to find webpage elements based on CLASS NAME

        :param element_class_name:
        :return: list of elements
        """
        return self.driver.find_elements(By.CLASS_NAME, element_class_name)

    def get_elements_by_css_selector(self, element_css_selector):
        """Locator method to find webpage elements based on CSS SELECTOR

        :param element_css_selector:
        :return: list of elements
        """
        return self.driver.find_elements(By.CSS_SELECTOR, element_css_selector)

    def get_elements_by_name(self, element_name):
        """Locator method to find webpage elements based on NAME

        :param element_name:
        :return: list of elements
        """
        return self.driver.find_elements(By.NAME, element_name)

    def get_elements_by_tag_name(self, element_tag_name):
        """Locator method to find webpage elements based on TAG NAME

        :param element_tag_name:
        :return: list of elements
        """
        return self.driver.find_elements(By.TAG_NAME, element_tag_name)

    def get_elements_by_xpath(self, element_xpath):
        """Locator method to find webpage elements based on XPATH

        :param element_xpath:
        :return: list of elements
        """
        return self.driver.find_elements(By.XPATH, element_xpath)

    def click_button(self, button_id):
        """

        :return: none
        """
        self.get_element_by_id(button_id).click()

    def click_on_text(self, clickable_text):
        """

        :param clickable_text:
        :return:
        """
        self.get_element_by_xpath(f"//*[contains(text(), '{clickable_text}')]").click()

    def click_cookie_modal(self):
        """Method to automatically click on Cookies popup window when it appears blocking any interaction with
        webpage elements.
        """
        self.get_element_by_class_name('fc-button-label').click()

    def input_text(self, element, text):
        element.send_keys(text)

    def get_attribute_value(self, element):
        return element.get_attribute('value')

    def collect_links(self):
        """
        Method collecting all links by locating a-href associated tags using xpath '//a[@href]'

        :return: dictionary of HTML links as {link_text: href_link, ...}
        """
        href_elements = self.get_elements_by_xpath("//a[@href]")
        links = {}
        for elem in href_elements:
            links[elem.text] = elem.get_attribute('href')
        return links

    def wait_for_text_load_by_id(self, wait_element_id, expected_text):
        """
        Method using WebDriverWait (with timeout) to wait for specified text to be displayed under a
        tag with specified ID

        :param wait_element_id:
        :param expected_text:
        :return: result of the wait (element was found or timeout exceeded)
        """
        element = (By.ID, wait_element_id)
        is_text_present = self.wait.until(ec.text_to_be_present_in_element(element, expected_text))
        return is_text_present

    def get_element_by_text(self, element_text):
        return self.get_element_by_xpath(f"//*[contains(text(), '{element_text}')]")

    def wait_for_clickable_text(self, element_text):
        element = (By.XPATH, f"//*[contains(text(), '{element_text}')]")
        is_button_present = self.wait.until(ec.element_to_be_clickable(element))
        return is_button_present

    def scroll_to_element(self, element_object):
        js = "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});"
        self.driver.execute_script(js, element_object)
        sleep(0.5)

    def scroll_to_page_bottom_lazyload(self):
        last_position = self.driver.execute_script('return window.pageYOffset;')
        while True:
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            sleep(5)
            current_position = self.driver.execute_script('return window.pageYOffset;')
            if current_position == last_position:
                break
            last_position = current_position
