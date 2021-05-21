# MessageAPI

Website which stores messages with views counter. Authenticated users can create messages, deletes them and updates which resets views counter. Any user is allowed to get a message, see it's content and view counter.

Live version: http://krzycho5434.pythonanywhere.com/

## Table of contents
* [Technologies](#technologies)
* [URLs](#urls)

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
To update existing message use:
```
curl --location --request PUT \
'http://krzycho5434.pythonanywhere.com/api/message/<message_id>/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Token <authentication_token>' \
--data-raw '{"text":"<your_new_text_message>"}'
```
To delete existing message use:
```
curl --location --request DELETE \
'http://krzycho5434.pythonanywhere.com/api/message/<message_id>/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Token <authentication_token>'
```

