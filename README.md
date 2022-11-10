# TiGOLF 

TiGOLF is a golf tips page where golfers can create an account and view different tips and can like and comment on the tips 

[Here is a live link to the site](https://golftips.herokuapp.com/)

![Responsive Tips](/media/tip-responsive.jpg)

## How to use the Site

The Site is designed for golfers of all levels. It is a site they can visit and look at Tips and instruction for better technique. The user can register for an account and then interact with the posts. They can interact with them by commenting on them and liking them if the choose to do so. As user you will be able to comment on the post and it will then be approved by an Admin member. If a user wishes to update their comments the can so by using the Edit Button. If they choose remove their comment for some reason, they can so by using the delete button.

Here is a flow of how the app should work.

![Flow Diagram](/media/flow-tips.jpg)

## User Stories
![User Stories](/media/user-stories.jpg)

* As a Site User I can view a list of tips posts so that I can select one to read
* As a Site User I can open a tips post so that see the whole tips post and read the insights
* As a Site Admin / Site User I can view the number of likes so that I can see what is popular and decide what is popular content
* As a Site Admin / Site User I can view comments on tips posts so that can read the conversation and what user's would like in future
* As a Site User I can register an account so that I can comment and and like tips posts
* As a Site I can leave comments on a post so that join in the conversation and say what I would like to see
* As a Site User I can like or unlike a tips post so that I can interact with the posted content
* As a Site Admin I can approve or disapprove comments so that I can filter out unsuitable comments
* As a Site User I can view a paginated list of tips posts so that easily select a tip to view
* As a Site Admin I can create, read, update and delete tips posts so that I can manage the site's content
* As a Site User I can edit or delete comments I have posted so that I can amend any mistakes I make after posting a comment

[Here is LINK to the live project board](https://github.com/users/dandon1990/projects/7/views/1)





## Features
* The site features posts that include: 
    * On the Home page the site displays all of the different Tips that have been posted.
    * The posts also have the details of who wrote them and which part of the game it is aimed at whether it (Long game, Short game, Putting)
    
    * Post features include:
        * Title of what is being taught.
        * Image of the stance that should be taken when playing the shot.
        * Details explaing the image and how to achieve the desire stance and what it should feel like.
        * Image of the swing to take when playing the particular shot.
        * An explanation of how long the swing should be and what the tempo should be.
        * A Comments section for users to read the conversation.
        * The ability for users to Edit and Delete their own comments.

![Home page](/media/Tips-home-page.jpg)
* The site’s home page Displays the most recent posts at the top of the page and then works back down the page in order of when they were created. There is also the option to sign-out after the user is logged in as well as the home button to take you back to the main page.

![Navigation](/media/navigation-tips.jpg)

*  At the top of the home page there is a navigation bar where the user can choose to register for an account if it’s their first time using the site or choose to login if they already have an account.
![Navigation Logout](/media/navigation-logout.jpg)

* There is also the option to sign-out after the user is logged in as well as the home button to take you back to the main page.

![No comment](/media/no-comment.jpg)

* A user will only be able to view the comments on the if they are not logged in. They won't be able to click the like button or comment on the post.

![Can comment](/media/can-comment.jpg)

* Once a user is logged in the can post a comment which will be approved by an admin member. The can also edit and delete their own comments but they cannot edit or delete comments from other users.



## Testing

I have manually tested this project by doing the following:

* Logging out of the account and checking:
    * If it is possible to like a post.
        * My expected result was that I wouldn't be able to like the post.
        * The result was that I could not like the post.
    * If it is possible to comment on a post.
        * My expected result was that I wouldn't be able to comment on a post.
        * The result was that I could not comment on the post.
    * If it is possible to edit a comment on a post.
        * My expected result was that I wouldn't be able to edit a comment on a post.
        * The result was that I could not edit a comment on the post.
    * If it is possible to delete a comment on a post.
        * My expected result was that I wouldn't be able to delete a comment on a post.
        * The result was that I could not delete a comment on the post.  

* Logging into the account and checking:
    * If it is possible to make a comment on a post.
        * My expected result was that I would be able to make a comment and it would have to approved by admin
        * The result was that I could post a comment and I have to wait for admin to approve it.
    * If it is possible to edit a comment on a post created by the user logged in.
        * My expected result was that I would be able to edit a comment created by the user logged in.
        * The result was that I was able to edit a comment created by the user logged in.
    * If it is possible to delete a comment created by the user logged into the account.
        * My expected result was that I would be able to delete a comment created byt the user logged into the account.
        * The result was that I could delete a comment created by the user logged into the account.
    * If it is possible to edit or delete a comment created by another user when logged into the account.
        * My expected result was that I would not be able to edit or delete comments created by other users whilst logged into the account.
        * The result was that I could not delete a comment created by another user logged into the account.

### Bugs

#### Solved Bugs 
* I had an issue with line length when first passing the code through PEP8. A lot of methods and variables were too long (> 79 characters).
I solved this through breaking them up into mutiple strings or displaying them in a verticle manner.

#### Remaing Bug
* No bugs remaining
    
#### Validator Testing
* No errors were found when running the code through [PEP8](http://pep8online.com/)
* No errors were found when running the HTML through [W3C](https://validator.w3.org/)
* No errors were found when running the CSS through [Jigsaw](https://jigsaw.w3.org/css-validator/)

## Technologies

* [Heroku](https://www.heroku.com/)
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Pip](https://pypi.org/project/pip/)
* [Git](https://git-scm.com/)
* [Githib](https://github.com/)
* [Gitpod](https://gitpod.io/)
* [Summernote](https://summernote.org/)
* [Bootstrap](https://getbootstrap.com/)


##  Deployment

To deploy this page to Heroku from its GitHub repository, the following steps were taken:
1. Clone this repository in Github
2. Create the Heroku App:
- Select "Create new app" in Heroku.
- Choose a name for your app and select the location.

3. Attach the Postgres database:
- In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.

4. Prepare the environment and settings.py file:

- In the Settings tab, click on Reveal Config Vars and copy the url next to DATABASE_URL.
- In your GitPod workspace, create an env.py file in the main directory.
- Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
- Add the SECRET_KEY value to the Config Vars in Heroku.
- Update the settings.py file to import the env file and add the SECRETKEY and DATABASE_URL file paths.
- Update the Config Vars with the Cloudinary url, adding into the settings.py file also.
- In settings.py add the following sections:
Cloudinary to the INSTALLED_APPS list
STATICFILE_STORAGE
STATICFILES_DIRS
STATIC_ROOT
MEDIA_URL
DEFAULT_FILE_STORAGE
TEMPLATES_DIR
Update DIRS in TEMPLATES with TEMPLATES_DIR
Update ALLOWED_HOSTS with ['app_name.heroku.com', 'localhost']
5. Store Static and Media files in Cloudinary and Deploy to Heroku:

- Create three directories in the main directory; media, static and templates.
- Create a file named "Procfile" in the main directory and add the following:
- web: gunicorn project-name.wsgi
- Log in to Heroku using the terminal heroku login -i.
- Then run the following command: heroku git:remote -a vegan-a-eat. This will link the app to the Gitpod terminal.
- After linking your app to your workspace, you can then deploy new versions of the app by running the command git push 
heroku main and your app will be deployed to Heroku.


## Credits 

* Code Institute 
    * LMS 
    * I think there I Blog walkthrough project
    * Hello DJango walkthrough project
    * Tutor Support - Special mentions to Ger, Gemma and Rebecca
* Stackoverflow
* Geeksforgeeks
* Youtube
* Google Sheets for Developers
* PEP8
* W3Schools
* Angharad Caswell - Deployment steps




