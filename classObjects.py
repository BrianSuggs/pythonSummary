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
  def myfunc2(abc):
    print("Hello my name is " + abc.name)

# p1 is an object of class Person
p1 = Person("Terry", 38)
p1.myfunc2()

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

#######################################################################################################################


# INHERITANCE
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class

# Create a Parent Class
# Any class can be a parent class, so the syntax is the same as creating any other class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

# Create a Child Class
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class
# Create a class named Student, which will inherit the properties and methods from the Person class
class Student(Person):
  pass

# Use the Student class to create an object, and then execute the printname method
x = Student("Mike", "Olsen")
x.printname()

# we have created a child class that inherits the properties and methods from its parent
# We want to add the __init__() function to the child class
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function
# The child's __init__() function overrides the inheritance of the parent's __init__() function
class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.
    
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
    
# Now we have successfully added the __init__() function, and kept the inheritance of the parent class, 
# and we are ready to add functionality in the __init__() function

# The super() functinon
# function will make the child class inherit all the methods and properties from its parent
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    
# By using the super() function, you do not have to use the name of the parent element, 
# it will automatically inherit the methods and properties from its parent

# Adding Properties
# Add a property called graduationyear to the Student class
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
    
# the year 2019 should be a variable, and passed into the Student class when creating student objects
# To do so, add another parameter in the __init__() function
# Add a year parameter, and pass the correct year when creating objects
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)


# Add Methods
# Add a method called welcome to the Student class
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
    
# If you add a method in the child class with the same name as a function in the parent class, 
# the inheritance of the parent method will be overridden

