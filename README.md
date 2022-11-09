# TiGOLF 

TiGOLF is a golf tips page where golfers can create an account and view different tips and can like and comment on the tips 

[Here is a live link to the app](https://golf-jnts.herokuapp.com/)

![App Title](/Assets/Documentation/deedee.png)

## How to use the Site

The Site is designed for golfers of all levels. It is a site they can visit and look at Tips and instruction for better technique. The user can register for an account and then interact with the posts. They can interact with them by commenting on them and liking them if the choose to do so. As user you will be able to comment on the post and it will then be approved by an Admin member. If a user wishes to update their comments the can so by using the Edit Button. If they choose remove their comment for some reason, they can so by using the delete button.

Here is a flow of how the app should work.

![Flow Diagram](/Assets/Documentation/flow_diagram.png)

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
        * The ability to Edit and Delete their on comments.
        
<br>
* The site’s home page Displays the most recent posts at the top of the page and then works back down the page in order of when they were created. At the top of the home page there is a navigation bar where the user can choose to register for an account if it’s their first time using the site or choose to login if they already have an account. There is also the option to sign-out after the user is logged in as well as the home button to take you back to the main page.

![Shaft Flex Calculating](/Assets/Documentation/flex_calcualtion.png)

* The app updates a google sheet with all the all of the User's inputs and the recommendations for club and shaft types.
![Google sheet of user input](/Assets/Documentation/google_sheet.png)  

* This can be really helpful to golf instructors and golf club fitters as it would let them see in advanced what kind of clubs a player would be able to use. 
* It can be good for data analysis to see what playing ability uses what shaft and type of club as well as average distances.

* The app uses validation and error-checking for all of the users inputs:
    * Names can't have numbers or special characters
    * Handicaps have to be within the limits of the R&A and USGA governing bodies of maximum 54.
    * Player must pick between certain distances on the 3 distances asked for to keep silly answers being out into the app.


## Testing

I have manually tested this project by doing the following:

* Given invalid inputs when asked for user's name:
    * Entered nothing when name was reuested
    * Entered numbers when the name was requested e.g(12345678890)
    * Entered special characters when the name was requested e.g(,.<>/?\|;:@'[]{})
* Each time an invalid input was entered into the Name request I expected to see an Error message to say that name couldn't be entered and this is what I seen.

![Name Validation](/Assets/Documentation/name_valid.png)


* Given invalid inputs when asked for the User's Handicap:
    * Entered a value higher than 54
    * Entered a value lower than 1
* Both times I expected to see an Error messsage saying that it was an invalid data input:
    * Too high for values over 54
    * Too Low for values under 1

![Handicap Validation](/Assets/Documentation/handicap_valid.png)

* Invalid inputs were also given for Pitching Wedge distance:
    * Too high (any values over 170 yards)
    * Too low (any values under 90 yards)
* Both times I expected to see an Error messsage saying that it was an invalid data input:
    * Too high for values over 170
    * Too Low for values under 90

![Pitching Wedge Validation](/Assets/Documentation/pwedge_valid.png)

* Invalid inputs were also given for 6 Iron distance:
    * Too high (any values over 220 yards)
    * Too low (any values under 130 yards)
* Both times I expected to see an Error messsage saying that it was an invalid data input:
    * Too high for values over 220
    * Too Low for values under 130

![Six Iron Validation](/Assets/Documentation/six_iron_valid.png)

* Invalid inputs were also given for Driver distance:
    * Too high (any values over 350 yards)
    * Too low (any values under 190 yards)
* Both times I expected to see an Error messsage saying that it was an invalid data input:
    * Too high for values over 350
    * Too Low for values under 130

![Driver Distance Vaildation](/Assets/Documentation/driver_valid.png)

* I also done manual testing to make sure all the outcomes would be accurate for different combinations of inputs.

* I tested a difference of less than 56 yards between 6 iron and pitching wedge distances.
    * My expected result result was Cavity Backs

        ![Cavity test](/Assets/Documentation/cav_test.png)

* I tested a difference of more than 55 yards between 6 iron and pitching wedge distances but with the 6 iron distance less then 190.
    * My expected result was Combo Set

        ![Combo test](/Assets/Documentation/combo_test.png)

* I tested a difference of more than 55 yards between 6 iron and pitching wedge distances but with the 6 iron distance more then 190.
    * My expected result was Blades

        ![Blades test](/Assets/Documentation/blade_test.png)

* I done testing to make sure that there are different outcomes for shaft flex:

    * I tested with different Driver distances of:
        * Less than 213
        * Between 213 - 262
        * More then 262
    
    The reason these distances were tested is that they correspond to the different clubhead speeds in the function that chooses the flex of shaft for the user.
    
    * My expected result of distances less than 213 were Regular

        ![Regular test](/Assets/Documentation/reg_test.png) 

    * My expected result of distances between 213 and 262 was Stiff

        ![Stiff test](/Assets/Documentation/stiff_test.png)

    * My expected result of distances more than 262 was Extra-Stiff

        ![Extra test](/Assets/Documentation/extra_test.png)


### Bugs

#### Solved Bugs 
* I had an issue with line length when first passing the code through PEP8. A lot of f strings were too long (> 79 characters).
I solved this through breaking them up into multiple f strings.

#### Remaing Bug
* No bugs remaining
    
#### Validator Testing
* No errors were found when running the code through [PEP8](http://pep8online.com/)

## Technologies

* [Heroku](https://www.heroku.com/)
* [Python](https://www.python.org/)
* [Pip](https://pypi.org/project/pip/)
* [colorama](https://pypi.org/project/colorama/)
* [Pyfiglet](https://pypi.org/project/pyfiglet/0.7/)
* [Git](https://git-scm.com/)
* [Githib](https://github.com/)
* [Gitpod](https://gitpod.io/)

## Deployment
* Create an account or log in at [Heroku](https://www.heroku.com/)
* Create new app, 
    * Add a unique name for your app (this app is called 'deedees-fitting-app')
    * Choose your region

* Click on Create New App
* Navigate to the Settings tab
* Under Config Vars store any sensitive data you saved in .json file. 
    * Add a Key - CREDS, then copy the .json file and paste it into Value field 
    * Add a Key - PORT and a Value 8000
* Add buildpacks: 
    * Add Python, then save changes
    * Add Nodejs, then save changes
    * Ensure Python is first and Nodejs second

* Navigate to Deploy tab
    * From Deployment Method select Github
    * Connect to Github
    * Search for repository name (club-shaft-fitter)
    * Click 'Connect'
    * Select 'Enable Automatic Deploys' if you wish for Heroku to rebuild the app every time you push changes to Github
    * Click 'Deploy Branch'
    * Click 'View'

* [Live link to the App](https://deedees-fitting-app.herokuapp.com/)    
* [Live link to the Google Sheet](https://docs.google.com/spreadsheets/d/1g5nW55t43D_g49mGp38mo4rYHIyMCGGKmicDN2v5zaw/edit#gid=1680754323)

## Credits 

* Code Institute - LMS, Love Sandwiches, Tutor Support, Python Template
* Stackoverflow
* Geeksforgeeks
* Youtube
* Google Sheets for Developers
* PEP8
* W3Schools




