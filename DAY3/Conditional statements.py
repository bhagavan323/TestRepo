# Example 1
# age=20
# if age>=18:
#     print("eligible for vote")
# else:
#     print("Not eligible for vote")
#
# Example 2
# if True:
#     print("True condition")
# else:
#     print("False condition")
#
# # Example 3
# if 1:
#     print("one")
# else:
#     print('Not one')

# Example 4 Find a number is eve/odd num%2=0

# num=11
# if num%2==0:
#     print("Given Number is Even")
# else:
#     print("Given Number is odd")
#

# Example 5 if else in single line (Ternary operator)

# num=10
# print("Even number")if num%2==0 else print("odd number")

# Example 6 if else  - -- Multiple statement in the single line
# a=20
# {print("Hello"),print("Python")} if a>=10 else {("Hi"),print("Java")}
#
#

# Example 7 -- Multiple conditions using elif
weekno=int(input("Enter the week nos between 1 to 7:"))
# print(type(weekno))
if weekno==1:
    print("Sunday")
elif weekno==2:
    print("Monday")
elif weekno==3:
    print("Tuesday")
elif weekno==4:
    print("Wednesday")
elif weekno==5:
    print("Thursday")
elif weekno==6:
    print("Friday")
elif weekno==7:
    print("Saturday")
else:
    print("Invalid Week Number")

