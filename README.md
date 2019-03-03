To run the server

1) If not created already, create virtual environment for python in directory where you clone this directory.
  `cd freedom-network`
  `python3 -m virtualenv ${name}`
2) Source virtualenv to start virtualenv 
  `source ${name}/bin/activate`
3) Install the packages that we need for the django project
 `pip3 install django`
 `pip3 install django-crispy-forms`
 `pip3 install Pillow`
4) For the first time running this make database migrations
 `python3 manage.py migrate` - should come back all okay
5) At this point you should be able to run the dev server
 `python3 manage.py runserver`
 Or you may create a superuser to sign in with by running the following command and entering user info
 `python3 manage.py createsuperuser`
6) Now you can access the website from the browser by typing the first option for our target users experience
 `localhost:8000`
 OR you can also access the administration side with your superuser account by typing 
 `localhost:8000/admin`
