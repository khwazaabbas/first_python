import re
pattern = "^a...s$"
text_string = "abbas"
result = re.match(pattern, text_string)
if result:
    print("match succfully found")
else:
    print("match n ot found")