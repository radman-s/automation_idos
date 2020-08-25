from selenium import webdriver

class Drivers:

    def __init__(self, argument):
        self.argument = argument

    def chrome(self):
        options = webdriver.ChromeOptions()
        options.add_argument(self.argument)
        driver = webdriver.Chrome(options=options)
        return driver




