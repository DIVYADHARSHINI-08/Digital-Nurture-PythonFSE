# Hands-On 2 - SDLC vs TDLC (V-Model & Agile QA Integration)

# Task 1: V-Model Mapping

## 9. V-Model Diagram

```
                 SDLC (Development)

              Requirements
                   │
                   ▼
             System Design
                   │
                   ▼
          Architecture Design
                   │
                   ▼
             Module Design
                   │
                   ▼
                 Coding
                   ▲
                   │
             Unit Testing
                   ▲
                   │
         Integration Testing
                   ▲
                   │
            System Testing
                   ▲
                   │
         Acceptance Testing

              TDLC (Testing)
```

### SDLC ↔ TDLC Mapping

| SDLC Phase | Corresponding TDLC Phase |
|------------|--------------------------|
| Requirements | Acceptance Testing |
| System Design | System Testing |
| Architecture Design | Integration Testing |
| Module Design | Unit Testing |
| Coding | Execution of all tests |

---

# 10. Test Artifacts Produced During Development

| SDLC Phase | Test Artifact Produced |
|------------|------------------------|
| Requirements | Acceptance Test Plan and Acceptance Test Cases |
| System Design | System Test Plan and System Test Cases |
| Architecture Design | Integration Test Plan and Integration Test Cases |
| Module Design | Unit Test Cases and Unit Test Plan |
| Coding | Source Code and Executable Application |

---

# 11. Entry Criteria and Exit Criteria

## Unit Testing

### Entry Criteria
- Module development is completed.
- Unit test cases are prepared.
- Development environment is ready.

### Exit Criteria
- All unit test cases are executed.
- All critical defects are fixed.
- Unit test results are documented.

---

## Integration Testing

### Entry Criteria
- Individual modules have passed unit testing.
- Modules are integrated.
- Integration test cases are ready.

### Exit Criteria
- All integration test cases are executed.
- Interfaces between modules work correctly.
- No critical integration defects remain.

---

## System Testing

### Entry Criteria
- Complete application is available.
- System test cases are prepared.
- Test environment is ready.

### Exit Criteria
- All planned system test cases are executed.
- No Critical or High severity defects remain.
- Application satisfies functional and non-functional requirements.

---

## Acceptance Testing

### Entry Criteria
- System testing is completed successfully.
- Business requirements are finalized.
- Acceptance test cases are prepared.

### Exit Criteria
- Customer validates the application.
- Business requirements are satisfied.
- Customer approves the software for deployment.

---

# 12. QA Engagement in the V-Model

QA should be involved before the testing phase to improve software quality.

### 1. Requirements Review

During the Requirements phase, QA:
- Reviews the Software Requirement Specification (SRS).
- Identifies missing, ambiguous, or conflicting requirements.
- Ensures requirements are testable.
- Prepares Acceptance Test Cases.

**Example (Course Management API):**
QA verifies that the requirement clearly specifies mandatory fields such as Course Name and Course Code.

---

### 2. Design Review

During the System Design/Architecture Design phase, QA:
- Reviews the application design.
- Identifies potential testing risks.
- Plans Integration and System Test Cases.
- Reviews API endpoints and database design.

**Example (Course Management API):**
QA verifies that the API endpoints, request format, response codes, and database relationships are clearly defined before development begins.

---

# Summary

The V-Model connects each development phase with its corresponding testing phase. QA participates not only during testing but also during requirements and design reviews to detect defects early, reducing cost and improving software quality.