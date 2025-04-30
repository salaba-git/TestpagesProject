from selenium import webdriver

class Driver:
    """
    Class for initialization of selenium webdriver for Chrome session.
    Implicitly wait included (2)
    """
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)

    def get_driver(self):
        return self.driver