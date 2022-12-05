
class User:
    def __init__(self, uid, name, age):
        self.id = uid
        self.name = name
        self.age = age

    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def __str__(self):
        return f"ID: {self.id} | Name: {self.name}\t | Age: {self.age}"