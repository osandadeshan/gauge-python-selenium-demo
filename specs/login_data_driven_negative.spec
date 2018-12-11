# Login Specification - Data Driven Negative Tests
Date Created    : 11/21/2018
Version		    : 1.0
Owner		       : Osanda Deshan
Description	    : Negative Data Driven Login Tests


   |user_name|password|
   |---------|--------|
   |gem      |gem     |
   |gemunu   |gemunu  |


* On Login Page

## Non registered users cannot login to the system

tags: registered-user, fail, login, data-driven

* Login as <user_name> using <password>
* User cannot navigate to the home page
