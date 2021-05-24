from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.events import AbstractEventListener

from app import settings


class WaitForPageToLoad:
    WAIT_FOR_PAGE_SCRIPT = ("return (typeof document != 'undefined')"
                            " && (document.readyState == 'complete')"
                            " && (typeof $ != 'undefined')"
                            " && ($.active == 0);")

    def __call__(self, driver):
        return driver.execute_script(self.WAIT_FOR_PAGE_SCRIPT)


# Event listener used to add extra functionality to selenium actions
class MyListener(AbstractEventListener):
    @staticmethod
    def _wait_for_page_to_load(driver):
        WebDriverWait(driver, settings.WAIT_TIMEOUT).until(WaitForPageToLoad())

    def after_click(self, element, driver):
        self._wait_for_page_to_load(driver)
