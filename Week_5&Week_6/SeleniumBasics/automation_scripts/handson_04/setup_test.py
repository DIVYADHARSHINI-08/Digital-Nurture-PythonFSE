"""
Hands-On 4 – Selenium Architecture

1. WebDriver
- Selenium WebDriver is an API used to automate web browsers.
- It communicates with the browser through the browser driver (ChromeDriver).

2. Selenium Grid
- Selenium Grid allows tests to run in parallel on multiple browsers and machines.
- It is mainly used for cross-browser and distributed testing.

3. Selenium IDE
- Selenium IDE is a browser extension used for Record and Playback.
- It can also generate Selenium automation scripts.
"""
"""
Hands-On 4 – Selenium Architecture

1. WebDriver
- Selenium WebDriver automates browsers by communicating with the browser driver.

2. Selenium Grid
- Executes tests in parallel on multiple browsers and machines.

3. Selenium IDE
- Browser extension used for record-and-playback and code generation.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# Implicit wait applies globally to all element searches.
# It waits up to 10 seconds for every element lookup.
# This can slow down execution because every find_element call uses the same timeout.
# Explicit waits are preferred because they wait only for specific elements when needed.

driver.implicitly_wait(10)

driver.get("https://www.lambdatest.com/selenium-playground/")

print("Page Title:", driver.title)

driver.quit()

"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://www.lambdatest.com/selenium-playground/")

print(driver.title)

driver.quit()
"""



