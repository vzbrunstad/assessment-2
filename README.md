# Assessment 2: Object Oriented Programming + CSV Reading/Writing

## Important Grading Information
* TODO PUT RUBRIC HERE
* This assessment is worth 15% of your final grade. You need to get a 75% or better to pass.
* If you fail the assessment, you can retake it once within 2 weeks. If you retake it within 7 days, a 5% penalty will be enacted. If you retake it between 8-14 days, a 10% penalty will be enacted. We will not regrade passing assessments.

## Rules / Process
* This test is fully open notes and open Google, but is not to be completed with other students
* Do not open a pull request against this repository. We will evaluate your code individually with you.

## Challenge
We are going to be building video inventory software for the last Blockbuster in Bend, Oregon. We will create 2 classes and have them interact with each other via a runner file.

Create a `User` class that keeps track of a user's first name, last name, their current outstanding reservations, and their previous reservations. Users should be able to rent up to 3 titles at a time and be able to return them. Next, create a `InventoryManager` class that keeps track of titles at the store and how many copies of each title they have. `User`s should be able to borrow titles if available, otherwise they should be notified that it is out of stock. Both classes should have their data persisted through a CSV file.

Finally, create a runner class that allows for a User to ask for the current inventory, see their current titles checked out, reserve a title, and return a title.
