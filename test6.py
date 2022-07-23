class person :
    def __init__(self, name , surname, yob):
        self._name1 = name  # it is protected. you can access in this class
        self.__surname1 = surname #it is private.
        self.yob1 = yob

sai = person("saicharan", "Bhavanipetwar", 1991)

print(sai.yob1) # this is public
print(sai._name1) # this is protected and need to write as it is to call.
print(sai._person__surname1)  #to extract the private we have to use class and object both by using _