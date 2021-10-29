last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
#1. Create a list called subjects and fill it with the classes you are taking
subjects = ["physics", "calculus", "poetry", "history"]

#2. Create a list called grades and fill it with your scores
grades = [98, 97, 85, 88]
#3. Create a two-dimensional list to combine subjects and grades. Use the table below as a reference to associated values
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

#4. Print gradebook.
print(gradebook)

#5. Your grade for your computer science class just came in! You got a perfect score, 100!
# Use the .append() method to add a list with the values of "computer science" and an associated grade value of 100 to our two-dimensional list of gradebook.
gradebook.append(["computer science", 100])

#6. Your grade for "visual arts" just came in! You got a 93!
# Use append to add ["visual arts", 93] to gradebook.

gradebook.append(["visual arts", 93])

#7. Our instructor just told us they made a mistake grading and are rewarding an extra 5 points for our visual arts class.
# Access the index of the grade for your visual arts class and modify it to be 5 points greater
gradebook[5][1] = 98

#8. You decided to switch from a numerical grade value to a Pass/Fail option for your poetry class.
# Find the grade value in your gradebook for your poetry class and use the .remove() method to delete it.
gradebook[2].remove(85)

#9. Use the .append() method to then add a new "Pass" value to the sublist where your poetry class is located.
gradebook[2].append("Pass")
print(gradebook)

#10. You also have your grades from last semester, stored in last_semester_gradebook.
# Create a new variable full_gradebook that combines both last_semester_gradebook and gradebook using + to have one complete grade book.
# Print full_gradebook to see our completed list.

last_semester_gradebook = [88, 90, 78, 54, 99, 98]
full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)