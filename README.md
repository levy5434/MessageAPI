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
'http://appmessageapi.azurewebsites.net/api/message/<message_id>/'
```
To get authentication token sent to your email use:
```
curl --location --request POST \
'http://appmessageapi.azurewebsites.net/api/token/' \
--header 'Content-Type: application/json' \
--data-raw '{"email":"<your_email_address>"}'
```
To create a message use:
```
curl --location --request POST \
'http://appmessageapi.azurewebsites.net/api/message/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Token <authentication_token>' \
--data-raw '{"text":"<your_text_message>"}'
```
To update an existing message use:
```
curl --location --request PUT \
'http://appmessageapi.azurewebsites.net/api/message/<message_id>/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Token <authentication_token>' \
--data-raw '{"text":"<your_new_text_message>"}'
```
To delete an existing message use:
```
curl --location --request DELETE \
'http://appmessageapi.azurewebsites.net/api/message/<message_id>/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Token <authentication_token>'
```
## Deployment
Application has been deployed via Azure Container Registry and Azure Web App Service.
