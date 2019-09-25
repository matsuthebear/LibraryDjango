# LibraryDjango
A fully functional Django Project where users can look, buy and check orders


# Requirements
In order to use this project, you must have installed Python
(version 3 or above), pip and Django. You can use any OS you want that is
supported by Python.
To install the packages just type
```sh
pip install -r requirements.txt
```
# About the Project
"Library Django" was created for an university exam, in order to pass the  "Ingegneria del Software" course at the University of Verona, Italy.
Here some features:
- Users can read books' descriptions
- User can buy books and check their orders
- Each user (even admins) have a Book Card, where points are stored
- Admins can delete, create and manage users and their book points
This project is based entirely on Django (Python and Html) and it follows
the MVC (Model-View-Control) model

# The Software
The structure of the software can be complex for anyone who tries Django for the first time, but I will explain how it is constructed and how each part works.
There are 3 folders in the main dir:
- library
- Library_Exam
- users
- db.sqlite3
- manage.py
- README.md
- requirements
### Main Files
There are three files in the main directory:
- manage.py : must be used in order to run the server. Just type
  ```sh
  python manage.py runserver
  ```
  to launch the server and try to manage it by the browser
- db.sqlite3 : the database itself.
- requirements.txt : the packages that must
  be installed in order to run correctly Django

### library
The "library" folder contains all the information about the library itself( like
how many books there are, how much they cost, etc.) and all the main
templates used for the software. It contains:
 - media : all the images stored and used for the website
 - migrations : SQL like commands used. It contains all the edits
  made for the database
 - static : files that are shared in the framework. It stores CSS and Javascript, but
 you can always add some other CSS or info.
 - templates : HTML files
 - admin.py : used to include all models used in the admin page (a must to manage them from the admin page)
 - apps.py
 - models.py : every sql-table stored in the database must be written in this file.
 If you look it you will see how the objects have a similar composition to the SQL table
 - tests.py
 - urls.py : this file allows the framework to link
 a function to a specific url submitted. It allows also to use static images and files.
 - views.py : functions used by the framework. Every function can return a request
 to a specific html page.
### users
 The "users" folder contains all the information about the users ( profiles, passwords, points gained, orders, etc.) and all the main
 templates used for the software. It contains
  - migrations : SQL like commands used. It contains all the edits
   made for the database
  - templates : HTML files (login, logout, profile, register)
  - admin.py : used to include all models used in the admin page (a must to manage them from the admin page)
  - apps.py
  - forms.py : used to add information to user base model (only composed by username
    and password ) and to create custom forms with the add of crispy-forms (package)
  - models.py : every sql-table stored in the database must be written in this file.
  If you look it you will see how the objects have a similar composition to the SQL table
  - signals.py : used to create automatically something if a signal is received
  - tests.py
  - views.py : functions used by the framework. Every function can return a request
  to a specific html page.
### Library_Exam
- settings.py : necessary to manage specific parts of the framework (ex: packages used)
- urls.py : like the other urls
- wsgi.py : used for deployment. __I will not show how to deploy this software
  because I don't want to and there are guides online to how to__

# Special thanks
- I want to thank Corey for sharing his Django project. It helped me a lot in order to understand and write a powerful program in Django. [See his  Github](https://github.com/CoreyMSchafer/code_snippets/tree/master/Django_Blog)
