# Hudl_QA_Test_Project

----- Structure of Hudl Test Project ---------

This project has been built using Selenium WebDriver, Chrome Webdriver, Python 3.7 and Visual Studio Code. The project has been divided into 4 major test components:
1. All buttons on the Login page 
2. The "Need Help?" functionality
3. Login checks using Email and Password
4. The "Log In with Organization" functionality

1. All Buttons on the Login page --> The buttons on this page include:
a. The Back button (signified by the <-- arrow)
b. The Hudl logo
c. The Sign Up button
The functionality of all these buttons has been tested, and for verification, applicable messages have been printed out in the terminal console.

2. The Need Help functionality --> The Need Help functionality has been tested firstly by clicking the button, following which test scripts have been written to check 
whether the Reset Password link is being sent only to those email IDs which are registered with Hudl. For those, two broad tests have been employed, a negative test with
an unregistered email ID, and a positive test with an existing email ID. 

3. Login checks using Email and Password --> The test cases scripted for the actual login functionality includes:
a. Correct email with incorrect password
b. Blank email and password fields
c. Correct email and correct password  

4. The "Log In with Organization" functionality --> This alternative login method has been tested by filling an email ID and attempting to log in. Due to the fact
that there is no organization email existing currently, this will be a negative test. 


