# Example 1: Creating Dictionary

# my_dic={101:'x',102:'y',103:'z'}
# print(my_dic)

# Example 2: Access items from dictionary
# my_dic={
#     "Brand": "Hyundai",
#     "Model": "i10",
#     "Year": 2021
# }
# print(my_dic["Brand"]) # Hyundai
# # Using get() function
# x=my_dic.get("Brand")
# print(x)

# Example 3: Change values in the dictionary

# my_dic={
#        "Brand": "Hyundai",
#        "Model": "i10",
#        "Year": 2020
#  }
# my_dic["Year"]=2021
# my_dic["Model"]="i20"
# print(my_dic) # {'Brand': 'Hyundai', 'Model': 'i20', 'Year': 2021}

# Example 4: Reading items from dictionary using loop
# my_dic={
#     "Brand": "Hyundai",
#     "Model": "i10",
#     "Year": 2021
#}

# for i in my_dic:
#     print(i)    # it prints only keys from the dictionary (Brand Model Year)

# for i in my_dic:
#     print(my_dic[i]) # is prints only values from the dictionary

# for i in my_dic.values():
#     print(i) # is prints only values from the dictionary

# for x,y in my_dic.items():
#     print(x,y)
# Output
# """Brand Hyundai
# Model i10
# Year 2021"""

# Example 5: check key is exist in the dictionary or not
# my_dic = { "Brand": "Hyundai","Model": "i10", "Year": 2021 }
# print(my_dic)
# if "Model" in my_dic:
#     print("exist")
# else:
#     print("not exist")
# print("Model" in my_dic)

# Example 6: find number of items in dictionary

# my_dic = { "Brand": "Hyundai","Model": "i10", "Year": 2021 }
# print(len(my_dic)) # 3

# Example 7: adding items to dictionary
# my_dic = { "Brand": "Hyundai","Model": "i10", "Year": 2021 }
# my_dic["colour"]="Red"
# print(my_dic)

# Example 8: Remove item from the dictionary

# my_dic = {'Brand': 'Hyundai', 'Model': 'i10', 'Year': 2021, 'colour': 'Red'}
# my_dic.pop("Year")
# print(my_dic) # {'Brand': 'Hyundai', 'Model': 'i10', 'colour': 'Red'}
# del my_dic["colour"]
# print(my_dic) # {'Brand': 'Hyundai', 'Model': 'i10'}
# my_dic.clear()
# print(my_dic) # {}

# Example 9: copying one dic to another dictionary
my_dic = {'Brand': 'Hyundai', 'Model': 'i10', 'Year': 2021, 'colour': 'Red'}
mu_dic2=my_dic.copy()
print(mu_dic2)