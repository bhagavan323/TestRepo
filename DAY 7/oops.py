# Example 1: create class
# class is a collection of variables(attributes) and methods(Behaviour)
#  Function - we can create without class
# Method -- inside the calss is method
# class is logical entity
# class is a blue print


# class My_class:
#     def my_method(self):
#         pass
#     def disply(self):
#         print("John")
#
# mc1=My_class()
# mc2=My_class()
#
# mc1.my_method()
# mc1.disply() # john


# Example 2:
# class my_class():
#     def m1(self):
#         print("This is instance method..")
#     @staticmethod
#     def m2(self,num):
#         print(self,num)
#
# mc1=my_class()
# mc1.m1()
# mc1.m2(100,200)  # 100 200 here colling static method directly using class not through object


# Example 3 how
# class myclass():
#     a,b=10,20  # class variables
#     def add(self):
#         print(self.a+self.b)
#     def mul(self):
#         print(self.a*self.b)
#
# mc=myclass()
# mc.add()  # 30
# mc.mul()  # 200

# Example 4
# i,j=15,25  # global variables
# class myclass:
#     a,b=10,20  # class variables
#     def add(self,x,y):  #
#         print(x+y)  # Here x,y are local variables
#         print(self.a+self.b)  # a,b are class variables
#         print(i+j)  # i, j are global variables
#
# mc=myclass()
# mc.add(100,200)


# Example 5
# a,b=15,25  # global variables
# class myclass:
#     a,b=10,20  # class variables
#     def add(self,a,b):
#         print(a+b)
#         print(self.a+self.b)
#         print(globals()['a']+globals()['b'])  # global variables
#
# mc=myclass()
# mc.add(100,200)

# Example 6: one class can have multiple objects
# class myclass:
#     def display(self,name):
#         print("This is display method")
#         print(name)
# obj1=myclass()
# obj1.display("John")
# obj2=myclass()
# obj2.display("scott")


# Example 7 constructor
# class myclass:
#     def __init__(self):
#         print("This is constructor..")
#     def m1(self):
#         print("Hello..")
#     def m2(self,x,y):
#         return(x+y)
#
# mc=myclass()  # invoke constructor automatically
# mc.m1()  # method we have call explicitly by using object
# print(mc.m2(10,20))

# Example 8

# class Myclass:
#     name="John"
#     def __init__(self,name):  # constructor expecting one argument
#         print(name)
#         print(self.name)
#
# mc=Myclass("Dovid") # passing parameter to the constructor


# Example 9
# req : EMP
# constructor : eid,ename,sal
# display() : print eid, ename,sal
# class emp:
#     def __init__(self,eid,ename,sal):
#         self.eid=eid
#         self.ename=ename
#         self.sal=sal
#
#     def display(self):
#         print(self.eid,self.ename,self.sal)
#
# e1=emp(101,"John",50000)
# e1.display() # 101 John 50000
#
# e2=emp(102,"Scoot",10000)
# e2.display() # 102 Scoot 10000


#Example 10
# req : EMP
# constructor : eid,ename,sal
# constructor : print eid, ename,sal
# class emp:
#     def __init__(self,eid,ename,sal):
#         self.eid=eid
#         self.ename=ename
#         self.sal=sal
#
#     def __str__(self):
#         return(self.ename,self.sal)  # invalid becoz __str__() returns only string data
#
#
# e1=emp(101,"John",50000)
# print(e1)







