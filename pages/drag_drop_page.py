from pages.base_page import BasePage
from links.links import drag_drop_url

class dragDropPage(BasePage):
    url = drag_drop_url
    
    def __init__(self, page):
        super().__init__(page)
        
    def get_dnd_element_1(self):
        return self.get_element("div.column#column-a[draggable='true']")
    
    def get_dnd_element_2(self):
        return self.get_element("div.column#column-b[draggable='true']")
