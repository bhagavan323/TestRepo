# # Example 1 : How to create a list
# A list is a collection which is ordered abd changeable

# mylist=[10,20,30,40]
# mylist2=["Apple","Banana","Cherry"]
# mylist3=["Apple",10,"Banana",20]
# mylist4=list() # Empty list
#
# print(mylist)
# print(mylist2)
# print(mylist3)
# print(mylist4)

# Accesing items from the list
# mylist=["Apple","Banana","Cherry"]  # index starts from 0
# # in list every item is identified by index number
# print(mylist[0]) # Apple
# print(mylist[2]) # Cherry
# print(mylist[-1]) # Cherry
# print(mylist[-2]) # Banana

# Example 3: Range of indexes
# mylist=["Apple","Banana","Cherry","Orange","Kiwi","Melon","Mango"]
# print(mylist[2:5])  # ['Cherry', 'Orange', 'Kiwi']
# print(mylist[-4:-1]) # ['Orange', 'Kiwi', 'Melon']

# Example 4: How to change the item value
# mylist=["Apple","Banana","Cherry",]
# print(mylist)   # ['Apple', 'Banana', 'Cherry']
#
# mylist[0]="Orange" # This will change the values based on index
# print(mylist) # ['Orange', 'Banana', 'Cherry']
#

# Example 5 : How to read list items using loop
# mylist=["Apple","Banana","cherry"]
# for i in mylist:
#     print(i)

# Example 6: Check if the item is exist in the list or not

# mylist=["Apple","Banana","Cherry"]
# if "Apple" in mylist:
#     print("Yes. Apple is present")
# else:
#     print("No. Apple is not present")
#

# Example 7: List Length (counting number of items in a list using len() function
# mylist=["Apple","Banana","cherry"]
# print(len(mylist))

# Example 8 : Add items in the list we have 2 functions are available 1 append()  2 insert()
# mylist=["Apple","Banana","cherry"]
# print(mylist)
# #mylist.append("Orange") # Adding new item at the end of the list
# #print(mylist) # ['Apple', 'Banana', 'cherry', 'Orange']
# mylist.insert(1,"Orange")
# print(mylist)


# Example 9 : Remove items from the list 3 methods are available 1.pop() function 2. del keyword 3. clear() function

# pop()
# mylist=["Apple","Banana","cherry"]
# mylist.pop(0) # here we must specify the index number not the item
# print(mylist) # ['Banana', 'cherry']

# Del Keyword
# mylist=["Apple","Banana","cherry"]
# del mylist[2]   # Here del command removes single item based on the index
# print(mylist) # ['Apple', 'Banana']

# Clear() Function

# mylist=["Apple","Banana","cherry"]
# mylist.clear()
# print(mylist) # []

# Example 10 : Copy list using copy() function

# mylist1=["Apple","Banana","cherry"]
# mylist2=list(mylist1)
#
# print(mylist1) # ['Apple', 'Banana', 'cherry']
#
# print(mylist2) # ['Apple', 'Banana', 'cherry']

#  using copy() function
# mylist1=["Apple","Banana","cherry"]
# mylist2=mylist1.copy()
# print(mylist1) # ['Apple', 'Banana', 'cherry']
#
# print(mylist2) # ['Apple', 'Banana', 'cherry']
#

# Example 11 : Combine/ Join lists 1. using + operator, 2. using looping statement  3.Extend() function
# using + operator
# list1=['a','b','c']
# list2=[1,2,3]
# list3=list1+list2
# print(list3) # ['a', 'b', 'c', 1, 2, 3]

# using looping statement
# list1=['a','b','c']
# list2=[1,2,3]
# for i in list2:
#     list1.append(i)
# print(list1) # ['a', 'b', 'c', 1, 2, 3]

# By using Extend() function

list1=['a','b','c']
list2=[1,2,3]
list1.extend(list2)
print(list1) # ['a', 'b', 'c', 1, 2, 3]

