					NITK Website

Project Structure:

/NITK_Site_venv (Virtual environment for project)
	|
	|-------/Lib(contains all the packages required for project)
	|-------/NITK (NITK Website App)
	|		|----/Migrations (Contains all the database migrations created)
	|		|----/static (Contains all the Static file (css, img) used in project)
	|		|-----/templates (Contains all the HTML files(UI) used fr rendering)
	|		|-----admin.py (Admin.py file is used for registering the Django models into the Django administration.)
	|		|-----Apps.py(Apps.py is a file that is used to help the user include the application configuration for their app.)
	|		|-----Models.py (Represents the models of web applications in the form of classes.)
	|		|-----Views.py (It contains all the views in the form of classes.)
	|		|-----forms.py(It contains all the forms used in the form of classes.)
	|-------/NITK_Site (Main Project)
	|		|-----settings.py (It contains the Django project configuration.)
	|		|-----url.py (URL is a universal resource locator, it contains all the endpoints that we should have for our website.)
	|		|-----wsgi.py (WSGI stands for Web Server Gateway Interface, it describes the way how servers interact with the applications.)
	|		|-----asgi.py (ASGI works similar to WSGI but comes with some additional functionality.)
	|-------Scripts (Scripts for virtual environment)
	|-------db.sqlite3 (Project Database)
	|-------manage.py (Command line utility for project)
	|-------pyvenv.cfg (Configuration File for Virtual environment)
	|-------readme.txt (This file)


Technlogies Used:

Front-end: HTML5, CSS, Javascript, Bootstrap.
Back-end: Django framework, SQLite3 Database.

Site Architecture:

|--Home
	|--Administration
	|	|--Director
	|	|--Heads Of Department
	|	|--Organisation Chart
	|--Academics
	|	|--Academic Office
	|	|--Programme
	|	|--UG Programme
	|	|--PG Programme
	|	|--Academic Calender
	|	|--Departments
	|	|--Fee Structure
	|--For Student
	|	|--UG & PG Time-Table
	|	|--UG & PG Syallabus
	|	|--Registration
	|	|--Login
	|--Career
	|	|--Teaching Positions
	|	|--Non Teaching Positions
	|--For Faculty
	|	|--Login




Workflow:

1)Student Workflow:
		-First Student will register on site.
		-After registration will be redirected to its homepage.
		-If subject registration is not done, a form will be shown to register subjects.
		-On Homepage details like semester,cgpa,credits,registered subjects will be shown.
		-News/Placement news will be shown as updated.

2)Faculty Workflow:
		-Faculty will login through credentials.
		-On landing page, News/ Placement activites can be updated.
		-Student data can be deleted, data can be updated.

3)Career Workflow:
		-Application for Teaching positions can be filled.
		-Application for Non-Teaching positions can be filled.