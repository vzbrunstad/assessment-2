# Assessment 2

## Competencies Covered
1. Reading / Writing to CSV
2. Code Cleanliness

**Note: You do not need to write Mamba tests for this**

## Backstory
You are a military recruiter in a major city and you would like to have a software program to manage new recruits. You do not know how to write data to a database so you decided to read and write to a CSV file.

### Release 0
Your OIC wants you to print out a list of all recruits. This is how they want it printed out:

```
Recruit 1: Jon Smith, born 01/01/1990, Marine Corps. Jon finished College and is being paid at the O-1 pay grade. Their closest relative is named Tom Smith.
```

### Release 1
You don't want to manually edit (add/remove) your CSV file every single time a new recruit comes into your office. You want your program to do it for you. Create funcitionality in your program to write (append) new recruits to your CSV.

**Hint:** You will probably need some `input` statements for this.

### Release 2
Your OIC wants you to create some search functionality. Given a name and birthdate, they want to be able to look up a specific recruit via the command line. If the given name and birthdate do not match up with anyone in the CSV, let your OIC know that as well.
