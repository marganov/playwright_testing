from pages.js_alert_page import JSAlertsPage



def test_alert(page):
    js_alert_page = JSAlertsPage(page)
    js_alert_page.open()
    
    page.once("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Click for JS Alert").click()
    assert page.locator("#result").text_content() == "You successfully clicked an alert", "Элемент не найден"
    
def test_confirm(page):   
    js_alert_page = JSAlertsPage(page)
    js_alert_page.open()
     
    page.once("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button", name="Click for JS Confirm").click()
    assert page.locator("#result").text_content() == "You clicked: Ok", "Сообщение об успехе не найдено"

def test_dismiss(page):
    js_alert_page = JSAlertsPage(page)    
    js_alert_page.open()
    
    page.once("dialog", lambda dialog:dialog.dismiss())
    page.get_by_role("button", name="Click for JS Confirm").click()
    assert page.locator("#result").text_content() == "You clicked: Cancel", "Сообщение об успехе не найдено"
   
    
def test_prompt(page):
    # Открываем страницу
    js_alert_page = JSAlertsPage(page)
    js_alert_page.open()

    # Указываем обработчик для prompt
    page.once("dialog", lambda dialog: dialog.accept("Test Input"))
    
    # Кликаем по кнопке, вызывающей prompt
    page.get_by_role("button", name="Click for JS Prompt").click()

    # Проверяем результат после ввода
    result_text = page.locator("#result").text_content()
    assert result_text == "You entered: Test Input", "Сообщение неверно"

def test_prompt_cancel(page):
    # Открываем страницу
    js_alert_page = JSAlertsPage(page)
    js_alert_page.open()

    # Указываем обработчик для prompt
    page.once("dialog", lambda dialog: dialog.dismiss())
    
    # Кликаем по кнопке, вызывающей prompt
    page.get_by_role("button", name="Click for JS Prompt").click()

    # Проверяем результат после нажатия "Cancel"
    result_text = page.locator("#result").text_content()
    assert result_text == "You entered: null", "Сообщение неверно"

    