# CLASSES & OBJECTS
# A Class is like an object constructor, or a "blueprint" for creating objects
# To create a class, use the keyword class
# Create a class named MyClass, with a property named x
class MyClass:
  x = 5

# Create Objects
# Now we can use the class named MyClass to create objects
# Create an object named p1, and print the value of x
p1 = MyClass()
print(p1.x)

class CarClass:
  make = "Toyota"
  mpg = 40

# Create Objects
car_1 = CarClass()

print(car_1.make)
print(car_1.mpg)

# The __int__() function
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Brian", 24)
p2 = Person("Kevin", 20)

print(p1.name)
print(p1.age)

print(p2.name)
print(p2.age)


# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name +
          " and I am ", self.age, " years old")

p1 = Person("John", 36)
p1.myfunc()


# The Self Parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age
  
  # abc is a placeholder for mysillyobject which is an instance of the class
  def myfunc(abc):
    print("Hello my name is " + abc.name)

# p1 is an object of class Person
p1 = Person("John", 36)
p1.myfunc()

# Modify Object Properties
p1.age = 40

# Delete Object Properties
# You can delete properties on objects by using the del keyword
# Delete the age property from the p1 object
del p1.age

# Delete Objects
# Delete the p1 object
del p1

# The Pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content, 
# put in the pass statement to avoid getting an error
class Person:
  pass

