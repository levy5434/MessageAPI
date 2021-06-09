# MessageAPI

Website which stores text messages  up to 160 characters with their views counter. Authenticated users can create messages, delete them and update which resets views counter. Any user is allowed to get a message, see it's content and views counter.

Live version: http://appmessageapi.azurewebsites.net/

## Table of contents
* [Technologies](#technologies)
* [URLs](#urls)
* [Deployment](#deployment)

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
Application has been deployed via Azure Container Registry and Azure Web App Service.\
To deploy this project first create a tagged container:
```
docker build -t [container's_name]:[version] .
```
Then create new container registry in Azure Container Registry service and enable `Admin user` in `Access keys` to get passwords for logging into service.\
In terminal login to Container Registry service and push container to cloud:
```
docker login [login_server]
docker push [container's_name]:[version]
```
After successfully uploading container's image, `Create Web App` in Azure Web App Service. Change `Publish` option to Docker Container and choose `Image Source` to Azure Container Registry and newly pushed image.\
After creating the Web App go to `Configuration` and add new application setting:
```
WEBSITES_PORT:8000
```
Application is ready to work on Azure Web App Service.
