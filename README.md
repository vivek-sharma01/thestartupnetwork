
This README would normally document whatever steps are necessary to get your application up and running.

### Dependencies ###

* Python 3.x
* PostGreSQL above 9.4

### Getting Started ###

* Create a user for postgres : "createuser thestartupnetwork "
* Create a db for the application : "createdb thestartupnetwork with password test"
* Set password for the database : <DB_PASSWORD>


### Virtual Environment Setup ###

* Setup uti virtualenv : "virtualenv -p python3 env"
* Move to virtualenv and activate its environment (source env/bin/activate)
* pip  install -r requirements.txt


### Bitbucket Repository Setup ###

* Go to the link: https://github.com/ashu0992sharma/thestartupnetwork
* Fork the original git repository 
* You can see your new repository in your repository list (https://github.com/<USER_NAME>/thestartupnetwork)
* Clone this new repository : git clone ur forked repo (e.g) https://github.com/<USER_NAME>/thestartupnetwork.git
* Using Command Line, navigate to the repository
* Check the remote : git remote -v (It will show 2 lines for origin)
* Add an upstream : git remote add upstream https://github.com/ashu0992sharma/thestartupnetwork
* Again check the remote : git remote -v (It will show 4 lines. 2 for origin and 2 for upstream)


### Code Setup ###


* Enter into terminal
* cd to project path
* python manage.py makemigrations
* python manage.py migrate
* create a superuser: python manage.py createsuperuser
* Run python manage.py runserver
* Go to browser and open localhost:8000/admin/ with the superuser credentials

### Celery workers ###

* Install RabbitMQ

        1) sudo apt-get install rabbitmq-server

* To run Celery

        1) Traverse to the project root directory
        2) Enable the virtual environment ( source env/bin/activate )
        3) celery -A mobileapps.celery_app worker --loglevel=DEBUG
        4) celery -A mobileapps.celery_app beat

* To add a periodic task through admin
        1) add an interval under Intervals
        2) Under Periodic tasks add the periodic task with queue name same as that defined in code.


### Push-Pull and PR Understanding ###

* To pull the code from upstream (Get changes from the original repo to your forked repo) : 
        
        1) git fetch upstream <BRANCH_NAME (if required)>
        2) git merge upstream/<BRANCH_NAME> <BRANCH_NAME>
        3) git push origin <BRANCH_NAME> (This is done to push the changes captured from original repository to your forked repository)


* To push the code (Push your changes): 
        
        1) git push origin <BRANCH_NAME>


