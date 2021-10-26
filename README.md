# Password_Locker

## Author
***DannyMyles***

## Description
This is a python application that manages Login and Signup credentials of a person for various accounts that is the Usernames and Passwords for each account. It also stores the passwords and generates a unique password for a user if they do not want to generate new passwords by themselves.

## Set-up instructions
### Install
Python3.9.1 in order to operate.

### Cloning my repository:
* Open Terminal {Ctrl+Alt+T}

* git clone git@github.com:DannyMyles/Password_Locker.git
* cd Password_Locker

* code . or atom . based on the text editor you have.

## How to Run the application!
To run the application, open the cloned file in terminal and run the following commands:

      $ chmod +x run.py

      $ ./run.py

To run test for the application *use $ python3.9 run_test.py

## User Story
As a user I would like to... :

    1. To create an account for the application or log into the application.

    2. Store my existing acounts login details for various accounts that I have registered for.

    3. Generate new password for an account that I haven't registered for and store it with the account name.

    4. Delete stored account login details that I do not want anymore.

    5. Copy my credentials to the clipboard.

## BDD
|               Behaviour              | Input                            | Output                                               |
|:------------------------------------:|----------------------------------|------------------------------------------------------|
| Open the application on the terminal | Run the command ***$ ./run.py*** | Hi! Welcome to an application that help you manage your credential ... * ca --- Create account details here |
|               Select ***ep***        | enter your own password     | Welcome ***username*** to password locker.Your new account password is: ***password***|
|Store a new credential in the application|   Enter ***cc***              |   Enter Account, username, password choose ***tp*** to enter your password or ***gp*** for the application to generate a password for you |
| Display all stored credentials       |           Enter ***dc***         | A list of all credentials that has been stored or You don't have any credentials saved yet|
|Find a stored credential based on account name|    Enter ***fc***        |Enter the Account Name you want to search for and returns the account details|
|Delete an existing credential that you don't want anymore| Enter ***Dd*** |Enter the account name of the Credential you want to delete and returns true if the account has been deleted and false if the account doesn't exist|
|  Exit the application                |              Enter ***Ex***       | Exit application |


## Technology Used
* Python3.9.1

## Contact Informarion
If you have any question or contributions, please email me at [dannymyles1999@gmail.com] [dancun.wawire@student.moringaschool.com]

## License
* MIT License:

* Copyright (c) 2021 DannyMyles


