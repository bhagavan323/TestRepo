# 2 types are arguments/parameters we can pass to the function
#

# Example 1:
# def func(i,j):
#     print(i,j)
# func(10,20)  # positional arguments
# func(j=20,i=10) # keyword arguments  we are not consider the position
#

# Example 2: default values assigned to positional arguments

# def fun(i,j=10):
#     print(i,j)
# fun(100,200) # 100 200
# fun(100) # 100 10

# Example 3: keyword arguments
# def greetings(name,greetmsg):
#     print(greetmsg+"  "+name)
# greetings(name="John",greetmsg="Hello") # Hello  John
# greetings(greetmsg="Hello",name="John") # Hello  John

# Example 4:

# def fun(a,b,c):
#     print(a,b,c)
# fun(10,20,30) # positional parameters/arguments  # 10 20 30
# fun(a=10,b=20,c=30) # keyword parameters/arguments  # 10 20 30
# fun(b=20,c=30,a=10) # keyword parameters/arguments   10 20 30
# fun(10,20,c=30)  # 10 20 30 combination of positional and keyword arguments
# #fun(10,b=20,30)  #  This is wrong as positional argument must apper before any keyword argument  SyntaxError: positional argument follows keyword argument
# fun(10,30,b=20) # TypeError: fun() got multiple values for argument 'b', -- this is having logical error

# Example 5: function can return multiple values

# def largest(a,b):
#     if a>b:
#         return a,b
#     else:
#         return b,a
# print(largest(100,200)) # (200, 100)
# print(largest(20,10)) # (20, 10)
# res=largest(10,20)
# print(res) # (20, 10)
# print(type(res)) # tuple






