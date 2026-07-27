import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


# Step 45

@pytest.mark.parametrize(
    "message",
    [
        "Hello",
        "Selenium Automation",
        "12345"
    ]
)
def test_simple_form_submission(driver, base_url, message):

    driver.get(f"{base_url}/simple-form-demo")

    textbox = driver.find_element(By.ID, "user-message")
    textbox.clear()
    textbox.send_keys(message)

    driver.find_element(By.ID, "showInput").click()

    output = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )

    assert output.text == message


# Step 43

def test_checkbox_demo(driver, base_url):

    driver.get(f"{base_url}/checkbox-demo")

    checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "input[type='checkbox']")
        )
    )

    checkbox.click()

    assert checkbox.is_selected()

    checkbox.click()

    assert not checkbox.is_selected()


# Step 49


def test_dropdown_selection(driver, base_url):

    driver.get(f"{base_url}/select-dropdown-demo")

    dropdown = Select(
        driver.find_element(By.ID, "select-demo")
    )

    dropdown.select_by_visible_text("Wednesday")

    selected = dropdown.first_selected_option.text

    assert selected == "Wednesday"

'''from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://www.lambdatest.com/selenium-playground"


# Step 42


def test_simple_form_submission(driver):

    driver.get(f"{BASE_URL}/simple-form-demo")

    message = "Hello Selenium"

    input_box = driver.find_element(By.ID, "user-message")
    input_box.clear()
    input_box.send_keys(message)

    show_button = driver.find_element(By.ID, "showInput")
    show_button.click()

    output = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.ID, "message")
        )
    )

    assert output.text == message

# Step 43

def test_checkbox_demo(driver):

    driver.get(f"{BASE_URL}/checkbox-demo")

    checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "input[type='checkbox']")
        )
    )

    checkbox.click()

    assert checkbox.is_selected()

    checkbox.click()

    assert not checkbox.is_selected()
'''