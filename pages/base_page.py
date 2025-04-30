from pages.driver import Driver
from selenium.webdriver.common.by import By

class BasePage(Driver):
    """Collection of generic methods to use throughout the framework:

        - Locator methods: ID, CLASS NAME, NAME, TAG NAME, CSS SELECTOR, XPATH
        - Cookie popup handler
        - basic

    """

    def __init__(self):
        super().__init__()

    def open_page(self, url):
        return self.driver.get(url)

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

    def click_cookie_modal(self):
        """Method to automatically click on Cookies popup window when it appears blocking any interaction with
        webpage elements.
        """
        self.get_element_by_class_name('fc-button-label').click()

    def input_text(self, element, text):
        element.send_keys(text)

    def collect_subpage_links(self, page_url):
        self.open_page(page_url)
        element_class_name = 'wp-block-button__link wp-element-button'
        subpages = self.get_elements_by_class_name(element_class_name)
        subpage_links = {}
        for subpage in subpages:
            link = subpage.get_element('href')
            link_name = subpage.text
            subpage_links[link_name] = link
        return subpage_links