"""
Task 1 - Web Framework Notes

1. Request-Response Cycle

Browser
   |
   | HTTP GET /api/courses/
   v
URL Router (urls.py)
   |
   v
View (views.py)
   |
   v
Model (models.py)
   |
Database Query
   |
   v
View receives data
   |
   v
HttpResponse / JSON Response
   |
Browser


2. Middleware

Middleware sits between the request and the view.

Request
    |
Middleware
    |
View
    |
Middleware
    |
Response

Examples:

AuthenticationMiddleware
- Identifies the logged-in user.

SessionMiddleware
- Enables session support.


3. WSGI vs ASGI

WSGI
- Handles synchronous requests.
- Suitable for traditional web applications.
- Django uses WSGI by default.

ASGI
- Supports asynchronous programming.
- Handles WebSockets and long-lived connections.
- Better for real-time applications like chat apps.
- Switch to ASGI when async support is needed.


4. MVC vs Django MVT

MVC

Model
View
Controller

Django MVT

Model -> Model
View (MVC) -> Template
Controller (MVC) -> Django View

Django View acts as the Controller.
Template acts as the View.
Model remains the Model.
"""