# Example 1:
# global_var = 10 # global variable
#
# def function():
#     local_var = 20 # Local variable
#     print(local_var)
#     print(global_var)
# # local variables only can access with in the function
# function()
# print(local_var)  # invalid because local_var is local variable of function()
# print(global_var) # valid because global_var is global variable
#

# Example 2:
# xy=100  # global variable
# def cool():
#     xy=200  # local variable
#     print(xy)
# cool() # 200


# Example 3: using global variable in local variable and update value

# xy=100  # global variable
# def cool():
#     global xy
#     xy=200   # global variable
#     print(xy)
# cool()  # 200






