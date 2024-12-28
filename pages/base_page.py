from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        """Открывает указанную страницу."""
        self.page.goto(url)

    def wait_for_element(self, locator: str):
        """Ожидает появления элемента на странице."""
        self.page.wait_for_selector(locator)

    def get_element(self, locator: str):
        """Возвращает элемент по локатору."""
        return self.page.locator(locator)

    def get_title(self) -> str:
        """Возвращает заголовок страницы."""
        return self.page.title()
