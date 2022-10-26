# LoginSys

## The Program

#### This program is written in Python. It utilizes Tkinter to provide a GUI. It uses a MongoDB database stored on the local machine to perform login credential lookups.

#### This program performs the login and registration functionalities of a login system. 

#### Login registration functionalities include accepting a username and password from the Login Registration frame's username and password entry fields and checking the username input against existing usernames in the database to ensure an account does not already exist. If any condition is not met, a message in red describing the issue is printed at the bottom of the frame, and after 2000 milliseconds, the user is redirected to an unfilled login registration frame. If the conditions are met, a message in green confirming login registration success is printed at the bottom of the frame, and after 2000 milliseconds, the user is directed to the Login frame.

#### Login functionalities include accepting a username and password from the Login frame's username and password entry fields and comparing the login credentials with those stored in the database. If matching credentials are not found, a message in red notifying the user of an incorrect login is printed at the bottom of the frame, and after 2000 milliseconds, the user is redirected to an unfilled login frame. If the query results in a match, a message in green confirming login success is printed at the bottom of the frame, and after 1000 milliseconds, the program is closed.
