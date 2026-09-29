def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average


marks = [78, 85, 92, 88, 75]

average = calculate_average(marks)

print("Marks:", marks)
print("Average Marks:", average)
