import pytest
from selene import browser


@pytest.fixture(autouse=True)
def browser_open():
    browser.open('https://demoqa.com/automation-practice-form')

@pytest.fixture(autouse=True)
def browser_config():
    browser.config.window_width = 1728
    browser.config.window_height = 1440
