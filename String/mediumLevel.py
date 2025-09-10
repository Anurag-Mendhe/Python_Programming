"""
Q1) Count number of words using split()
String: "Docker makes applications portable and lightweight"

Q2) Check startswith / endswith
String: "Hello DevOps World"

Q3) Find first occurrence of "is"
String: "This is a Linux distribution and it is stable"

Q4) Capitalize first letter only
String: "welcome to kubernetes"

Q5) Join list into string
List: ["DevOps", "means", "collaboration"]

Q6) Use format_map() with a dictionary:
data = {"service": "Docker", "status": "running"}
Print: "Service Docker is currently running"

Q7) You have a dict:
log = {"level": "ERROR", "code": 500, "msg": "Internal Server Error"}
Use format_map() to print: "Log [ERROR] - Code: 500 - Message: Internal Server Error"

Q8) Write a program that takes a dict of environment variables:
env = {"USER": "devops", "SHELL": "/bin/bash"}
and prints: "User devops is using shell /bin/bash"
"""

# count number of words using split
string1 = "Docker makes applications portable and lightweight"
words = string1.split()
count = len(words)
print("Words count : ",count)
print("\b")

# check
string2 = "Hello DevOps World"
print("startswith 'Hello' ? ",string2.startswith("Hello"))
print("endswith 'World' ? ",string2.endswith("World"))
print("\b")

# find 
string3 = "This is a Linux distribution and it is stable"
print(string3.find("is"))
print("\b")

# Capitalize
string4 = "welcome to kubernetes"
print(string4.capitalize())
print("\b")

# Join
string5 = ["DevOps", "means", "collaboration"]
print(" ".join(string5))
print("\b")

# Use format_map()
data1 = {"service": "Docker", "status": "running"}
string6 = "Service {service} is currently {status}".format_map(data1)
print(string6)
print("\b")

# Use format_map()
log = {"level": "ERROR", "code": 500, "msg": "Internal Server Error"}
string7 = "Log [{level}] - Code: {code} - Message: {msg}".format_map(log)
print(string7)
print("\b")

# Use format_map()
env = {"USER": "devops", "SHELL": "/bin/bash"}
string8 =  "User {USER} is using shell {SHELL}".format_map(env)
print(string8)

