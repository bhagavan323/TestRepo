# Example 1
# class A:
#     def m1(self):
#         print("This is m1 method from class A")
#
#
# class B(A):
#     def m2(self):
#         print("This is m2 method from class B")
#
# bobj=B()
# bobj.m1() # This is m1 method from class A
# bobj.m2() # This is m2 method from class B

# Example 2 single inheritance

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x,self.y)
#
# class B(A):
#     a,b=100,200
#     def m2(self):
#         print(self.a+self.b)
#
# bobj=B()
# bobj.m1() # 10 20
# bobj.m2()  # 300


# Example 3 Multilevel inheritance

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=30,40
#     def m2(self):
#         print(self.a-self.b)
#
# class C(B):
#     i,j=5,10
#     def m3(self):
#         print(self.i*self.j)
#
# cobj=C()
# cobj.m1() # 30
# cobj.m2() # -10
# cobj.m3() # 50

# Example 4 Hierarchy inheritance


# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=30,40
#     def m2(self):
#         print(self.a-self.b)
#
# class C(A):
#     i,j=5,10
#     def m3(self):
#         print(self.i*self.j)
#
# bobj=B()
# bobj.m1() # 30
# bobj.m2() # -10
# cobj=C()
# cobj.m1() # 30
# cobj.m3() # 50

# Example 5 Multiple inheritance

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B:
#     a,b=30,40
#     def m2(self):
#         print(self.a-self.b)
#
# class C(A,B):
#     i,j=5,10
#     def m3(self):
#         print(self.i*self.j)
#
#
# cobj=C()
# cobj.m1() # 30
# cobj.m2() # -10
# cobj.m3() # 50

# Example 6
# class A:
#     def m1(self):
#         print("This is m1 method from class A")
#
# class B(A):
#     def m1(self):
#         print("This is m1 method from class B")
#         super().m1() # to invoke the parent class method
#
# bobj=B()
# bobj.m1() # This is m1 method from class B
#           # This is m1 method from class A

# Example 7
# class A:
#     a,b=10,20
#
# class B(A):
#     i,j=100,200
#     def m(self,x,y):
#         print(x+y) # local variable
#         print(self.i+self.j) # class variables
#         print(self.a+self.b) # class variables
#
# bobj=B()
# bobj.m(300,400)
# Example 8 Overriding variables
# class Parent:
#     name="Scoot"
#
# class Child(Parent):
#     name="John" # overriding the variable value
#
# cobj=Child()
# print(cobj.name) # John

# Example 9 overriding method
# class Bank:
#     def rateOfInterest(self):
#         return 0
#
# class XBank(Bank):
#     def rateOfInterest(self):
#         return 10
#
# class YBank(Bank):
#     def rateOfInterest(self):
#         return 12
#
# objx=XBank()
# print(objx.rateOfInterest()) # 10
# objy=YBank()
# print(objy.rateOfInterest()) # 12

# overloading --
# polymorphism we can implement using overloading concept

# Example 10 overloading (polymorphism)
# class Human:
#     def sayhello(self,name=None):
#         if name is not None:
#             print("Hello "+name)
#         else:
#             print("Hello")
#
# h=Human()
# h.sayhello() # Hello
# h.sayhello("Scoot")  # Hello Scoot

# Example 11
class Calculation:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)

calobj=Calculation()
calobj.add() # 0
calobj.add(10,20) # 30
calobj.add(10,20,30) # 60















