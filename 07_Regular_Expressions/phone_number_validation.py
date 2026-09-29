import re

phone_number = "9876543210"

pattern = r"^[6-9]\d{9}$"

if re.match(pattern, phone_number):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")
