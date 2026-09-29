# Program to calculate student result

marks_obtained = 425
total_marks = 500

percentage = (marks_obtained / total_marks) * 100
remaining_marks = total_marks - marks_obtained

print("Marks Obtained:", marks_obtained)
print("Percentage:", percentage)
print("Remaining Marks:", remaining_marks)

print("Passed:", marks_obtained >= 250)
