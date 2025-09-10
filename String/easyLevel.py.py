'''
Q1) Convert to lowercase/uppercase/title case
String: "DeVoPs AuToMaTiOn"

Q2) Remove leading/trailing spaces
String: " /var/log/syslog "

Q3) Count how many times "a" appears
String: "Ansible manages automation and applications"

Q4) Check alphabetic, digit, alphanumeric
String: "k8sCluster123"

Q5) Replace spaces with -
String: "Continuous Integration Continuous Deployment" 

Q6) Use format() to print:
"Container nginx is running on port 8080"
(values: "nginx", 8080)

Q7) Use keyword arguments in format() to print:
"User admin has logged in from 192.168.1.10"
(keys: user="admin", ip="192.168.1.10")

Q8) Format a string using index positions:
"Service mysql failed on server2"
(args: "server2", "mysql")
'''

# case function
string1 = "DeVoPs AuToMaTiOn"
print("Lower Case : "   ,string1.lower())
print("Upper Case : "   ,string1.upper())
print("Title Case : "   ,string1.title())
print("Capital Case : " ,string1.capitalize())
print("\b")

# stripe function
string2 = " /var/log/syslog "
print("After strip :"   ,string2.strip())
print("\b")

# count function
string3 = "Ansible manages automation and applications"
print("Count for a is : ",string3.count("a"))
print('\b')

# check function
string4 = "k8sCluster123"
print("Isalpha ? : ",string4.isalpha())
print("isdigit ? : ",string4.isdigit())
print("isalnum ? : ",string4.isalnum())
print("\b")

# replace function
string5 = "Continuous Integration Continuous Deployment"
print("Replace : ",string5.replace(" ","-"))
print("\b")

# formating
string6 = "Container {} is running on port {}".format("nginx", 8080)
print(string6)
print("\b")

#key-word arguments
string7 ="User {user} has logged in from {ip}".format(user="admin", ip="192.168.1.10")
print(string7)
print("\b")

# format string using index position
string8 = "Service {1} failed on {0}".format("server2", "mysql")
print(string8)
