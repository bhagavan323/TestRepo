# Example 1: Creating set
# myset={"Apple","Banana","Cherry"}
# myset1={"Panasonic","HP",100,10.5,}
# print(myset1) # {'Panasonic', 10.5, 100, 'HP'}
# print(myset) # {'Cherry', 'Apple', 'Banana'}

# Example 2:  Accessing items from set
# myset={"Apple","Banana","Cherry"}
# for i in myset:
#     print(i)

# Example 3: vale exists in set or not
# myset={"Apple","Banana","Cherry"}

# print("Banana" in myset)    # True
# print("banana1" in myset)    # False

# Example 4: Adding new items to set, we have two options 1. add() function 2. Update() function
# by using add() function we can add single item only
# by using update () function we can add multiple items

# myset={"Apple","Banana","Cherry"}
# myset.add('Orange')
# print(myset) # {'Banana', 'Orange', 'Cherry', 'Apple'}
# myset.update(["Mango","Grapes"])
# print(myset) # {'Apple', 'Orange', 'Cherry', 'Grapes', 'Banana', 'Mango'}


# Example 5: find number of items in a set using len() function

# myset={'Banana', 'Orange', 'Cherry', 'Apple'}
# print(len(myset)) # 4

# Example 6: Remove items from the set -remove() , discard() functions
# myset={'Banana', 'Orange', 'Cherry', 'Apple'}
# myset.remove('Banana')
# print(myset) # {'Cherry', 'Orange', 'Apple'}

# myset.remove('xyz')
# print(myset) # KeyError: 'xyz', which is not available from the set

# myset={'Banana', 'Orange', 'Cherry', 'Apple'}
# myset.discard('Banana')
# print(myset) # {'Cherry', 'Orange', 'Apple'}
# myset.discard('xyx') # will not throw any error
# print(myset)  # {'Banana', 'Orange', 'Apple', 'Cherry'}


# Example 7: to clear all items from set
# myset={'Banana', 'Orange', 'Cherry', 'Apple'}
# myset.clear()
# print(myset) # set()
# myset={'Banana', 'Orange', 'Cherry', 'Apple'}
# del myset
# print(myset) # NameError: name 'myset' is not defined

# Example 8: Joining two sets - union(), update()
# set1={'a','b','c'}
# set2={1,2,3}
# set3=set1.union(set2)
# print(set3) # {'a', 1, 2, 'c', 3, 'b'}

# set1={'a','b','c'}
# set2={1,2,3}
# set1.update(set2)
# print(set1) # {1, 'b', 2, 3, 'a', 'c'}
