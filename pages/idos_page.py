from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .locator import Locator
from .base_page import BasePage

class IdosPage(BasePage):

    url = 'https://idos.idnes.cz/vlaky/spojeni/?changeShield=true'

    # search inputs
    @property
    def from_search(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="From"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def to_search(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="To"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def search_button(self):
        locator = Locator(By.XPATH, '//div[@class="submit"]/button')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def only_direct(self):
        locator = Locator(By.CSS_SELECTOR, 'label[for="OnlyDirect"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def time1(self):
        locator = Locator(By.XPATH, '(//h2[@class="reset date"])[1]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def time2(self):
        locator = Locator(By.XPATH, '(//h2[@class="reset date"])[2]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def time3(self):
        locator = Locator(By.XPATH, '(//h2[@class="reset date"])[3]')
        return BaseElement(driver=self.driver, locator=locator)

