from pages.base_page import BasePage
from links.links import MAIN_URL

class MainPage(BasePage):
    GITHUB_LINK = "a[href*='github.com/tourdedave'] img[alt='Fork me on GitHub']"
    GITHUB_FALLBACK_LINK = "a[href*='github.com'] img"

    def open_main_page(self):
        """Открывает главную страницу."""
        self.goto(MAIN_URL)

    def is_github_link_visible(self) -> bool:
        """Проверяет видимость ссылки на GitHub."""
        if self.page.locator(self.GITHUB_LINK).is_visible():
            return True
        return self.page.locator(self.GITHUB_FALLBACK_LINK).is_visible()

    def get_github_link_href(self) -> str:
        """Возвращает href ссылки на GitHub."""
        github_link = self.page.locator(self.GITHUB_LINK)
        if not github_link.is_visible():
            github_link = self.page.locator(self.GITHUB_FALLBACK_LINK)
        return github_link.locator("..").get_attribute("href")
