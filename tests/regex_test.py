strings = ["abcdef", "abcd:", "abc:", "bc", "a", "b", "c", "abcde"]
import re

# getting all the strings of length greater than 3
matches = []
for string in strings:
    pattern = re.compile(r'\w{4,}$')
    match = re.match(pattern, string)
    if match is not None:
        ## print(match.group(0))
        matches.append(match.group(0))
        

##for match in matches:
##    print(match)

# getting all the strings starting with a only
matches = []
for string in strings:
    pattern = re.compile(r'a[a-z]+:$')
    match = re.match(pattern, string)
    if match is not None:
        matches.append(match.group(0))

for match in matches:
    print(match)