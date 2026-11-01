class myclass: #Creates a class that I  called myclass.
    def __init__(self, name, age): #Gives properties to the class that are called name and age.
        self.name = name
        self.age = age
    def __str__(self): #When printing the class, it prints it formatted nicely.
        return f"{self.name} {self.age}"
    def myfunc(self): #Creates a function that can be called in a special way, as shown on line 14.
        print("Hello ", self.name, ".", sep = "") #Prints Hello, Jack when called with p1.

p1 = myclass("Jack", 50) #Creates a person that has a name and an age.
print(p1.name) #Prints the name, or Jack.
print(p1.age) #Prints the age, or 50.
print(p1) #Prints the whole thing the way the __str__ function programmed it to.
p1.myfunc() #Calls the myfunc function that is up on line 7.