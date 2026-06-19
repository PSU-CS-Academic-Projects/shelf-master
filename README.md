# Shelf Master Library System

## Project Information

## Project Category
 Web Systems

### Members:
 * Vincent Mago
 * John Carlo Dagoy
 * Mark Jayson Galarpe

## Academic Year
 2025-2026

## Instructor
 Ma'am Divine Caabay

## Project Description
  Shelf Master is a library system made tracking of the borrowed books easier.

## Features
 * Secured User Authentication
 * Modern Analytics Dashboard with Chart
 * Automated Overdue Notification
 * Member History Tracker

## Technologies Used
 * Python
 * Django
 * Faker
 * SQlite
 * Pillow
 * HTML5/CSS3
 * JavaScript
 * Chart.js

## Installation Guide:
 - Clone Repository or navigate to project site
  cd project

 - activate project
  project/script/.activate

 - navigate to cloned repository
  cd library-system/projectsite

 - install environment dependencies
  pip install -r requirements.txt

 - run missing core database migrations if applicable
  python manage.py migrate

 - Create a Superuser account for you to log in
  python manage.py createsuperuser

 - run server
 python manage.py runserver 8080

 - access dashboard after loggin in

### Video Demo
 https://drive.google.com/drive/folders/1koy0HBHjiX0gYPEnScj5W7YxiISHcJJb?usp=sharing

## Screenshots

#### Login Page
![Login Page](screenshots/login.png)

#### Dashboard Overview
![Dashboard Overview](screenshots/overview.png)

#### Books Collection
![Books Collection](screenshots/books.png)

#### Book Management Panel
![Book Management Panel](screenshots/book%20management.png)

#### Borrowings Log
![Borrowings Log](screenshots/borrowings.png)

#### Members Directory
![Members Directory](screenshots/members.png)

#### Member Profile Example
![Member Profile Example](screenshots/member%20example.png)

## Future Improvements
* Integrating Barcode Scanners
* Real-time automated emails for overdue borrowers
* Support for digital book reservations and queues
* Online payment for membership
