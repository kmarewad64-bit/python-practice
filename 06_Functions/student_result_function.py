def calculate_percentage(marks):
    total = sum(marks)
    percentage = (total / 500) * 100
    return percentage


def check_result(percentage):
    if percentage >= 40:
        return "Pass"
    else:
        return "Fail"


marks = [78, 85, 72, 88, 80]

percentage = calculate_percentage(marks)
result = check_result(percentage)

print("Marks:", marks)
print("Percentage:", percentage)
print("Result:", result)
