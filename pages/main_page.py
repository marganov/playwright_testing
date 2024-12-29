from pages.base_page import BasePage
from links.links import MAIN_URL

class MainPage(BasePage):
    GITHUB_ELEM = "a[href*='github.com/tourdedave'] img[alt='Fork me on GitHub']"
    GITHUB_FALLBACK_ELEM = "a[href*='github.com'] img"
    url = MAIN_URL
    def __init__(self, page):
        super().__init__(page)

    def is_github_link_visible(self) -> bool:
        """Проверяет видимость ссылки на GitHub."""
        if self.page.locator(self.GITHUB_ELEM).is_visible():
            return True
        return self.page.locator(self.GITHUB_FALLBACK_ELEM).is_visible()

    def get_github_link_href(self) -> str:
        """Возвращает href ссылки на GitHub."""
        github_link = self.page.locator(self.GITHUB_ELEM)
        if not github_link.is_visible():
            github_link = self.page.locator(self.GITHUB_FALLBACK_ELEM)
        return github_link.locator("..").get_attribute("href")
