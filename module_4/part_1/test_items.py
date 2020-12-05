
def test_add_one_item_to_basket_with_notification(browser):
    #Data
    add_to_basket_button_locator =".btn-add-to-basket"
    assert_error_message = "The button isn't there or the button text is incorrect"

    # Act
    add_to_basket_button = browser.find_element_by_css_selector(add_to_basket_button_locator)

    # Assert
    basket_button_value = add_to_basket_button.get_attribute("value")
    basket_button_text = add_to_basket_button.text
    assert basket_button_value in basket_button_text, assert_error_message
