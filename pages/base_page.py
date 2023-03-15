from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def element_is_visible(self, locator, timeout=10):
        return Wait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=10):
        return Wait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))

    def remove_footer(self):
        self.browser.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.browser.execute_script('document.getElementById("fixedban").style.display="none"')
