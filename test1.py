class Person:
    def __init__(self, name, surname, emailid, year_of_birth):
        self.name1 = name
        self.surname = surname
        self.emailid = emailid
        self.year_of_birth = year_of_birth

anuj_var = Person("anuj", "Bhandari", "anuj@gmail.com", 1994)
sai_var = Person("saicharan","bhavanipetwar","samcool@gamil.com", 1991)
gargi = Person("gargi","xyz", "gargi@gmail.com", 1992)

print(anuj_var.name1)
print(sai_var.name1)
print(gargi.name1)
print(gargi.emailid)
print(sai_var.year_of_birth)
print(type(sai_var))