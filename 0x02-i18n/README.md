Project: i18n A
uthor: Samuel Atiemo

Project Tasks:

0. Basic Flask app
mandatory
First you will setup a basic Flask app in 0-app.py. Create a single / route and an index.html template that simply outputs “Welcome to Holberton” as page title (<title>) and “Hello world” as header (<h1>).

1. Basic Babel setup
mandatory
Install the Babel Flask extension:

2. Get locale from request
mandatory
Create a get_locale function with the babel.localeselector decorator. Use request.accept_languages to determine the best match with our supported languages.

3. Parametrize templates
mandatory
Use the _ or gettext function to parametrize your templates. Use the message IDs home_title and home_header.

4. Force locale with URL parameter
mandatory
In this task, you will implement a way to force a particular locale by passing the locale=fr parameter to your app’s URLs.

5. Mock logging in
mandatory
Creating a user login system is outside the scope of this project. To emulate a similar behavior, copy the following user table in 5-app.py.

6. Use user locale
mandatory
Change your get_locale function to use a user’s preferred local if it is supported.

7. Infer appropriate time zone
mandatory
Define a get_timezone function and use the babel.timezoneselector decorator.

8. Display the current time
#advanced
Based on the inferred time zone, display the current time on the home page in the default format. For example:

Jan 21, 2020, 5:55:39 AM or 21 janv. 2020 à 05:56:28


