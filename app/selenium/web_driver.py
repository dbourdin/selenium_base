from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.events import EventFiringWebDriver

from app import settings
from app.selenium.selenium_utils import MyListener


chrome_options = Options()
if settings.HEADLESS:
    chrome_options.add_argument("--headless")
driver = EventFiringWebDriver(webdriver.Chrome(options=chrome_options), MyListener())
