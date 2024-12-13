# x = lambda a: a + 10
# print(x(5))

# x ='hello world'
# print(x

# class MyClass:
#   x = 5
# print(MyClass)

# class myclass:
#   x=5
# print(myclass)
# class myclass:
#     x=3
    # print(myclass)
    
# class Person:
#  def __init__(self, name, age):
#     self.name = name
#     self.age = age
# p1 = Person("John", 36)
# print(p1.name)
# print(p1.age)


# class person:
#  def __init__(self, name, age):
#     self.name=name
#     self.age=age
    
# p1 = person("abu", 36)
# p1 = person("sayed", 36)

# print(p1.name)
# print(p1.age)     

# # ____________________________students nam & roll number list_____
# class student:
#     def __init__(self, name, roll):
#         self.name = name
#         self.roll = roll
#     def details(self):
#         print('name is: ', self.name)
#         print('roll is: ', self.roll)
# s1 = student('md abu sayed',35)
# s2 = student('md lablu',25)

# s1.details()
# s2.details()
# # ____________________________students nam & roll number list_____       

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{'my name is: ' + self.name} {self.age}"    

# p1 = Person("John", 36)

# print(p1)


# __________________________________str method

# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil", "Refsnes")


# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")

# def my_function(x):
#   return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))

# def my_function(x):
#   return 4*x
# print(my_function(6))
# print(my_function(4))
# print(my_function(7))
# ________________________________________________increment for pyuthon_______
# A sample use of increasing the variable value by one. 
# count = 0
# count += 1
# count = count+1
# print('The Value of Count is', count) 

# print("INCREMENTED FOR LOOP") 
# for i in range(0, 5): 
# 	print(i) 

# # this is for increment operator here start = 5, 
# # stop = -1 and step = -1 
# print("\n DECREMENTED FOR LOOP") 
# for i in range(4, -1, -1): 
# 	print(i) 
# ________________________________________________increment for pyuthon_______

# ____________________________________________________

# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil", "Refsnes")

# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")

# def myfunction(fname, lname):
#   print(fname - lname)
# myfunction(5 , 2)

# def my_function(*abu):
#     print('your recent brother is: ' + abu[2])
# my_function('abu' , 'sayed', 'lablu')

# def my_function(fname):
#   print(fname + " abu")
#   print(fname + " sayed")
#   print(fname + " lablu")

# my_function("md")
# my_function("Tobias")
# my_function("Linus")

# def my_function(x,y):
#   print(x*y)

# my_function(3,3)
# def myfunction(x,y):
#     print(x*y)
# myfunction(5,6)
# def my_function(**kids):
#     print('my name is: ' + kids['lname'])
# my_function(fname='abu',lname='sayed')

# x = lambda a: a + 10
# print(x(5))

# x = lambda a, b: a % b
# print(x(5, 10))

# x=lambda a, b: a + b
# print(x(5, 7))

# x = lambda a, b, c: a + b + c
# print(x(5, 6, 2))
# x=lambda a,b,c,d: a + b - c % d
# print(x(10,2,3,10))





# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))

x=('hello world')
print(x)