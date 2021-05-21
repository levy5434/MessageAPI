# MessageAPI

Website which stores text messages  up to 160 characters with their views counter. Authenticated users can create messages, delete them and update which resets views counter. Any user is allowed to get a message, see it's content and views counter.

Live version: http://krzycho5434.pythonanywhere.com/

## Table of contents
* [Technologies](#technologies)
* [URLs](#urls)
* [Deployment](#Deployment)

## Technologies
* Python version: 3.9.5
* Django version: 3.2.3
* DRF version: 3.12.4

## URLs
Example shows how to use API with cURL.

To get a message use:
```
curl --location --request GET \
'http://krzycho5434.pythonanywhere.com/api/message/<message_id>/'
```
To get authentication token sent to your email use:
```
curl --location --request POST \
'http://krzycho5434.pythonanywhere.com/api/token/' \
--header 'Content-Type: application/json' \
--data-raw '{"email":"<your_text_message>"}'
```
To create a message use:
```
curl --location --request POST \
'http://krzycho5434.pythonanywhere.com/api/message/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Token <authentication_token>' \
--data-raw '{"text":"<your_text_message>"}'
```
To update an existing message use:
```
curl --location --request PUT \
'http://krzycho5434.pythonanywhere.com/api/message/<message_id>/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Token <authentication_token>' \
--data-raw '{"text":"<your_new_text_message>"}'
```
To delete an existing message use:
```
curl --location --request DELETE \
'http://krzycho5434.pythonanywhere.com/api/message/<message_id>/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Token <authentication_token>'
```
## Deployment
Project has been uploaded to pythonanywhere.com 
To run your project on the site. You have got to make an account, then create new app.
On the app bash console install python and make a virtual enviroment. Clone your project from github and install required packages using:
```
pip install -r requirements.txt
```
In Web options on pythonanywhere.com UI set the source code, working directory, virtualenv and wsgi configuration file paths.

Point your Django project setting is wsgi file:
```
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
```
Last thing is to update project ALLOWED_HOSTS settings.
```
 ALLOWED_HOSTS =['*'] 
```
Reload your app in user interface.
