## Konigle Test Django

# Requirements

First of all, run these:
1. pip install requirements.txt
2. python manage.py makemigrations
3. python manage.py migrate

# API 

1. List all the email : 127.0.0.1:8000/api/list
2. Add new email : 127.0.0.1:8000/api/add
3. Detail of the email : 127.0.0.1:8000/api/detail/<id>

# Users

- For the visitor index page : 127.0.0.1:8000
- For the seller dashboard : 127.0.0.1:8000/dashboard

login with this credential for seller:
- email: johndoe@email.com
- password: unity12345678

# Admin

Admin site: 127.0.0.1:8000/admin

login with this credential for admin:
- email: admin@email.com
- password: unity12345678

Login is using email address because most people will remember their email address rather than username, so the authentication system is changed to email required.

# Flow

Once the visitor visit the page, widget will pop up and ask for email submission. Email submitted will send to the API and get created into the database.

Seller could check the email list through their Dashboard.
There are 3 categories listed in the Dashboard (Total Email List, New Email of the current month, and Unsubscribed List) for the detial list of each category, seller can access it by clicking the icon on the top right of each card.

Unsubscribed email will still stay in the database for data science purposes, that is why the API is not support DELETE action, everytime the buyer unsubscribed from the seller, "subscribe" field will change to "False". Of course once the buyer submit the email again, it will be recorded as a newly added because the system will replaced the "date_action" field into the current date time and "subscribe" to True.

Every Monday and Wednesday, the system will send the email to the seller reporting the current stat. To activate this automation, of course Celery server need to be activated as well.

For this development stage, email backend is set to File Based in the settings and once the email is sent, File will be stored into "store_celery_emails_temp" folder as a log file

# Celery and Beat 

Sending Email automation is using Celery, Redis and Beat. 
Local machine need to install Redis from: 
https://github.com/tporadowski/redis/releases (Win)

or

https://redis.io/download/ (Mac and Linux)

To run these servers locally, open 2 terminals and run these commands on each terminal separately:
1. celery -A konigle_test worker --pool=solo -l info
2. celery -A konigle_test beat -l info

to change the time of sending email, go to :
celery.py file under konigle_test folder, change the schedule of Beat Scheduler to 'hour=' and 'minute='

Everything you need for the email content is under tasks.py inside 'Unity' folder
