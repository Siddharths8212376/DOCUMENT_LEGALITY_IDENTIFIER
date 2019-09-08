del_strings = [ "\n", "\t", "\r"]

strings = ["Siddharth"," \nMiddle", "\r\t\nKid", "\n", "Indent\n\r"]
lis = []
for string in strings:
    for del_ in del_strings:
        if del_ in string:
            string = string.replace(del_, "")
    lis.append(string)
print(lis)
mid = "siddharth"
mid = mid.replace("si", "is")
print(mid)