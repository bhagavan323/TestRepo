# Example 1 : TupleDemo
# mytuple=("Apple","Banana","Cherry")
# print(mytuple)

# Example 2 Access tuple items

# mytuple=("Apple","Banana","Cherry")
# print(mytuple[1])

# Example 3 : range of indexes
#
# mytuple=("Apple","Banana","Cherry","Orange","Kiwi","Melon","Mango")
# print(mytuple[2:5]) # ('Cherry', 'Orange', 'Kiwi')
# print(mytuple[-4:-1]) # ('Orange', 'Kiwi', 'Melon')

# Example 4 : Changing tuple items
# by default tuple does not allow you change values because it is immutable
#  but there is work around
# tuple---> list(Modify)--->tuple
# mytuple=("Apple","Banana","Cherry")
# mylist=list(mytuple)
# mylist[0]="Orange"
# mytuple=tuple(mylist)
# print(mytuple)  # ('Orange', 'Banana', 'Cherry')
#
# Example 5 : Reading tuple items using loop
# mytuple=("Apple","Banana","Cherry")
# for i in mytuple:
#     print(i)
# Example 6 : check if item exists (Searching of item in tuple)
# mytuple=("Apple","Banana","Cherry")
# if "Banana123" in mytuple:
#     print("yes, Banana is present")
# else:
#     print("no, Banana is not present")

# Example 7 : find the tuple length - counting items in a tuple
# mytuple=("Apple","Banana","Cherry")
# print(len(mytuple)) # 3
# Example 8 : Add items to tuple - not possible because tuple is immutable - cannot change vales/item
# mytuple=("Apple","Banana","Cherry")
# mytuple[0]="Orange"
# print(mytuple) # TypeError: 'tuple' object does not support item assignment

# Example 9 : copy tuple
# mytuple=("Apple","Banana","Cherry")
# mytuple2=mytuple
# print(mytuple2) # ('Apple', 'Banana', 'Cherry')
# print(mytuple) # ('Apple', 'Banana', 'Cherry')

# Example 10 : Removing items from tuple - connot possible because tuple is immutable
# mytuple=("Apple","Banana","Cherry")
# # mytuple.remove("Apple")
# print(mytuple)
# del mytuple
# print(mytuple) # NameError: name 'mytuple' is not defined.

# Example 11 : joining/combine tuples
# tuple1=(10,20,30)
# tuple2=('a','b','c')
# tuple3=tuple2+tuple1
# print(tuple3)

 # Example 12 : Tuples Comparison


# tuple1=(10,20,30)
# tuple2=('a','b','c')
# if tuple1==tuple2:
#     print("tuples are equal")
# else:
#     print("tuples are not equal")


