from selenium import webdriver

class Driver:
    """
    Class for initialization of selenium webdriver for Chrome session.
    Implicitly wait included (2)
    """
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        # self.driver.set_network_conditions(
        #     offline=False,
        #     latency=5,  # additional latency (ms)
        #     download_throughput=1000 * 1024,  # maximal throughput
        #     upload_throughput=500 * 1024)  # maximal throughput

    def get_driver(self):
        return self.driver


    def get_url(self):
        return self.driver.current_url

