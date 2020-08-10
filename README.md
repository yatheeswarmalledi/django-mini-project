# django-mini-project

- Extract the zip file.
- Open command prompt.
- Download python(>=3.6) from https://www.python.org/downloads/ and install it. 
- Install django, djangorestframework, factory_boy using below commands:
	pip install django
	pip install djangorestframework
	pip install factory_boy
  
- If you are downloading the code from Github, kindly edit your secret key in the settings file before using the code and have a look at Debug selection.
- Navigate to the project directory directory: 'mysite/' 
- Run migrations using below commands: 
	python manage.py makemigrations
	python manage.py migrate
		
- To populate database with dummy data, run this command:
	python manage.py mycommand
	(type python manage.py mycommand --help for usage details)
  
- The server is hosted on " http://yatheeswar.pythonanywhere.com ", so please visit the site after starting the migrations.

- If you are running on Local server, please check Debug settings before running.
- Finally, to run the server:
	python manage.py runserver
		
- Head over to the link (127.0.0.1:8000). You can see the GET request
- Click on "http://127.0.0.1:8000/MyUser/" for displaying the data in json format. 

Thank you.
