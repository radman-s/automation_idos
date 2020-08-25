from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class BaseElement(object):

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        return None


    def click(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=self.locator))
        element.click()
        return None

    def input_text(self, text):
        self.web_element.send_keys(text)
        return None

    def text(self):
        text = self.web_element.text
        return text

    def enter(self):
        element = ActionChains(self.driver)
        element.send_keys(Keys.ENTER).perform()
        return None

    def arrow_down(self):
        element = ActionChains(self.driver)
        element.send_keys(Keys.ARROW_DOWN).perform()
        return None

    def get_time_format(self):
        time = self.web_element.text[:5]
        return time.replace(':', '.')




