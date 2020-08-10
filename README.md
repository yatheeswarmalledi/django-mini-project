# django-mini-project

# Description:
This is a mini project to demonstrate functionality between django and rest framework.  
The website is hosted on "http://yatheeswar.pythonanywhere.com"

# Instructions for using the code:
- Download the code and extract the zip file or clone directly using git command line tool.
- Open command prompt.
- Create a virtual environment (optional but recommended).
- Download python(>=3.6) from https://www.python.org/downloads/ and install it.
- Install django, djangorestframework, factory_boy using below commands:  
	`pip install django`  
	`pip install djangorestframework`  
	`pip install factory_boy`  

- Navigate to 'django-mini-project/mysite/settings.py' file and add your own 'SECRET_KEY'. Also set 'DEBUG' to True.
- From command prompt, navigate to the project directory directory: 'django-mini-project/mysite/'
- Run migrations using below commands:  
	`python manage.py makemigrations`  
	`python manage.py migrate`  
- To populate database with dummy data, run this command: 
	`python manage.py mycommand`  
	(type `python manage.py mycommand --help` for argument usage details)
- Finally, to run the server:   
	`python manage.py runserver`  

- Head over to the link (http://127.0.0.1:8000). You can see the GET request.
- Click on "http://127.0.0.1:8000/MyUser/" for displaying the data in json format.

Thank you.
