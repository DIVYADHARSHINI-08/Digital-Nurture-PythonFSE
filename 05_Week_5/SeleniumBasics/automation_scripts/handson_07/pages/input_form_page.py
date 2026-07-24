from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InputFormPage(BasePage):

    NAME = (By.ID, "name")
    EMAIL = (By.ID, "inputEmail4")
    PASSWORD = (By.ID, "inputPassword4")
    COMPANY = (By.ID, "company")
    WEBSITE = (By.ID, "websitename")
    COUNTRY = (By.NAME, "country")
    CITY = (By.ID, "inputCity")
    ADDRESS1 = (By.ID, "inputAddress1")
    ADDRESS2 = (By.ID, "inputAddress2")
    STATE = (By.ID, "inputState")
    ZIP = (By.ID, "inputZip")

    SUBMIT = (By.XPATH, "//button[normalize-space()='Submit']")

    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR,
        ".success-msg, .alert-success, .success-message"
    )

    def fill_form(
        self,
        name,
        email,
        password,
        company,
        website,
        country,
        city,
        address1,
        address2,
        state,
        zip_code
    ):
        self.wait_for_element(self.NAME).send_keys(name)
        self.wait_for_element(self.EMAIL).send_keys(email)
        self.wait_for_element(self.PASSWORD).send_keys(password)
        self.wait_for_element(self.COMPANY).send_keys(company)
        self.wait_for_element(self.WEBSITE).send_keys(website)

        Select(
            self.wait_for_element(self.COUNTRY)
        ).select_by_visible_text(country)

        self.wait_for_element(self.CITY).send_keys(city)
        self.wait_for_element(self.ADDRESS1).send_keys(address1)
        self.wait_for_element(self.ADDRESS2).send_keys(address2)
        self.wait_for_element(self.STATE).send_keys(state)
        self.wait_for_element(self.ZIP).send_keys(zip_code)

    

    def submit_form(self):

        button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.SUBMIT)
        )

        # Scroll to the button
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        # Move the page slightly upward so the sticky header doesn't cover the button
        self.driver.execute_script("window.scrollBy(0, -150);")

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SUBMIT)
        )

        # Use JavaScript click to avoid interception
        self.driver.execute_script("arguments[0].click();", button)

    def get_success_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        ).text