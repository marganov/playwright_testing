from pages.base_page import BasePage
from links.links import js_alerts_url

class JSAlertsPage(BasePage):
    url = js_alerts_url
    def __init__(self, page):
        super().__init__(page)
    
    def get_alert_button(self):
        """Получаем кнопку с алертом"""
        button = self.get_element("button[onclick='jsAlert()']")
        assert button.is_visible(), "Кнопка не обнаружена"
        return button
    
    def get_confirm_button(self):
        button = self.get_element("button[onclick='jsConfirm'()]")
        assert button.is_visible(), "Кнопка не обнаружена"
        return button
    
    def get_promt_button(self):
        button = self.get_element("button[onclick='jsPromt'()]")
        assert button.is_visible(), "Кнопка не обнаружена"
        return button
    