# Assessment 2: Object Oriented Programming + CSV Reading/Writing
- **Inventory Manager**

## Important Grading Information
- Make sure you read the [Assessment-2 Grading Rubric](https://docs.google.com/spreadsheets/d/1AlAQukmB3SS7IyW2hu0zY-9RaQnHY3lLeTi2O1fUb30/edit?usp=sharing).
- This assessment is worth 15% of your final grade. You need to get a 75% or better to pass. (You must pass all assessments in order to graduate Code Platoon's program.)
- If you fail the assessment, you have can retake it once to improve your score. For this assessment... 
  - 5% penalty: If you complete and submit the retake **by 8:30am, July 12th, 2021** (end of the middle week break).
  - 10% penalty: If you complete and submit the retake afterwards.

## Rules / Process
- This test is fully open notes and open Google, but is not to be completed with other students
- Do not open a pull request against this repository. We will evaluate your code individually with you.

## Requirements
- This assessment should be completed using Python.

## Challenge
We are going to be building video inventory software for the last Blockbuster in Bend, Oregon. We will create 2 classes and have them interact with each other via a runner file.

Create a `User` class that keeps track of a user's first name, last name, their current rented movies. Users should be able to rent up to 3 titles at a time and be able to return them. Next, create a `InventoryManager` class that keeps track of titles at the store and how many copies of each title they have. `User`s should be able to rent movies if available, otherwise they should be notified that it is out of stock. Both classes should have their data persisted through a CSV file.

Finally, create a runner class that allows for a User to ask for the current inventory, see their current movies checked out, rent a movie, and return a movie.

```
Welcome to Code Platoon Video!
1. View a user's rented movies
2. See available titles & quantity
3. Rent a movie
4. Return a movie
```
