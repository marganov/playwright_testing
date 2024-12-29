import pytest
from pages.add_remove_page import addRemovePage
from links.links import add_remove_url
 


@pytest.mark.smoke
@pytest.mark.functional
def test_massive_add_delete(page):
    add_remove_page = addRemovePage(page)
    add_remove_page.open()
    
    # Добавляем 100 кнопок
    for _ in range(100):
        page.evaluate("addElement()")
    
    buttons = page.locator(".added-manually")
    assert buttons.count() == 100, "Должно быть добавлено 100 кнопок"
    
    # Удаляем все кнопки
    for _ in range(100):
        page.evaluate("deleteElement()")
    
    assert buttons.count() == 0, "Все кнопки должны быть удалены"



@pytest.mark.smoke
@pytest.mark.UI
def test_add_element_button(page):
    add_remove_page = addRemovePage(page)
    add_remove_page.open()
    
    # Нажимаем на кнопку "Add Element" 5 раз
    for _ in range(5):
        page.click("button[onclick='addElement()']")
    
    page.wait_for_selector("button.added-manually")
    
    delete_button = page.locator("button.added-manually")
    assert delete_button.count() == 5, "Ожидалось 5 кнопок"
    
    # Удаляем все кнопки
    while delete_button.count() > 0:
        delete_button.first.click()
    
    # Проверяем, что все кнопки удалены
    assert delete_button.count() == 0, "Кнопки не удалены"