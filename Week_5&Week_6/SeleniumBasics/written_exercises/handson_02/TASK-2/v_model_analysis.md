# Task 2: Agile QA and Shift-Left Testing

## 13. Problems with Waterfall Testing

In the traditional Waterfall model, testing begins only after the development phase is completed. This creates several challenges for the Course Management API project.

### Problem 1: Late Detection of Defects

Bugs are identified only after all coding is finished. Fixing defects at this stage is expensive and time-consuming.

**Example:**
If the `POST /api/courses` endpoint stores incorrect data in the database, the issue may only be discovered after the entire API has been developed.

---

### Problem 2: Increased Development Cost

Changes made after development require developers to modify code, database design, and API logic, increasing both cost and effort.

**Example:**
If the college decides that the **Course Code** must be unique after development is complete, major changes will be required.

---

### Problem 3: Delayed Product Delivery

If many defects are found during testing, the release is delayed because developers must fix bugs and QA must retest the application.

**Example:**
Multiple API endpoints fail during system testing, delaying the deployment of the Course Management API.

---

# 14. QA Role in Agile Ceremonies

| Agile Ceremony | QA Responsibilities |
|----------------|---------------------|
| **Sprint Planning** | Reviews user stories, defines acceptance criteria, estimates testing effort, identifies test scenarios. |
| **Daily Stand-up** | Shares testing progress, reports blocked issues, discusses defects, and coordinates with developers. |
| **Sprint Review** | Demonstrates completed features, validates acceptance criteria, verifies user stories, and confirms completed functionality. |
| **Retrospective** | Discusses what went well, identifies process improvements, suggests better testing practices, and helps improve future sprints. |

---

# 15. Shift-Left Testing Practices

Shift-Left Testing means testing activities begin as early as possible in the Software Development Life Cycle (SDLC). This helps prevent defects instead of finding them later.

### a) Review Requirements for Testability

QA reviews the Software Requirement Specification (SRS) before development begins to ensure all requirements are clear, complete, and testable.

**Course Management API Example:**
QA confirms that mandatory fields such as **Course Name** and **Course Code** are clearly specified.

---

### b) Write Test Cases Before Coding (TDD / BDD)

QA prepares test cases or acceptance criteria before developers start coding.

**Course Management API Example:**
QA writes test cases for the `POST /api/courses` endpoint before the API is implemented.

---

### c) Static Code Analysis

Developers use static analysis tools to detect coding issues, security vulnerabilities, and coding standard violations before executing the application.

**Course Management API Example:**
Run static analysis tools to identify potential coding errors in the API source code before deployment.

---

### d) API Contract Testing Before Integration

Verify that the API request and response formats follow the agreed API specification before integrating with other components.

**Course Management API Example:**
Ensure the `POST /api/courses` endpoint accepts the required JSON fields and returns the correct HTTP status codes before frontend integration.

---

# 16. Acceptance Criteria (Given-When-Then)

## Scenario 1: Happy Path

**Given** the college administrator is authenticated

**When** the administrator submits valid course details

**Then** the course should be created successfully and the API should return **HTTP 201 Created**.

---

## Scenario 2: Duplicate Course Code

**Given** a course with the same course code already exists

**When** the administrator attempts to create another course using that course code

**Then** the API should reject the request and return an appropriate error message (e.g., **HTTP 409 Conflict**).

---

## Scenario 3: Missing Required Fields

**Given** the administrator submits a request with missing mandatory fields

**When** the request is sent to the API

**Then** the API should return **HTTP 400 Bad Request** with validation error messages indicating the missing fields.

---

# Summary

In Agile, QA actively participates throughout every sprint instead of waiting until development is complete. Shift-Left Testing encourages early collaboration between developers and QA through requirement reviews, early test design, static code analysis, and API contract testing. This approach reduces defects, lowers development costs, and improves software quality.