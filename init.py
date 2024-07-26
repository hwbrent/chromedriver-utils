from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


def init() -> webdriver.Chrome:
    """
    Initialises and returns a selenium webdriver
    """

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
    options.add_argument("--disable-gpu")  # Disable GPU acceleration in headless mode

    service = ChromeService(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(options=options, service=service)

    return driver
