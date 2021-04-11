![Travellers logo](static/images/readme/travellers-logo-readme.png)

# Testing

## Manual Testing

Manual testing was done throughout the development process. Often when new features were implemented, but also every now and then to make sure whole application was properly working.

### Errors and fixes:
**Card image not displayed**: When user uploaded an image in New Place and Edit Place forms the image name was uploaded to the database but actual image was not showing in created/edited cards. This only happened in Heroku page. Found out that when app was runned from workspace uploaded images was saved to both a specific created folder for uploaded images in the workspace and image name was uploaded to the database. This was not the case for Heroku page. I made a changes in add_place and edit_place app routes in app. py and added request.form.get(). Instead users were asked to insert image url's in New Place and Edit Place forms. After submitting the form image url's were uploaded to the database and were appearing in created Place cards. 

**Application revealing code**: When writing /logout at the end of the page url, an error page appeared revealing code. This is an important security issue and must be fixed, otherwise the application can be vulnerable. I added an function to logout app route in app. py which try: if there is a session, and if not user gets redirected to login page. Issue was fixed, and the code was not revealed anymore.

**Favicon was throwing an error to console**: Favicon was throwing errors to console telling "GET /profile/static/images/favicon/favicon.ico HTTP/1.1" 404 and "GET /profile/static/images/favicon/site.webmanifest HTTP/1.1" 404 errors. I googled this and found out links in python needs to look different. By changing favicon links in my base. html page, adding href="{{ url_for('static', filename='path') }}", I was able to fix these errors. 

