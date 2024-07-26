from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


def init(chromedriver_path: str, headless: bool = True) -> webdriver.Chrome:
    """
    Given the path of a `chromedriver` executable, this function initialises
    a `WebDriver`, and returns it
    """

    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
    options.add_argument("--disable-gpu")  # Disable GPU acceleration in headless mode

    service = ChromeService(chromedriver_path)
    driver = webdriver.Chrome(options=options, service=service)

    return driver
