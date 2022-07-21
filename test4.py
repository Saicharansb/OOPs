class Person:
    def __init__(self, name, surname, emailid, year_of_birth):
        self.name1 = name
        self.surname = surname
        self.emailid = emailid
        self.year_of_birth = year_of_birth

    def __init__(self, name, surname):
        self.name1 = name
        self.surname = surname


    def age(sudh, current_year):
        return current_year

anuj_var = Person("anuj", "Bhandari")
sai_var = Person("saicharan","bhavanipetwar")
gargi = Person("gargi","xyz")
print(anuj_var.age(2022))
