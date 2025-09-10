"""
Q1) Print only alphabetic words
String: "Deploy v2.0 on server-1 at 10pm"

Q2) Check valid password
String: "DevOps123"

Q3) Replace "python" with "Java" and uppercase
String: "I love python scripting in DevOps"

Q4) Check digit string before/after strip
String: " 8080 "

Q5) Count uppercase & lowercase letters
String: "GitHuB aCtIoNs"

Q6) Use format() with alignment and padding to make a table-like output:

Service     Status
nginx       running
mysql       stopped
(Hint: "{:<10}" for left align, "{:>10}" for right align).

Q7) Create a log string using format_map() from a dict:
log = {"time": "2025-09-09 14:00", "level": "INFO", "service": "k8s"}
Output: "2025-09-09 14:00 | INFO | Service: k8s"

"""

string1 = "Deploy v2.0 on server-1 at 10pm"
print("Printing only alphabets from string ")
l = string1.split(" ")
for i in l:
    if (i.isalpha()):
        print(i)
print("\b")

string2 = "DevOps123"
if string2.isalnum():
    print("It is a valid Password")
else:
    print("Invalid Password")
print("\b")

string3 = "I love python scripting in DevOps"
m = string3.replace("python","Java")
n = m.upper()
print(n)
print("\b")

string4 = " 8080 "
print("Check isdigit before strip : ",string4.isdigit())
a = string4.strip()
print("Check isdigit after strip : ",a.isdigit())
print("\b")

string5 = "GitHuB aCtIoNs"
countUP = 0
countDW = 0
for i in string5:
    if i.isupper():
        countUP += 1
    else:
        countDW += 1
print("Count of upperCase : ",countUP)
print("Count of lowerCase : ",countDW)
print("\b")

# format using padding and alignment
print("{:<10} {:<10}".format("Service","Status"))
print("{:<10} {:<10}".format("ngnix","running"))
print("{:<10} {:<10}".format("mysql","stopped"))
print("\b")

# format_map
log = {"time": "2025-09-09 14:00", "level": "INFO", "service": "k8s"}
string7 = "{time} | {level} | Service: {service}".format_map(log)
print(string7)
print("\b")
