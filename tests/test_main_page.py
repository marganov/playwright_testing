import pytest
import requests
from pages.main_page import MainPage
from links.links import MAIN_URL

@pytest.mark.tests_mainPage
@pytest.mark.smoke
def test_open_page(page):
    main_page = MainPage(page)
    main_page.open()
    assert main_page.get_title() == "The Internet"

@pytest.mark.api
@pytest.mark.smoke
def test_page_availability():
    response = requests.get(MAIN_URL)
    assert response.status_code == 200

@pytest.mark.smoke
def test_github_link(page):
    main_page = MainPage(page)
    main_page.open()

    # Проверка видимости ссылки
    assert main_page.is_github_link_visible(), "GitHub link could not be located"

    # Проверка корректности ссылки
    href = main_page.get_github_link_href()
    assert href is not None, "GitHub link href is missing"
    response = requests.get(href)
    assert response.status_code == 200, f"GitHub link is broken, status code: {response.status_code}"
