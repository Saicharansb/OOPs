class person:

    def age(self, current_year , year_of_birth):
        return current_year-year_of_birth

    def email_id_input(self,email_id):
        print("take and mail id from person and print it ", email_id)

    def ask_name(self):
        name = input("tell me your name : ")
        return name

    def ask_dob(self):
        dob = input("tell me your date of birth :")
        return dob

sudh = person()
anuj = person()
gargi = person()
sai = person()

# sudh.email_id_input("sudh@ineuron.ai")
# print(sai.ask_name())

print(gargi.ask_dob())