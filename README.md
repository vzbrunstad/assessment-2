# Assessment 2: Object Oriented Programming + CSV Reading/Writing
- **Video Inventory Manager**

## Important Grading Information
- Make sure you read the [Assessment-2 Grading Rubric](https://docs.google.com/spreadsheets/d/1AlAQukmB3SS7IyW2hu0zY-9RaQnHY3lLeTi2O1fUb30/edit?usp=sharing).
  - Application Correctness (40%)
  - Code Design (40%)
  - CSV Files (10%)
  - Testing (10%)
- This assessment is worth 15% of your final grade. You need to get a 75% or better to pass. (You must pass all assessments in order to graduate Code Platoon's program.)
- If you fail the assessment, you have can retake it once to improve your score. For this assessment... 
  - *5% penalty*: If you complete and submit the retake **within one week** of receiving your grade. 
  - *10% penalty*: If you complete and submit the retake **by 8:30am, July 12th, 2021** (end of the middle week break). A retake for this assessment WILL NOT be accepted after this date.

## Rules / Process
- This test is fully open notes and open Google, but is not to be completed with other students
- Push your solution up to your personal Github. Do not submit a pull request. 

## Requirements
- This assessment should be completed using Python.

## Challenge
*Back in the day*, humans would actually leave their homes to go rent a physical video copies of movies (what a strange concept, right?). Blockbuster was the leading video rental company in this era. Today, there is only one Blockbuster location left which is located in Bend, Oregon. Today, we are going to ask you to build a video inventory application for this Blockbuster!

Your Video Inventory Management application should be able to:
- Manage customer information:
  - customer id
  - first name
  - last name
  - current list of video rentals (by title)
- Manage the store's video inventory:
  - video id
  - video title
  - number of copies currently available
- Allow a video rental to be rented out to a customer
  - NOTE: Customer must be limited to a maximum of 3 rentals at a time. Your application should ensure no customer can exceed this limit.
- Allow a video rental to be returned from a customer
- Read application data from CSV files
- Write application data out to CSV files

Give careful consideration into what  data structures & data types (classes) you might need to use. Also, your application should always keep the CSV data files updated! We need data records to be backed up, in case our application were to crash (and lose data internally).

Your application should have a menu interface that allows:
- Viewing the current video inventory for the store
- Viewing a customer's current rented movies
  - *by id*
- Renting a movie to a customer
  - *by title*
- Returning a movie from a customer
  - *by title*
- Adding a new customer
  - You should not have an initial list of video rentals assigned to a newly created customer
- Exiting the application

Your menu should look something like this: 
```
Welcome to Code Platoon Video!
1. View entire video inventory
2. View customer's rented movies
3. Rent video
4. Return video
5. Add new customer
6. Exit
```
