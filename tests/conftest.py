import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()


@pytest.fixture(scope="function", params=["chromium", "firefox", "webkit"])
def all_browsers_page(request):
    """Фикстура для тестов во всех трёх браузерах."""
    with sync_playwright() as p:
        browser = getattr(p, request.param).launch(headless=True) #True для отображения браузеров во время прохождения тестов
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()
