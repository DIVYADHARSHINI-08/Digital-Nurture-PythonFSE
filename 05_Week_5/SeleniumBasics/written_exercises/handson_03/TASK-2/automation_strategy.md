# Task 2: Compare Automation Framework Types

## 21. Comparison of Automation Framework Types

### 1. Linear Framework

**Description:**
The Linear Framework, also known as the Record-and-Playback Framework, is the simplest automation framework. Test scripts are written sequentially, where each step is executed one after another without reusing code or separating test data. It is suitable for small and simple projects.

**Advantage:**
- Easy to create and understand.

**Disadvantage:**
- Difficult to maintain as the project grows because code is duplicated.

**Example (Course Management System):**
Automating a simple login test where the script performs the login process from start to finish without using reusable functions.

---

### 2. Modular Framework

**Description:**
The Modular Framework divides the application into independent modules such as Login, Course Management, and Student Management. Each module has its own reusable test scripts, making the framework easier to maintain.

**Advantage:**
- Promotes code reusability and simplifies maintenance.

**Disadvantage:**
- Requires more planning during the initial development stage.

**Example (Course Management System):**
Create separate modules for Login, Add Course, Update Course, and Delete Course so that each module can be reused in multiple test cases.

---

### 3. Data-Driven Framework

**Description:**
In a Data-Driven Framework, test data is stored separately in files such as Excel, CSV, or JSON. The same automation script executes multiple times using different input values.

**Advantage:**
- One script can test many different datasets.

**Disadvantage:**
- Managing external test data files increases complexity.

**Example (Course Management System):**
Execute the login test using 50 different username and password combinations stored in an Excel file.

---

### 4. Keyword-Driven Framework

**Description:**
The Keyword-Driven Framework uses predefined keywords such as Login, Click, EnterText, and Submit to perform test actions. Test cases are created using these keywords instead of writing code, making them easier for non-technical users.

**Advantage:**
- Allows non-technical team members to create and understand test cases.

**Disadvantage:**
- Framework design and maintenance can be complex.

**Example (Course Management System):**
Use keywords like Login, AddCourse, Save, and Logout to create automation scenarios without directly writing Selenium code.

---

### 5. Hybrid Framework

**Description:**
The Hybrid Framework combines the features of Modular, Data-Driven, and Keyword-Driven frameworks. It provides reusable modules, supports external test data, and can also use keywords for easier test creation. This is the most commonly used framework in real-world Selenium projects.

**Advantage:**
- Highly flexible, reusable, scalable, and easy to maintain.

**Disadvantage:**
- More complex to design and implement initially.

**Example (Course Management System):**
Use reusable page modules, execute tests with multiple datasets, and allow both technical and non-technical team members to contribute to test creation.

---

## 22. Recommended Framework

For the Course Management frontend, I recommend using a **Hybrid Framework** that combines the **Modular**, **Data-Driven**, and **Keyword-Driven** frameworks.

### Justification

- **Data-Driven Framework** allows the login functionality to be tested with **50 different username and password combinations** using external data files.
- **Modular Framework** enables the login functionality to be reused across **20 different test cases**, reducing duplicate code.
- **Keyword-Driven Framework** allows non-technical team members to write or understand test cases using predefined keywords instead of Selenium code.
- The **Hybrid Framework** combines all these advantages, making it scalable, maintainable, and suitable for large Selenium automation projects.

---

## 23. Hybrid Framework Folder Structure

```text
CourseManagementAutomation/
│
├── config/
│   └── config.py
│
├── test_data/
│   ├── login_data.xlsx
│   ├── course_data.csv
│   └── student_data.json
│
├── pages/
│   ├── login_page.py
│   ├── course_page.py
│   ├── student_page.py
│   └── base_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_courses.py
│   └── test_students.py
│
├── utilities/
│   ├── browser_setup.py
│   ├── logger.py
│   ├── screenshots.py
│   └── helpers.py
│
├── reports/
│
├── screenshots/
│
├── requirements.txt
│
└── README.md
```

### Folder Description

| Folder/File | Purpose |
|--------------|---------|
| **config/** | Stores application configuration such as URLs, browser settings, and environment details. |
| **test_data/** | Contains external test data files (Excel, CSV, JSON) used for data-driven testing. |
| **pages/** | Implements the Page Object Model (POM), where each page contains its locators and methods. |
| **tests/** | Contains Selenium test scripts for different application features. |
| **utilities/** | Includes reusable helper functions such as browser setup, logging, screenshots, and utility methods. |
| **reports/** | Stores HTML or other test execution reports. |
| **screenshots/** | Stores screenshots captured during test failures. |
| **requirements.txt** | Lists all Python package dependencies required for the project. |
| **README.md** | Provides project documentation and setup instructions. |