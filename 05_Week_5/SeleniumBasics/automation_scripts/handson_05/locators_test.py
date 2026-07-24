from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.implicitly_wait(10)

driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

#By.ID

element = driver.find_element(By.ID, "user-message")
print("Located using ID")

#By.NAME

element = driver.find_element(By.NAME, "message")
print("Located using NAME")

#By.CLASS_NAME

element = driver.find_element(By.CLASS_NAME, "form-control")
print("Located using CLASS_NAME")

#By.TAG_NAME

element = driver.find_element(By.TAG_NAME, "input")
print("Located using TAG_NAME")

#Absolute XPath

# Absolute XPath
# The website structure may change, so this locator can fail.

# Absolute XPath
driver.find_element(
    By.XPATH,
    "/html/body/div[1]/div/main/div/section[2]/div/div/div/div[1]/div[2]/div/div[1]/input"
)
print("Located using Absolute XPath")

#Relative XPath

element = driver.find_element(
    By.XPATH,
    "//input[@id='user-message']"
)
print("Located using Relative XPath")

## CSS by ID
driver.find_element(By.CSS_SELECTOR, "#user-message")
print("Located using CSS Selector (ID)")

# CSS by Attribute (using placeholder)
driver.find_element(
    By.CSS_SELECTOR,
    "input[placeholder='Please enter your Message']"
)
print("Located using CSS Selector (Attribute)")

# CSS using class
driver.find_element(
    By.CSS_SELECTOR,
    "input.border"
)
print("Located using CSS Selector (Class)")

# Navigate to Checkbox Demo page
driver.get("https://www.lambdatest.com/selenium-playground/checkbox-demo")

driver.find_element(
    By.XPATH,
    "//label[text()='Option 1']"
)
print("Located using XPath text()")

driver.find_elements(
    By.XPATH,
    "//label[contains(text(),'Option')]"
)
print("Located using XPath contains()")

"""
Locator Preference (Best → Worst)

1. ID
2. NAME
3. CSS Selector
4. Relative XPath
5. CLASS_NAME
6. Absolute XPath

Reason:
- ID is unique and fastest.
- CSS selectors are efficient and readable.
- Relative XPath is flexible.
- CLASS_NAME may not be unique.
- Absolute XPath is fragile because any HTML structure change can break it.
"""

driver.quit()

