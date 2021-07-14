link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_button(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert button is not None, "Error!"
