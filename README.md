<h1 align="center">Top 12 Anime</h1>

[View the live project here](https://top-10-anime-f8c245cd60e9.herokuapp.com/)

The project contains an application called Top 12 Anime which is a website that gives details on the top 12 rated anime of all time. I originally had the top 10 rated animes but decided to change to the top 12 animes as I think the 3 per row looked nicer and used up a bit more whitespace without being to big.

The admin user of the site can manage comments to keep the website a respectable and harmfree place

![Mockup](documentation/supp-images/amiresponsive.png)

## Index – Table of Contents
* [User Experience (UX)](#user-experience-ux) 
* [Features](#features)
* [Design](#design)
* [Planning](#planning)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## User Experience (UX)

### User stories :

* US01: View Top 10 Rated Anime
  - As a visitor, I want to view a list of the top 10 rated anime, with their ratings, genres, and images, so I can easily find out about the best anime
* US02: View Details page
  - As a visitor, I want to click on an anime title to view more detailed information such as the plot, characters, release date, and predefined ratings.
* US03: User sign-up
  -As a new user, I want to create an account with my email and password, so I can leave comments and like/dislike anime or comments.
* US04: User login
  - As a returning user, I want to log in to my account, so I can interact with the content (comment, like/dislike).
* US05: Admin panel
  - As an admin, I want to manage user accounts and interactions, so I can moderate content for the website.
* US06: Admin comment management
  - As an admin, I want to moderate user comments and delete inappropriate or harmful content, so I can ensure the site remains a positive space.
* US07: Add comments
  - As a logged-in user, I want to comment on my favorite anime from the list, so I can share my thoughts with other fans.
* US08: Like/Dislike Anime
  - As a logged-in user, I want to like or dislike an anime and other users' comments, so I can engage with the community.


## Features

### Existing Features

-   __F01 Navigation Bar__
    
    The navigation bar has a consistent look and placement each page supporting easy and intuitive navigation.  It includes a Logo, and a link to the Home page. If the user is not signed in then links are available to the Sign-up page.  If a user is signed in then the links available, in addition to the Home link, are for  and Sign out; and the active username and a user icon are also displayed.
    
    If the user signed in is the admin user then an additional link of Admin is also shown on the navigation bar.  This link takes the user to the Django Admin screens where data in the underlying database can be added, retrieved, modified and deleted.
    
    The navigation bar is responsive on multiple screen sizes - on smaller screens it coverts to a 'burger' menu style.  
    
    ![Navbar Full](documentation/webpages/nav-signed-out.png)
    ![Navbar Full Signed in](documentation/webpages/nav-signed-in.png)
    ![Navbar Burger](documentation/webpages/nav-burger.png)


-   __F02 Landing page image and text__
    
    At the top of the landing page (home page) there is an area that includes a photograph and a text overlay which together clearly identify the purpose of the site as a place to find and book guided hikes in Banff.  

    ![Landing Area](documentation/webpages/homepage.png)

    

    


    ![ Detail](documentation/webpages/details-page.png)



    ![Comment](documentation/webpages/comments.png)





-   __F10 User authentication__
    
    The application provides the following user authentication related functions :

    - User Registration
      - A user needs to be registered before they can sign in.  The option to Register appears on the navigation bar when no user is currently signed in.  To Register, the user needs to provide a) a username which has not already been registered, b) an optional email address (if this is provided then it needs to be an email address that is not already registered) and c) a password which they must enter twice.  Once registered a user can sign in.

        ![Register User](documentation/webpages/signup.png)

    - User Sign in
      - Once registered a user can sign in and will have access to extra functionality, namely :
        - can comment on a anime
        - can like a anime

      - To sign in the user must provide a) a registered username and b) the password for the username
     
        ![Sign in User](documentation/webpages/signin.png)
      
    - User Sign out
      - A signed in user can sign out by clicking on the Sign out link on the navigation bar.  The user simply needs to confirm the action by clicking on the Sign out button on the page.

        ![Sign out User](documentation/webpages/signout.png)




### Features which could be implemented in the future

- Adding likes/dislikes to the posts and comments.


## Design

-   ### Wireframes

    The wireframe diagrams below describe the Home, Login, Logout and Sign-up pages.
    <details>
    <summary>Desktop Wireframes</summary>

    ![Desktop Wireframes](documentation/wireframes/homepage_desktop.png)
    ![Desktop Wireframes](documentation/wireframes/detailspage_desktop.png)
    ![Desktop Wireframes](documentation/wireframes/userbiopage_desktop.png)
    </details>
    <details>
    <summary>Tablet Wireframes</summary>

    ![Tablet Wireframes](documentation/wireframes/homepage_tablet.png)
    ![Tablet Wireframes](documentation/wireframes/detailspage_tablet.png)
    ![Tablet Wireframes](documentation/wireframes/userbiopage_tablet.png)
    </details>
    <details>
    <summary>Smartphone Wireframes</summary>

    ![Smartphone Wireframes](documentation/wireframes/homepage_mobile.png)
    ![Smartphone Wireframes](documentation/wireframes/detailspage_mobile.png)
    ![Smartphone Wireframes](documentation/wireframes/userbiopage_mobile.png)
    </details>


