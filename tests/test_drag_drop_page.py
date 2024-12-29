import pytest
from pages.drag_drop_page import dragDropPage


@pytest.mark.smoke
def test_simple_drag_drop(page):
    drag_drop_page = dragDropPage(page)
    drag_drop_page.open()

    # Получаем элементы для drag-and-drop
    element_1 = drag_drop_page.get_dnd_element_1()
    element_2 = drag_drop_page.get_dnd_element_2()

    # Сохраняем начальный текст из элементов
    text_element_1_before = element_1.text_content()
    text_element_2_before = element_2.text_content()

    # Выполняем drag-and-drop
    element_1.drag_to(element_2)

    # Проверяем, что элементы поменялись местами
    assert element_1.text_content(
    ) == text_element_2_before, "Элемент 1 не сменил позицию с элементом 2"
    assert element_2.text_content(
    ) == text_element_1_before, "Элемент 2 не сменил позицию с элементом 1"
