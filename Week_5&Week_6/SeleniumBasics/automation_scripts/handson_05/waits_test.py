import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

# Launch Chrome
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.maximize_window()


# STEP 36 - Explicit Wait


driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo")

button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".btn-success-auto")
    )
)

button.click()

wait = WebDriverWait(driver, 10)

success_alert = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".alert-success")
    )
)

print("Alert Text :", success_alert.text)

assert "autocloseable success message" in success_alert.text.lower()

print("Explicit Wait Test Passed")


# STEP 37 - Compare sleep() vs Explicit Wait


# Using time.sleep() 

driver.refresh()

start = time.time()

driver.find_element(By.CSS_SELECTOR, ".btn-success-auto").click()

time.sleep(3)

print("time.sleep() Duration :", round(time.time() - start, 2), "seconds")

#  Using Explicit Wait

driver.refresh()

start = time.time()

button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".btn-success-auto")
    )
)

button.click()

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".alert-success")
    )
)

print("Explicit Wait Duration :", round(time.time() - start, 2), "seconds")

"""
time.sleep()
-------------
Always waits the full duration even if the element appears earlier.

WebDriverWait
-------------
Returns immediately when the condition is satisfied.
It is faster and more reliable.
"""


# STEP 38 - Wait Until Clickable


driver.refresh()

start = time.time()

button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".btn-success-auto")
    )
)

button.click()

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".alert-success")
    )
)

print("Clicked after waiting for clickability.")

"""
visibility_of_element_located
-----------------------------
Element is present and visible.

element_to_be_clickable
-----------------------
Element is visible, enabled and can be clicked.
"""


# STEP 39 - Fluent Wait


driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")

wait = WebDriverWait(
    driver,
    timeout=10,
    poll_frequency=0.5,
    ignored_exceptions=[NoSuchElementException]
)

row = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//table//tbody/tr[1]")
    )
)

print("First table row loaded successfully.")

driver.quit()