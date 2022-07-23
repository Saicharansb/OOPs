class person :

    _name = "sam"
    __surname = "kumar"
    yob = 1990

obj = person()
print(obj)
# inheritance- use of parental functions.
class employee(person):
    pass

obj1 = employee()
print(obj1)
print(obj1.yob)
print(obj1._name) #system will not give any options as it is private
print(obj1._person__surname) # system will not give optionas as it is protected.


