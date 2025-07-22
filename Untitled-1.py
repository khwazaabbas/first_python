class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = person("khwaza", "abbas")
x.printname()

class student(person):
    def __init__(self, fname, lname, year):
        # person.__init__(self, fname, lname)
        super().__init__(fname, lname)
        self.birthyear = year 
        self.mobilenumber = 9758897536

    def method(self):
        print("my name is ", self.firstname, self.lastname, "and birth date is", self.birthyear, "and the mobile number is ", self.mobilenumber )

y = student("mani", "ansari", 1995)
y.printname()
print(y.birthyear)
print(y.mobilenumber)
y.method()