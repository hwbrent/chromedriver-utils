from typing import Iterable

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


default_args = [
    "--headless",
    "--disable-gpu",
]


def init(
    chromedriver_path: str, args: Iterable[str] = default_args
) -> webdriver.Chrome:
    """
    Given the path of a `chromedriver` executable and a set of options, this
    function initialises a `WebDriver`, and returns it.

    Default options (for `selenium.webdriver.ChromeOptions`):
    - `--headless` - Run Chrome in headless mode (no GUI)
    - `--disable-gpu` - Disable GPU acceleration in headless mode
    """

    options = webdriver.ChromeOptions()
    for arg in args:
        options.add_argument(arg)

    service = ChromeService(chromedriver_path)
    driver = webdriver.Chrome(options=options, service=service)

    return driver
