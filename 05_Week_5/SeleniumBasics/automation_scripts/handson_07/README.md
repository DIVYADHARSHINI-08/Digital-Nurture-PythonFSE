# Hands-On 7: Page Object Model (POM) Design Pattern

## Objective

The objective of this hands-on exercise is to implement the Page Object Model (POM) design pattern using Selenium and Pytest. This exercise focuses on creating reusable page classes, separating test logic from UI element locators, and improving the maintainability and scalability of automation scripts.

---

## Topics Covered

- Page Object Model (POM)
- Base Page Design
- Page Classes
- Selenium WebDriver
- Pytest Integration
- Test Automation Best Practices
- Code Reusability
- Maintainable Test Framework

---

## Tasks Completed

- Created a reusable `BasePage` class for common browser operations.
- Developed individual page classes for:
  - Simple Form Demo
  - Checkbox Demo
  - Select Dropdown List
  - Input Form Submit
- Moved all web element locators into page object classes.
- Implemented reusable methods for interacting with web elements.
- Wrote Pytest test cases using page object methods.
- Eliminated direct `driver.find_element()` calls from test files.
- Executed all test cases successfully.
- Verified the implementation of the Page Object Model design pattern.

---

## Project Structure

```text
Handson_07/
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── simple_form_page.py
│   ├── checkbox_page.py
│   ├── dropdown_page.py
│   └── input_form_page.py
│
├── tests/
│   ├── conftest.py
│   └── test_playground.py
│
├── reports/
│   └── report.html
│
├── screenshots/
│
├── requirements.txt
└── README.md
```

---

## Learning Outcomes

After completing this hands-on, I was able to:

- Implement the Page Object Model (POM) architecture.
- Separate UI locators from test logic.
- Create reusable page classes for different web pages.
- Improve the readability and maintainability of Selenium test scripts.
- Write cleaner and more scalable Pytest test cases.
- Reuse common browser actions through a Base Page class.
- Execute automation tests with improved code organization.

---

## Technologies Used

- Python
- Selenium WebDriver
- Pytest
- ChromeDriver
- WebDriver Manager
- pytest-html
- LambdaTest Selenium Playground

---

## Maintenance Benefit of Page Object Model

The Page Object Model (POM) separates web element locators and page-specific actions from the test scripts. This makes the automation framework easier to maintain because changes to the application's user interface require updates only in the corresponding page object, while the test cases remain unchanged. POM also improves code reusability, readability, and scalability for larger automation projects.

---

## Expected Outcome

- All test cases executed successfully (**6/6 tests passed**).
- No direct `driver.find_element()` calls in the test files.
- Test logic was completely separated from page locators using the Page Object Model.
- HTML report generated successfully.

---

## Conclusion

This hands-on provided practical experience in implementing the Page Object Model (POM), a widely used design pattern in Selenium automation. By organizing locators and actions into dedicated page classes, the framework became more maintainable, reusable, and scalable. The successful execution of all test cases demonstrated the effectiveness of the POM approach in building robust automation frameworks.