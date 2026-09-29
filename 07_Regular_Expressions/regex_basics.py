import re

text = "I am learning Python and Python is useful for Data Analytics."

pattern = "Python"

matches = re.findall(pattern, text)

print("Text:", text)
print("Matching Words:", matches)
print("Number of Matches:", len(matches))
