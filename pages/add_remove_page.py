from pages.base_page import BasePage
from links.links import add_remove_url

class addRemovePage(BasePage):
    
    add_button = "button[onclick='addElement()']"
    delete_button = "button[onclic='deleteElement()']"
    url = add_remove_url
    def __init__(self, page):
        super().__init__(page)
    
    def click_add_button(self):
        self.page.locator(self.add_button).click()
        
    def get_delete_buttons_count(self):
        # Gjkexftv rjkbxtcndj ryjgjr
        return self.page.locator(self.delete_button).count()
    
    def click_delete_button(self, index=0):
        buttons = self.page.locator(self.DELETE_BUTTONS)
        if index < buttons.count():
            buttons.nth(index).click()
        else:
            raise IndexError("Индекс кнопки 'Удалить' выходит за границы.")