# Middleware - It sits between the web server and the view. It processes requests before they reach the view and responses before they leave the application.

# Two built-in Django Middleware:
# 1. Authentication Middleware (Allowing the view to know, who is making the request)
# 2.Common Middleware          (Handles URL rewriting and sets URL Standards)

# WSGI - Web Server Gateway Interface - Handles one request at a time per thread

# ASGI - Asynchronous Server Gateway Interface - Supports features like Websockets, long polling and HTTP/2

# ASGI is used when we handle real time features and handle high concurrency tasks

# MVC - Model View Controller separates data, logic and presentation
# Django - Model View Template 

# Mapping: MVC vs Django
# Model      - Model    (Defines the data structure and database interactions)
# View       - Template (Handles the UI/UX layer)
# Controller - View     (Contains the business logic and connects models and templates)


