skills = ["Python", "Excel", "Python", "Power BI", "Python", "Excel"]

frequency = {}

for skill in skills:
    if skill in frequency:
        frequency[skill] += 1
    else:
        frequency[skill] = 1

print("Skill Frequency:")

for skill, count in frequency.items():
    print(skill, ":", count)
