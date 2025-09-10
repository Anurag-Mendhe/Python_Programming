A string in Python is a sequence of characters enclosed in either:
1.Single quotes ' '
2.Double quotes " "
3.Triple quotes ''' ''' or """ """ (for multi-line strings)

While Python has 47 string methods, in real coding we mostly use a small set of commonly needed ones.
Here are the most commonly used string functions (with examples):
---------------------------------------------------------------------------------------------------------
🔹 1. Case Conversion

lower() → Convert to lowercase
"HELLO".lower()   # 'hello'

upper() → Convert to uppercase
"hello".upper()   # 'HELLO'

title() → Convert to title case
"hello world".title()   # 'Hello World'

capitalize() → First letter uppercase
"python".capitalize()   # 'Python'
---------------------------------------------------------------------------------------------------------
🔹 2. Trimming / Removing

strip() → Remove spaces (or given chars) from both ends
"  hello  ".strip()   # 'hello'

lstrip() / rstrip() → Remove from left / right
---------------------------------------------------------------------------------------------------------
🔹 3. Searching

find(sub) → First index (or -1 if not found)
"python".find("th")   # 2

count(sub) → Count occurrences
"banana".count("a")   # 3

startswith() / endswith() → Check beginning or ending
"python".startswith("py")   # True
---------------------------------------------------------------------------------------------------------
🔹 4. Replacing & Splitting

replace(old, new) → Replace substring
"hello world".replace("world", "Python")   # 'hello Python'

split() → Split into list
"a,b,c".split(",")   # ['a', 'b', 'c']

join(iterable) → Join elements with separator
"-".join(["a", "b", "c"])   # 'a-b-c'
---------------------------------------------------------------------------------------------------------
🔹 5. Checking Types

isdigit() → All digits?
isalpha() → All letters?
isalnum() → Letters + digits?
isspace() → Only spaces?
isupper() → checks for upper
islower() → checks for lower
"123".isdigit()    # True
"hello".isalpha()  # True
"hello123".isalnum() # True
---------------------------------------------------------------------------------------------------------
🔹6. .format()
String formatting in Python is the process of creating a dynamic string by inserting values into a predefined text. 

i.f-strings (Formatted String Literals): f-strings provide a concise and efficient way to embed expressions inside string literals.
Variables and expressions are directly placed within curly braces {} inside an f-string, which is prefixed with an f or F.
name = "userName"
print(f"{name} is logged in")
---------------------------------------------------------------------------------------------------------
ii. .format() method: This method is available on string objects and allows for placeholders (curly braces {}) within a string to be replaced by arguments passed to the .format() method. 
Placeholders can be empty, numbered, or named
message = "You bought {} {} for ${:.2f} each.".format(quantity, item, price)
---------------------------------------------------------------------------------------------------------
# Positional arguments
msg = "Hello, {}. Welcome to {}.".format("Engineer", "DevOps")
print(msg)
# Output: Hello, Engineer. Welcome to DevOps.
---------------------------------------------------------------------------------------------------------
# Index-based arguments
msg = "Service {1} failed on {0}".format("server1", "nginx")
print(msg)
# Output: Service nginx failed on server1
---------------------------------------------------------------------------------------------------------
# Keyword arguments
msg = "User: {user}, Role: {role}".format(user="admin", role="DevOps Engineer")
print(msg)
# Output: User: admin, Role: DevOps Engineer
---------------------------------------------------------------------------------------------------------
🔹7. format_map(mapping)

This is like .format(), but it directly takes a dictionary (mapping object).
It’s faster and simpler when you already have values in a dict.

✅ Examples
data = {"user": "root", "ip": "192.168.1.1"}

msg = "User {user} logged in from {ip}".format_map(data)
print(msg)
# Output: User root logged in from 192.168.1.1
---------------------------------------------------------------------------------------------------------
✅ Summary of Most Used Functions

Case conversion → lower(), upper(), title(), capitalize()
Trimming → strip(), lstrip(), rstrip()
Searching → find(), count(), startswith(), endswith()
Replacing/splitting → replace(), split(), join()
Checking type → isdigit(), isalpha(), isalnum(), isspace()s.
format(*args, **kwargs) – String formatting.
format_map(mapping) – Formatting with dict directly.
