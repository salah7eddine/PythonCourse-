# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
  # Constructor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
  
  def greeting(self):
    return f'My name is {self.name} and I am {self.age}'
  
  def has_birdthay(self):
    self.age += 1
  

# Extend class
class Customer(User):
   # Constructor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
    self.balance = 0
  
  def set_balance(self, balance):
    self.balance = balance
    
  def greeting(self):
    return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

# Init user object
mizo = User('Hamza Abousaid','mizo@gmail.com', 25)

mizo.has_birdthay()  
print(mizo.greeting())

# Init customer object
meryem = Customer('Meryem Abousaid', 'mery@gmail.com', 19)

meryem.set_balance(5000)

print(meryem.greeting())

