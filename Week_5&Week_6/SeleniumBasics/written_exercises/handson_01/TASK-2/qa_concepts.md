# Task 2: Defect Lifecycle & Severity Classification

## 5. Defect Lifecycle

The Defect Lifecycle describes the different stages a defect goes through from the time it is reported until it is closed.

```
New
 ↓
Assigned
 ↓
Open
 ↓
Fixed
 ↓
Retest
 ↓
Verified
 ↓
Closed
```

### Defect States

**1. New**
- A QA tester identifies a defect and reports it in the defect tracking tool.

**2. Assigned**
- The defect is assigned to a developer for analysis and fixing.

**3. Open**
- The developer reviews the defect and starts working on it.

**4. Fixed**
- The developer fixes the defect and marks it as fixed.

**5. Retest**
- The QA tester retests the application to verify the fix.

**6. Verified**
- The QA tester confirms that the defect has been fixed successfully.

**7. Closed**
- The defect is closed because it has been resolved successfully.

### Alternative Paths

### Rejected
The developer rejects the defect because:
- It is not a bug.
- It cannot be reproduced.
- It is working as designed.
- It is a duplicate defect.

### Deferred
The defect is acknowledged but postponed to a future release because:
- It has low business impact.
- There are higher-priority defects to fix.
- The fix requires significant effort.

---

# 6. Severity and Priority Classification

| Bug | Severity | Priority | Justification |
|------|----------|----------|---------------|
| **a)** POST `/api/courses` returns **500 Internal Server Error** for all requests. | **Critical** | **P1** | The API is completely unusable. No user can create a course, so it must be fixed immediately. |
| **b)** Course names longer than 150 characters are silently truncated without an error. | **Medium** | **P3** | The application still works, but data is modified unexpectedly. It should be fixed, but it is not an emergency. |
| **c)** Swagger `/docs` page contains a typo in the API description. | **Low** | **P4** | This is only a documentation issue and does not affect application functionality. |
| **d)** Login occasionally returns **401 Unauthorized** even with correct credentials (intermittent). | **High** | **P1** | Users may be unable to log in randomly. Since the issue is intermittent and affects authentication, it requires immediate attention. |

---

# 7. Defect Report

**Defect ID:** DEF-001

**Title:** POST /api/courses returns 500 Internal Server Error for all requests

**Environment:**
- Windows 11
- Google Chrome 138
- Course Management API (Local Environment)

**Build Version:**
v1.0.0

**Severity:**
Critical

**Priority:**
P1 (Highest)

**Steps to Reproduce:**
1. Start the Course Management API.
2. Open Postman or any API testing tool.
3. Send a POST request to `/api/courses` with valid course details.
4. Click **Send**.

**Expected Result:**
The API should create the course successfully and return **HTTP Status Code 201 (Created).**

**Actual Result:**
The API returns **HTTP Status Code 500 (Internal Server Error)** and the course is not created.

**Attachments:**
Screenshot of **500 Internal Server Error**.

---

# 8. Difference Between Severity and Priority

| Severity | Priority |
|-----------|----------|
| Measures how much the defect affects the system. | Measures how urgently the defect should be fixed. |
| Decided mainly by QA. | Decided mainly by the Product Owner, Project Manager, or Business Team. |

### Example

A typo in the CEO's dashboard:

Instead of:

```
Welcome
```

it displays:

```
Welocme
```

- **Severity:** Low (the system still works correctly)
- **Priority:** High (P1) because the CEO will see it during an important presentation, so it should be fixed immediately.

This is an example where **High Priority does not mean High Severity**.