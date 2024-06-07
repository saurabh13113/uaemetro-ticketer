# uaemetro-ticketer
Highschool Project that allows customers to purchase UAE metro tickets

Use PDF File to understand Nuances of Project.

Rough project breakdown:

1. WELCOME PAGE
   First you are greeted with the intricate welcome
   graphic using turtle module.
   We are then taken to the welcome screen, of the metro
   where it shows us a picture of the metro in action as
   well as a brief description of it. And the option to
   continue onto the login screen.
   
2. LOGIN PAGE :-
   In the login screen there are 2 modes of logging in: Customer and Administrator.
   For the Administrator one we will need to enter the specific username and password to continue onto the
   admin user face.
   
3. CUSTOMER INTERFACE :-
   If we continue onto the customer login screen and the
  ticket rates for the different destinations.
  There are 2 buttons and 5 entry fields each with a
  particular function assigned to it:
    i. NAME:- To enter customer name
    ii. DESTINATION:- To enter desired destination
    iii. NO OF TICKETS:- To enter quantity of tickets to be purchased
    iv. TICKET TYPE:- To enter whether it’s a oneway or return ticket
    v. DISCOUNT:-
          1. NO DISCOUNT
          2. GOVT EMPLOYEE-50% discount
          3. SENIOR CITIZEN-25% discount
    CLEAR BUTTON:- Clears all of the entered fields to be used incase of an error
    SUBMIT BUTTON:- Gets input and computes data to calculate final bill and display it to customer
   
   
5. ADMINISTRATOR INTERFACE
  You must enter the correct username and password to be able to access the Administrator functions.
  There is the usual customer interface but additionally there are the following administrator privileges.

  SEARCH BUTTON:-Administrator can enter particular name and search for that customer record. If found will display all details of that customer.
  UPDATE BUTTON:- Administrator can enter particular name and enter updated details then on clicking button the details are updated in record.
  DISPLAY BUTTON:- Administrator can display and view all customer records
  DELETE BUTTON:- Administrator can enter particular name and on pressing button the particular record will be deleted

Needed imports/packages:

=> MySQL Connector: To import and store data from project into MySQL databse(if needed)
=> Turtle/Tkinter: For the GUI and animations in the app to function.