## Planning

A GitHub Project with linked Issues was used as the Agile tool for this project.  User Stories with acceptance criteria were defined using GitHub Issues and development of code for these stories was managed using a Kanban board.  All of the User Stories were linked to a 'parent' Epic issue to show how they all supported the over-arching goal of the project.  The acceptance criteria were tested as each story moved to 'Done' and were also included in the final pre-submission manual testing documented in the Testing section of this README.

The Epic, User Stories and Kanban board can be accessed here : [Project board](https://github.com/users/JackH1155/projects/2/views/1)


## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Python](https://www.python.org/)

### Frameworks, Libraries & Programs Used

-[Django]

### Validator Testing 

- [HTML Validator](https://validator.w3.org/)

- results for index.html
  - <details>
    <summary>Homepage</summary>

    ![Homepage](documentation/testing/homepage-test.png)
  </details>

- results for post_details.html
  - <details>
    <summary>Anime Details</summary>

    ![Anime Details](documentation/testing/details-test.png)
  </details>

- results for user_bio.html
  - <details>
    <summary>User Profile</summary>

    ![User Profile](documentation/testing/userbio-test.png)
  </details>

- results for edit_bio.html
  - <details>
    <summary>Edit Profile</summary>

    ![Edit Profile](documentation/testing/editbio-test.png)
  </details>

- results for signup.html
  - <details>
    <summary>Signup</summary>

    ![Signup](documentation/testing/signup-test.png)
  </details>

- results for login.html
  - <details>
    <summary>Login</summary>

    ![Login](documentation/testing/login-test.png)
  </details>

- results for signout.html
  - <details>
    <summary>Logout</summary>

    ![Logout](documentation/testing/logout-test.png)
  </details>


- [CSS Validator](https://jigsaw.w3.org/css-validator/)

 - <details>
      <summary>style.css validation results</summary>

      ![style.css](documentation/testing/comments-jshint.png)
      </details>


- [Python Validator](https://pep8ci.herokuapp.com/)
  - <details>
      <summary>Top 10 Anime urls.py validation results</summary>

      ![Top 10 Anime urls.py](documentation/testing/top_10_anime-urls.png)
    </details>

  - <details>
      <summary>Project settings.py validation results</summary>

      ![Project settings.py](documentation/testing/settings-test.png)
    </details>

  - <details>
      <summary>Blog urls.py validation results</summary>

      ![Blog urls.py](documentation/testing/blog-urls.png)
    </details>

  - <details>
      <summary>Blog admin.py validation results</summary>

      ![Blog admin.py](documentation/testing/blog-admin.png)
    </details>

  - <details>
      <summary>Blog forms.py validation results</summary>

      ![Blog forms.py](documentation/testing/blog-forms.png)
    </details>

  - <details>
      <summary>Blog models.py validation results</summary>

      ![Blog models.py](documentation/testing/blog-models.png)
    </details>

  - <details>
      <summary>Blog views.py validation results</summary>

      ![Blog views.py](documentation/testing/blog-views.png)
    </details>

  - <details>
      <summary>UserBio admin.py validation results</summary>

      ![UserBio admin.py](documentation/testing/userbio-admin.png)
    </details>

  - <details>
      <summary>UserBio forms.py validation results</summary>

      ![UserBio forms.py](documentation/testing/userbio-forms.png)
    </details>

  - <details>
      <summary>UserBio models.py validation results</summary>

      ![UserBio models.py](documentation/testing/userbio-models.png)
    </details>

  - <details>
      <summary>UserBio views.py validation results</summary>

      ![UserBio views.py](documentation/testing/userbio-views.png)
    </details>
  

### Manual Testing Test Cases and Results


| **User Story (US)** | **Test Case** | **Acceptance Criteria** | **Expected Outcome** | **Actual Outcome** | **Pass/Fail** |
| ------ | ------ | ------ | ------ | ------ | ------ |
| **US01** : As a visitor, I want to view a list of the top 10 rated anime, with their ratings, genres, and images, so I can easily find out about the best anime | Verify that HomePage shows the top 12 anime in order of ratings | 1. The page displays the top 12 anime in a grid or list format. 2. Each anime entry includes an image, title, genre, rating, and brief description. 3. Clicking on an anime title or image leads to its detail page. | Seeing the 12 highest rated Anime on homepage. Each Anime has a picture, title, genre, rating and a brief description.  Clicking on the title or image takes you to the details page. | HomePage displays the top 12 rated Animes. Each Anime doesn't have the genre or a description but does have the ranking(rating) with an image and a title. Clicking on the title takes you to the details page though clicking on the image does not. | 1. Pass 2. Fail 3. Fail |
| **US02** : As a visitor, I want to click on an anime title to view more detailed information such as the plot, characters, release date, and predefined ratings. | Verify that the visitors can view the details page, like and/or comment on the Anime. | 1.The page displays detailed information for the selected anime. 2. Users can like/dislike the anime on this page. 3. Users can see the like/dislike count. The page includes a comment section (for logged-in users) and displays previous comments. | Visitors can click on an Anime to go to its detail page and viewing more information on the Anime. Logged in Users can like/dislike and/or comment on the Anime. | Visitors can view the details page. Logged in users can comment on the Anime but not like/dislike | 1. Pass 2. Fail 3. Fail 4. Pass |
| **US03** :  |  |  |  |  |  |
| **US04** :  |  |  |  |  |  |
| **US05** :  |  |  |  |  |  |
| **US06** :  |  |  |  |  |  |
| **US07** :  |  |  |  |  |  |
| **US08** :  |  |  |  |  |  |


__Summary of Testing__

| **Category** | **Pass** | **Fail** | **Total Tests** |
| ---- | ---- | ---- | ---- |
| Functionality Testing |  |  | 1 |
| Responsive Design |  |  | Tested on mobile, tablet, desktop (Chrome, Opera, Edge) |
| Performance Testing |  |  | Tested on mobile, tablet, desktop | 

__Overall Conclusion__
All tested user stories and acceptance criteria passed successfully. The website provides a seamless user experience with intuitive navigation, responsive design across multiple devices, and strong security features for handling user bookings.




### Browser Compatibility

- Chrome DevTools was used to test the responsiveness of the application on different screen sizes.  In addition, testing has been carried out on the following browsers :
    - Google Chrome version
    - Opera
    - Microsoft Edge

    

### Known bugs

- Some images on homepage are to small.
- Profile default image doesn't load.


### Create Application and Postgres DB on Heroku
- Log in to Heroku at https://heroku.com - create an account if needed.
- From the Heroku dashboard, click the Create new app button.  For a new account an icon will be visible on screen to allow you to Create an app, otherwise a link to this function is located under the New dropdown menu at the top right of the screen.
- On the Create New App page, enter a unique name for the application and select region.  Then click Create app.
- On the Application Configuration page for the new app, click on the Resources tab.
- In the Add-ons search bar enter "Postgres" and select "Heroku Postgres" from the list - click the "Submit Order Form" button on the pop-up dialog.
- Next, click on Settings on the Application Configuration page and click on the "Reveal Config Vars" button - check the DATABASE_URL has been automatically set up. 
- Add a new Config Var called DISABLE_COLLECTSTATIC and assign it a value of 1.
- Add a new Config Var called SECRET_KEY and assign it a value - any random string of letters, digits and symbols.
- The settings.py file should be updated to use the DATABASE_URL and SECRET_KEY environment variable values as follows :

  - DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}

  - SECRET_KEY = os.environ.get('SECRET_KEY')

- In Gitpod, in the project terminal window, to initialize the data model in the postgres database, run the command : python3 manage.py migrate 
- Make sure the project requirements.txt file is up to date with all necessary supporting files by entering the command : pip3 freeze --local > requirements.txt
- Commit and push any local changes to GitHub.
- In order to be able to run the application on localhost, add SECRECT_KEY and DATABASE_URL and their values to env.py


### Connect the Heroku app to the GitHub repository
- Go to the Application Configuration page for the application on Heroku and click on the Deploy tab.
- Select GitHub as the Deployment Method and if prompted, confirm that you want to connect to GitHub. Enter the name of the github repository (the one used for this project is () and click on Connect to link up the Heroku app to the GitHub repository code.
- Scroll down the page and choose to either Automatically Deploy each time changes are pushed to GitHub, or Manually deploy - for this project Manual Deploy was selected.
- The application can be run from the Application Configuration page by clicking on the Open App button.
- The live link for this project is (https://top-10-anime-f8c245cd60e9.herokuapp.com/)



#### The live link to the application can be found here - (https://top-10-anime-f8c245cd60e9.herokuapp.com/) 


## Credits 
Used this README https://github.com/elainebroche-dev/pf4-wayfarers-guided-hikes/blob/main/README.md as a base skeleton for my README.

Got images and details from https://www.imdb.com/search/title/?keywords=anime&sort=user_rating,desc


### Code 

Some of the code is from the CodeStar blog walkthrough. I changed it a little to fit into my project.

I have used ChatGPT to help with some issues and some code stucture.


### Content 

Imformation on the top 12 rated Anime and the order they are rated in.
