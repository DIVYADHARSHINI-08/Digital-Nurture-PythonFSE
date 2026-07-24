from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

# Launch Chrome
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.maximize_window()
driver.implicitly_wait(10)


# Step 28


driver.get("https://www.lambdatest.com/selenium-playground/")

# Click "Simple Form Demo"
driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

# Verify URL
assert "simple-form-demo" in driver.current_url

print("Current URL:", driver.current_url)

# Go back
driver.back()

time.sleep(2)


# Step 29


driver.execute_script("window.open('https://www.google.com');")

print("Window Handles:")
print(driver.window_handles)

driver.switch_to.window(driver.window_handles[1])

print("Google Title:", driver.title)


# Step 30


driver.switch_to.window(driver.window_handles[0])

os.makedirs("screenshots", exist_ok=True)

driver.save_screenshot("screenshots/playground_screenshot.png")

print("Screenshot saved successfully.")

# Step 31


print("Current Window Size:")
print(driver.get_window_size())

# A consistent browser window size ensures the webpage layout
# remains the same across different executions. This helps avoid
# failures caused by responsive design changes.

driver.set_window_size(1280, 800)

print("Updated Window Size:")
print(driver.get_window_size())

time.sleep(2)

driver.quit()