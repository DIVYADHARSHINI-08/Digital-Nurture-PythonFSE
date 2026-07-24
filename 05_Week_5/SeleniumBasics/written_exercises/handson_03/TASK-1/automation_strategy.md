# Hands-On 3 – Test Automation Process, Lifecycle & Framework Types

# Task 1: Automation Decision and Test Case Selection

## 17. Criteria for Deciding Whether to Automate a Test Case

### 1. Repetitive Execution
**Explanation:** Test cases that are executed frequently should be automated to save time and reduce manual effort.

**Application to the Scenario:**
The `POST /api/courses` endpoint is tested after every code change. Automating this test ensures consistent validation without repeated manual work.

---

### 2. Regression Testing
**Explanation:** Test cases that verify existing functionality after code changes are good candidates for automation.

**Application to the Scenario:**
Whenever new features are added, the automated test verifies that the `POST /api/courses` endpoint still returns **HTTP 201 Created** with the correct course data.

---

### 3. High Business Impact
**Explanation:** Features that are critical to business operations should be automated to ensure reliability.

**Application to the Scenario:**
Creating a course is a core feature of the Course Management API. If this functionality fails, administrators cannot add new courses, making it a high-priority candidate for automation.

---

### 4. Stable Functionality
**Explanation:** Features that rarely change are easier to automate and maintain.

**Application to the Scenario:**
The `POST /api/courses` endpoint has a stable API structure and is unlikely to change frequently, making it suitable for automation.

---

### 5. Data-Driven Testing
**Explanation:** Test cases that require multiple sets of input data can be efficiently automated.

**Application to the Scenario:**
The same test can be executed with different course names, course codes, and descriptions using multiple datasets to verify the API under various conditions.

---

# 18. Automate or Manual

| Test Case | Decision | Justification |
|------------|-----------|---------------|
| **a) Regression test for all CRUD endpoints after every code change** | **Automate** | Regression tests are repetitive and need to be executed after every code update. Automation saves time and ensures consistency. |
| **b) Exploratory testing of a new search feature** | **Manual** | Exploratory testing requires human observation, creativity, and analysis to discover unexpected defects. |
| **c) Performance test: 100 concurrent users calling GET /api/courses/** | **Automate** | Performance testing requires simulating many users simultaneously, which is only practical using automation tools. |
| **d) UI test for the login form** | **Automate** | Login functionality is frequently tested and is a stable feature, making it suitable for automation. |
| **e) Verify the API documentation (Swagger) is accurate** | **Manual** | Documentation should be manually reviewed to ensure descriptions and examples are clear and accurate. |
| **f) Smoke test: Verify the API is reachable after deployment** | **Automate** | Smoke tests are performed after every deployment, so automating them provides quick feedback on application availability. |

---

# 19. Test Automation ROI

### Definition

**Test Automation ROI (Return on Investment)** measures whether the benefits of automating a test outweigh the time and effort required to create and maintain the automated test.

### Calculation

- Time required to automate one regression test = **4 hours = 240 minutes**
- Manual execution time per run = **30 minutes**

**Break-even Point:**

```
240 ÷ 30 = 8 runs
```

Therefore, the automated test pays for itself after **8 executions**.

### Maintenance Overhead

After the **10th run**, each automated execution requires an additional **20% maintenance effort**.

```
20% of 30 minutes = 6 minutes
```

Effective execution effort after the 10th run:

```
30 + 6 = 36 minutes
```

Even with maintenance, automation continues to save significant time compared to repeated manual execution, especially over many test cycles.

---

# 20. Flaky Test

### Definition

A **flaky test** is a test that produces inconsistent results without any changes to the application. It may pass during one execution and fail during another under the same conditions.

### Example

A Selenium test attempts to click the **Submit** button immediately after the page loads.

- If the page loads quickly, the test passes.
- If the button has not yet become clickable, the test fails.

This inconsistent behavior makes it a flaky test.

### Strategies to Prevent or Fix Flaky Tests

1. **Use Explicit Waits**
   - Replace `time.sleep()` with `WebDriverWait` to wait until elements are visible or clickable.

2. **Use Stable Locators**
   - Prefer unique locators such as **ID** or **CSS Selectors** instead of fragile XPath expressions.

3. **Maintain a Stable Test Environment**
   - Ensure the application, test data, browser, and network environment remain consistent during test execution.