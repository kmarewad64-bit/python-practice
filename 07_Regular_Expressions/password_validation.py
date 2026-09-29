import re

password = "Python@123"

pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&*!]).{8,}$"

if re.match(pattern, password):
    print("Strong Password")
else:
    print("Weak Password")
