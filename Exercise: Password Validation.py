# Create a password validation tool.
# Password must be at least 8 characters long.
# Password can contain any sort of letters and numbers.
# Password can only have these symbols: $%#@

import re

password_pattern = re.compile(r"[a-zA-Z0-9#@$%]{8,}\d$")
password1 = 'sagsfad'
password2 = 'supersecret2023'

password_check1a = password_pattern.search(password1)
password_check1b = password_pattern.fullmatch(password1)

password_check2a = password_pattern.search(password2)
password_check2b = password_pattern.fullmatch(password2)


print(password_check1a)
print(password_check1b)

print(password_check2a)
print(password_check2b)
