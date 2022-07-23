class person :

    _name = "sam"
    __surname = "kumar"
    yob = 1990

    def _age(self, current_year):
        return current_year -self.yob
    def __age1(self, current_year):
        return current_year -self.yob

obj = person()

print(obj._age(2022))
print(obj._person__age1(2022))
# inheritance- use of parental functions.
class employee(person):
    _name = "samcool"
    __surname = "montey"
    yob = 1900

obj1 = employee()
print(obj1._age(2022))
print(obj1._person__age1(2022))
print(obj1)
print(obj1.yob)
print(obj1._name) #system will not give any options as it is private
print(obj1._employee__surname) # system will not give option as it is protected.
