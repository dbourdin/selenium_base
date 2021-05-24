import requests
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

from app.selenium.web_driver import driver


class BasePage:
    def __init__(self):
        self._driver = driver

    def _click_element(self, selector):
        self._get_element(selector).click()

    def _element_exists(self, selector):
        try:
            self._get_element(selector)
            return True
        except NoSuchElementException:
            return False

    def _get_element(self, selector):
        return self._driver.find_element(*selector)

    def _is_visible(self, selector):
        return self._get_element(selector).is_displayed()

    def _send_text(self, selector, text):
        self._get_element(selector).send_keys(text)

    @staticmethod
    def _download_file(download_url):
        return requests.get(download_url, stream=True)

    def _get_current_url(self):
        return self._driver.current_url

    def _select_option_in_dropdown_by_text(self, dropdown_selector, option_text):
        Select(self._get_element(dropdown_selector)).select_by_visible_text(option_text)
