# create string variable
# name=""
# name=''

# ways of creating string variable
# s="welcome"
# s='Welcome'
# s=str('Welcome')
# s=str("Welcome")
#
# # Creating empty string variable
# name=""
# name=''
# name=str()
# mutable - cannot change the vale of the variable
# immutable -can change the value of variable

# strings are immutable
# str="welcome"
# print(id(str))  # 2098740180976 id of the variable

# str1="welcome"
# print(id(str1))  # 1625341409200 id of the variable
# str1=str1+"to Pythone"
# print(id(str1)) # 1625346143328
# if the value is changed after updation, then it is immutable

# Example 3 : + and * with string
# str="Welcome"
# print(str+'programming')    # concatenation/joining  Welcomeprogramming
# print(str*3) # WelcomeWelcomeWelcome

# Example 4 Slicing []
# Starting index 0
# ending index 1
# str="Welcome"
# print(str[1:3]) # el
# print(str[:6])  # Welcom here starting index is 0 by default
# print(str[2:]) # lcome
# print(str[1:-1]) # elcom  -1 means which will remove the last one character
# print(str[1:-2])    # elco -2 means which will remove the last two characters

# Example 5 : ord() and chr()
# print(ord('A')) # 65 # returns the ASCII code of the character
# print(chr(65))  # A  # returns character represented by a ASCII number.

# Example 6 : max() min() len()
# print(max("abc")) # C
# print(min("abc"))   #a
# print(len("abc")) # 3

# Example 7 : in not in operators
# s="Welcome"
# # print("come" in s)  # TRUE
# # print("lome" in s)  # False
#
# print("come" not in s)  # false
# print("lome" not in s)  # True

# Example 8 : String comparison
# print("tim" == "tie") # false
# print("free" != "freedom") # True
# print("arrow" > "aron") # True
# print("right" >= "left") # True

# # Example 9 : Testing strings  True/false
# s="Welcome to Python"
# print(s.isalnum()) # False
# print("Welcome".isalpha())  # true
# print("2021".isdigit()) # True
# print("first Number".isidentifier()) # False
# print(s.islower()) # True
# print("WELCOME".isupper()) # True
# print(s.isspace()) # False
# Example 10 : Searching for substrings
# s="Welcome to Python"
# print(s.endswith("thon")) # True
# print(s.startswith("good")) # false
# print(s.find("come"))   # 3
# print(s.find("become")) # -1 not fount
# print(s.count("t")) #2

# Example 11 : Converting string
# s="String in PYTHON"
# s1=s.capitalize()
# print(s1)
# s2=s.title()
# print(s2)
# s3=s.lower()
# print(s3)
# s4=s.upper()
# print(s4)
# s5=s.swapcase()
# print(s4)
# s5=s.replace("in","on")
# print(s5)


# EXAMPLE 12 : Reverse a string
# method 1
# s="Welcome"
# rev_str=""
# for i in s:
#     rev_str=i+rev_str
# print("Reversed string is:",rev_str)

# Method 2
s="welcome"
rev_str=s[::-1] # s[starting:ending:-1] s[0:7:-1]
print(rev_str)  # emoclew









