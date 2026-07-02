# Course Management Microservices

| Service              | Responsibility                  | Endpoints          | Database         |
|----------------------|---------------------------------|--------------------|------------------|
| Course Service       | Manage departments and courses  | /api/courses       | courses.db       |
| Student Service      | Manage students and enrollments | /api/students      | students.db      |
| Auth Service         | Register users, login, JWT      | /api/auth          | auth.db          |
| Notification Service | Send email confirmations        | /api/notifications | notifications.db |

## Natural Decomposition

- Course Service
    - Course CRUD
    - Department CRUD

- Student Service
    - Student CRUD
    - Enrollment

- Auth Service
    - Register
    - Login
    - JWT Validation

- Notification Service
    - Email confirmations

## Synchronous vs Asynchronous Communication

### Synchronous (HTTP)

- Request waits for another service to respond.
- Simple to implement and easy to understand.
- Services are tightly coupled.
- If one service is unavailable, dependent requests fail.

### Asynchronous (RabbitMQ/Kafka)

- Services communicate through a message queue.
- Loosely coupled and more resilient.
- Better for high scalability and background processing.
- Supports eventual consistency.
- Common use cases: email notifications, logging, order processing, and event-driven workflows.