import re

pattern = input()

if re.match("1", pattern[0]) or re.match("8", pattern[0]) or re.match("9", pattern[0]) and len(pattern) == 8:

    print("Valid")

else:

    print("Invalide")
