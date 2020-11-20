import re
test_text = "6 - 9:30 AM - 10:30 AM - 2 PM - 5 PM - 9 PM"
print(re.sub(r'(\s|^)(\d+)(\s)', r'\1\2:00\3', test_text))