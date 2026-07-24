# Hands-On 1 - QA Concepts, Functional Testing & Defect Lifecycle

## Task 1: Testing Types for Course Management API

### 1. Unit Testing

**Test Case:**
Verify that the `add_course()` function returns a success response when valid course details are provided.

**Description:**
The function is tested independently without involving the API endpoint or the database.

**Classification:** Functional Testing

---

### 2. Integration Testing

**Test Case:**
Verify that the `POST /api/courses` API endpoint successfully stores the course details in the database.

**Description:**
Send a valid request to create a course and verify that:
- The API returns **HTTP Status Code 201 (Created)**.
- The course is stored correctly in the database.

**Classification:** Functional Testing

---

### 3. System Testing

**Test Case:**
Verify the complete course management workflow from API request to database response.

**Description:**
Perform the following operations:
1. Create a new course.
2. Retrieve the created course.
3. Update the course details.
4. Delete the course.

Verify that every operation completes successfully and the expected results are returned.

**Classification:** Functional Testing

---

### 4. User Acceptance Testing (UAT)

**Test Case:**
Verify that a college administrator can successfully manage courses using the Course Management API.

**Description:**
The college administrator should be able to:
- Create a course
- View course details
- Update course information
- Delete a course

The system should satisfy the business requirements of course management.

**Classification:** Functional Testing

---

## Task 2: Functional vs Non-Functional Testing

### Classification

| Testing Type | Functional / Non-Functional |
|--------------|-----------------------------|
| Unit Testing | Functional |
| Integration Testing | Functional |
| System Testing | Functional |
| User Acceptance Testing | Functional |

### Non-Functional Test Example

**Performance Testing**

Verify that the `POST /api/courses` endpoint can process **1000 course creation requests within 5 seconds** while maintaining acceptable response time and without server failures.

This is a **Non-Functional Test** because it measures **how well** the API performs under load rather than checking whether it functions correctly.

---

## Task 3: Black-Box Testing vs White-Box Testing

### Black-Box Testing

Black-Box Testing is a testing technique where the tester validates the application's functionality **without knowing the internal source code**. The tester focuses only on inputs and expected outputs.

**Performed by:** QA/Test Engineers

### White-Box Testing

White-Box Testing is a testing technique where the tester has knowledge of the application's internal code, logic, and structure. Individual methods, conditions, and code paths are tested.

**Performed by:** Developers

### Difference

| Black-Box Testing | White-Box Testing |
|-------------------|-------------------|
| No knowledge of source code | Knowledge of source code is required |
| Tests functionality | Tests internal logic |
| Focuses on inputs and outputs | Focuses on code structure |
| Performed mainly by QA/Testers | Performed mainly by Developers |

---

## Task 4: Formal Test Cases for POST /api/courses

| Test Case ID | Description | Preconditions | Test Steps | Expected Result | Actual Result | Pass/Fail |
|--------------|-------------|---------------|------------|-----------------|---------------|-----------|
| TC_001 | Create a course with valid details | API is running | 1. Send POST request with valid course name and course code.<br>2. Submit the request. | HTTP 201 Created is returned and the course is stored successfully. | | |
| TC_002 | Create a course with missing required field | API is running | 1. Send POST request without Course Name.<br>2. Submit the request. | HTTP 400 Bad Request is returned with an appropriate validation error message. | | |
| TC_003 | Create a course with duplicate course code | API is running and the course code already exists | 1. Send POST request using an existing course code.<br>2. Submit the request. | HTTP 409 Conflict (or appropriate duplicate error) is returned and the duplicate course is not created. | | |
