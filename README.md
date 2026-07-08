=========================================================
Little Lemon Back-End Capstone Project
=========================================================

This project was developed as the final Back-End Developer Capstone Project
for the Meta Back-End Developer Professional Certificate.

Technologies Used
-----------------
- Python
- Django
- Django REST Framework
- MySQL
- Djoser Authentication
- Token Authentication
- Git & GitHub

=========================================================
Project Features
=========================================================

- Django serves static HTML content
- MySQL database integration
- Menu API
- Table Booking API
- User Registration
- Token Authentication
- Unit Tests
- API testing using Insomnia/Postman/cURL

=========================================================
How to Run This Project
=========================================================

1. Clone the repository

git clone <YOUR_GITHUB_REPOSITORY_URL>

2. Move into the project directory

cd meta-backend-capstone

3. Open the Django project

cd LittleLemon

4. Create a virtual environment

Windows:

python -m venv venv
venv\Scripts\activate

Linux / macOS:

python3 -m venv venv
source venv/bin/activate

5. Install project dependencies

If using Pipenv:

pipenv install
pipenv shell

OR

pip install -r requirements.txt

6. Configure the MySQL database

Create a MySQL database.

Example:

Database Name:
littlelemon

Update DATABASES inside settings.py with your own MySQL credentials.

7. Apply database migrations

python manage.py makemigrations
python manage.py migrate

8. Create a superuser

python manage.py createsuperuser

9. Run the unit tests

python manage.py test

10. Start the development server

python manage.py runserver

Open your browser:

http://127.0.0.1:8000/

=========================================================
API Endpoints
=========================================================

Static HTML

/

---------------------------------------------------------

Menu API

GET     /api/menu/
POST    /api/menu/
GET     /api/menu/<id>/
PUT     /api/menu/<id>/
DELETE  /api/menu/<id>/

---------------------------------------------------------

Booking API

GET     /api/bookings/
POST    /api/bookings/
GET     /api/bookings/<id>/
PUT     /api/bookings/<id>/
DELETE  /api/bookings/<id>/

---------------------------------------------------------

Authentication

POST    /api/registration/
POST    /api/token/login/
POST    /api/token/logout/

=========================================================
Testing the API
=========================================================

The API can be tested using:

- Insomnia
- Postman
- cURL

For protected endpoints:

1. Register a user
2. Login using:

POST /api/token/login/

3. Copy the generated token.

4. Add the following header to authenticated requests:

Authorization: Token <your_token>

=========================================================
Peer Review Checklist
=========================================================

✔ Django serves static HTML content

✔ Project is committed to GitHub

✔ MySQL database is configured

✔ Menu API implemented

✔ Booking API implemented

✔ User registration implemented

✔ Token authentication implemented

✔ Unit tests included

✔ API can be tested using Insomnia

=========================================================
End of Readme
=========================================================