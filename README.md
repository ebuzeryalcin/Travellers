![Travellers logo](static/images/readme/travellers-logo-readme.png)

# Travellers

- [Travellers](#travellers)
  - [UX](#ux)
    - [Project Goal](#project-goal)
    - [User Stories](#user-stories)
    - [Wireframes](#wireframes)
    - [Views and Data Structure](#views-and-data-structure)
    - [Design](#design)
      - [Typography](#typography)
      - [Color Scheme](#color-scheme)
  - [Features](#features)
    - [Existing Features](#existing-features)
      - [Account Registration](#account-registration)
      - [User Session](#user-session)
      - [Create New Entries, Place cards](#create-new-entries-place-cards)
      - [Places page](#places-page)
      - [View, Edit, and Delete cards](#view-edit-and-delete-cards)
      - [Security](#security)
    - [Features Left to Implement](#features-left-to-implement)
  - [Technologies Used](#technologies-used)
  - [Tools Used](#tools-used)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Local Deployment](#local-deployment)
    - [Deployment to Heroku](#deployment-to-heroku)
  - [Credits](#credits)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)

---

Travellers is an travel web application that offers users to create, edit, share and delete uploaded travel places. People travel and often forget what they did at a specific place, what they liked and disliked. This application allows users to upload travel places which will be public for other users. An easy to use application where people share travel destiantions with other people. 

![Travellers responsive display](static/images/readme/travellers-responsive-display.PNG)

It has been deployed to heroku and can be viewed from [here](https://travellers-ebuzer-yalcin.herokuapp.com/).

## UX

### Project Goal

Travellers is an application which can be used in different screen sizes. It is easy to use and understand. Navigation bar has only needed buttons and overall buttons is well thinked before implemented within the application. Whatever users do the application aims to give fast and intuitive experience. 

### User Stories

Users:
- As a user, I'd like to have a quick introduction about the page, why I should create an account. 
- As a user, I'd like the page to clearly show me where to register an account.
- As a user, I'd like the page to be smooth, easy to use.
- As a user, I'd like to interact and see other users uploaded travel cards.
- As a user, I'd like to share my own travel places by creating my own travel cards.
- As a user, I'd like to be able to upload image of a travel place. 
- As a user, I'd like to have intuitive buttons when I am logged in.
- As a user, I'd like to edit or delete my own travel cards.
- As a user, I'd like to get messages when I have added, edited or deleted a travel card. 

Content creator:
- As a content creator, I'd like to give an quick and understandable introduction of my page.
- As a content creator, I'd like to promote my page with nice looking travel cards on my Homepage. 
- As a content creator, I'd like to promote how to register.
- As a content creator, I'd like my page to be intuitive and informative for users.

### Wireframes

Based on user stories, wireframes were drawn. Full wireframes is found [here](static/images/readme/travellers-wireframe.png).

![Travellers wireframe](static/images/readme/Travellers-sample.png)

Final design looks quite similar to what was scetched at the beginning of this project. 

### Views and Data Structure

This is how the data structure look:

![data structure](static/images/readme/data-structure.png)

Views and actions:

![views and actions](static/images/readme/travellers-views.png)

Following image illustrates data validation the user can input:

![data validation](static/images/readme/data-validation.png)

These elements have been the same throughout the development stage.

### Design

This application have been built with bootstrap, such systems like grid and cards. The [Navbar theme](https://bootswatch.com/united/) and [Bootsrap cards](https://freefrontend.com/bootstrap-cards/) is some of the codes used in this project, while some styles were overwritten in [style.css](static/css/style.css) file.

Fonts and colors were choosen to create a clear look. I wanted an overall colorful and uplifting theme in this project. 

#### Typography

This font is used throughout the site:

1. **Ubuntu**: was used for the most as font in this project. This font was used for customized logo and for page texts. 

![Ubuntu font](static/images/readme/font-ubuntu.PNG)

#### Color Scheme

I tried to use lots of colors which were matching, at she same time I wanted to use standard colors for buttons, delete button has a red colors which is characteristics of its name:

-   [rgb(241, 111, 4)](https://convertingcolors.com/rgb-color-241_111_4.html?search=rgb(241,%20111,%204)) `- Dark, saturated orange`

This color was used throughout every page. Mainly because page content appeared nice with orange background and also because it blended in nive with the darker orange navigation bar.

-   [RGB(92, 66, 141)](https://convertingcolors.com/rgb-color-92_66_141.html?search=rgb(92,%2066,%20141)) ` - Dark purple`

 Used in logo and circles with placeholder for what html page you are in. A color that pops out, simply an eyecatching color. Also used in forms.

-   [Hex(17A2B8)](https://convertingcolors.com/hex-color-17A2B8.html?search=#17a2b8) ` - Sweet blue`

This color is used as background color in footer section, blends overall in with orange. 

-   [#f1f1f1](https://convertingcolors.com/hex-color-F1F1F1.html?search=#f1f1f1) ` - Super light grey`

Texts seemed to appear clearer with this color, suited well. 

-   [Hex(4CAF50)](https://convertingcolors.com/hex-color-4CAF50.html?search=#4CAF50) ` - Green`

This button color is used to submit register, login and submitting created travels cards. 

## Features

### Existing Features

#### Account Registration

-   People can register an account, choose a username and password:
    -   Username must be between 4 and 10 characters, pattern="^[a-zA-Z0-9]{4,10}$"
    -   Password must be between 5 and 15 characters, pattern="^[a-zA-Z0-9]{5,15}$"
    -   Requirement to fill the form to proceed registration

#### User Session

-   Existing users can log into their account using their chosen username and password
-   Same requirement to fill the form as the registration form, to login
-   Logout from account, closing session
-   Trying to accessing a page from the application while logged out, user will be redirected to login page

#### Create New Entries, Place cards

-   Users can create new entries, place cards, when logged in by clicking on New place button at the navbar
-   This is what the user needs to do to meet the requirements for validation:

    -   City name must be between 2 and 20 characters
    -   Country name must be between 2 and 20 characters
    -   The description must be between 10 and 250 caharters, a javascript function below the description input field is counting down the amount of charecters left
    -   Pros must be between 2 and 20 characters
    -   Cons must be between 2 and 20 characters
    -   A image url can be choosen, needs to be a url

All of these inputs are required.

#### Places page

-   The Places page is displaying all Place cards created by users chronologically, from most recently to oldest. Works both when logged in and when logged out.

#### View, edit, and delete cards

-   By clicking on My Profile, owner of the card can see all of its Place cards
-   Each Place card has two buttons, one to edit and one to delete the card
-   Place cards in this page is shown chronolically, from most recently to oldest
-   By clicking on edit user will be redirected to the edit place page
-   User can see all previous inputs and change inputs
-   If user don't want to change the card the editing can be cancelled by clicking on the cancel button, Place card will then remain the same

#### Security

Several steps were taken to ensure the security of the user's data.

-   The password users are using is secured with hashing method, a secret key which secures users password. It cannot be seen anywhere including the database.
-   For security reasons, if a user/person tries to access session features, application functionalitites which requires to be logged in, page will redirect to login page. This secority method keeps the application safe. 

### Features Left to Implement

-   Search for Places in place page.
-   Method to recover password, for this email information will also be needed.
-   Rate and/or mark Place cards as favourite.
-   Use an file api. When an image or gif is chosen, file is uploaded to a cloud so the app then can get the file via uploaded file url.

## Technologies Used

-   HTML5
-   CSS3
-   Bootstrap
-   Fontawesome
-   Google fonts
-   JavaScript / JQuery
-   Python
-   Favicon
-   Flask
-   [CSS Autoprefixer](https://autoprefixer.github.io/)

## Tools Used

-   [Lucidchart](https://www.lucidchart.com/pages/) to create the wireframes and to sketch
-   [Git](https://git-scm.com/) for version control
-   [Heroku](https://heroku.com/) to deploy the application
-   VS Code
-   [Responsive mockups](https://placeit.net/)

## Testing

Testing was done manually throughout the development process.

The full rundown of the testing can be found [here](TESTING.md).

Additionally, all code was validated in the following ways:

**HTML** - All pages were run through the [W3C HTML Validator](https://validator.w3.org/) to ensure compliance with the standards.

**CSS** - CSS validation with the W3C's [Jigsaw Validator](https://jigsaw.w3.org/css-validator/) returned overlay was not an overflow value. This is fixed. No other issues were found.

**Python** - All Python code was checked with the [PEP8 online validator](http://pep8online.com/) and is PEP8 compliant.

**Javascript** - All Javascript code was checked with the [JSHint](https://jshint.com/), successfully passed.

## Deployment

Before deploying the application, ensure the following are installed:

-   [Python 3](https://www.python.org/)
-   [PIP](https://pypi.org/project/pip/)
-   [Git](https://git-scm.com/)
-   [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

The application relies on the following service, and account will have to be created:

-   [MongoDB](https://www.mongodb.com/)

### Local Deployment

These are the steps to deploy Travellers locally.

1.  From the application's [repository](https://github.com/ebuzeryalcin/Travellers), click the "code" button and download the zip of the repository.

    Alternatively, you can clone the repository using the following line in your terminal:

        git clone https://github.com/ebuzeryalcin/Travellers.git

2.  Access the folder in your terminal window and install the application's required modules using the following command:

        python -m pip -r requirements.txt

3.  In MongoDB, create a new project called "myfirstcluster", and in this project create a new database called "task_manager".

    This database will contain two collections: `places` and `users`.

4.  Create a file containing your environmental variables called `env.py` at the root level of the application. It will need to contain the following lines and variables:

    ```
    import os

    os.environ.setdefault("IP", "0.0.0.0")
    os.environ.setdefault("PORT", "5000")
    os.environ.setdefault("SECRET_KEY", "YOUR_SECRET_KEY")
    os.environ.setdefault("MONGO_URI", "YOUR_MONGODB_URI")
    os.environ.setdefault("MONGO_DBNAME", "task_manager")
    ```

    Please note that you will need to update the `SECRET_KEY` with your own secret key, as well as the `MONGO_URI` and `MONGO_DBNAME` variables with those provided by those applications.

    If you plan on pushing this application to a public repository, ensure that `env.py` is added to your `.gitignore` file.

5.  The application can now be run locally. In your terminal, type the command `python3 run app.py`. The application will be available in your browser at the address `http://localhost:5000`.

### Deployment to Heroku

To deploy Travellers to Heroku, use the following steps:

1. Login to your Heroku account and create a new app.

2. Ensure the Procfile and requirements.txt files exist are present in your local repository.

    The Procfile should contain the following line:

    ```
    web: python app.py
    ```

    To ensure requirements.txt exists and is up to date, use the following line in your terminal:

    ```
    pip3 freeze --local > requirements.txt
    ```

3. Add heroku as a remote for your git repository by getting the heroku git URL for your application in its settings, and typing the following command:

    ```
    git remote add heroku https://git.heroku.com/your-heroku-git-url
    ```

4. Push Travellers to heroku with the following command:

    ```
    git push heroku master
    ```

5. In your terminal, enter the following line to prepare the application for launch once it is deployed

    ```
    heroku ps:scale web=5
    ```

6. In your app in heroku, go to settings, reveal the config vars and enter the following variables:

| Variable       | Value               |
| -------------- | ------------------- |
| IP             | 0.0.0.0             |
| PORT           | 5000                |
| SECRET_KEY     | YOUR_SECRET_KEY     |
| MONGO_URI      | YOUR_MONGO_URI      |
| MONGODB_NAME   | task_manager        |

Ensure to enter your own `SECRET_KEY`, `MONGO_URI`, `MONGODB_NAME` variables.

1. Go to the deploy tab of your application, and click "Deploy Branch" under the manual deploy section.

2. Travellers is now deployed to heroku. It can be accessed by clicken the "Open App" button on the top right.

## Credits

### Media

-   Travel inspiration [DeanSchneider](https://www.deanschneider.com/hakuna-mipaka/)

### Acknowledgements

-   Inspiration for this project came from my wife Kübra
-   [Felipe Alarcon](https://github.com/fandressouza) for always giving valuable feedback and for his avaliability
-   Mehmet Cengiz Turanlı for his support throughout the project

