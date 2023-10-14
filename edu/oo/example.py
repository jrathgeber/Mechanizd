class employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.email = self.firstname + "." + self.lastname + "@kite"

    def giveRaise(self, salary):

        self.salary = salary


class developer(employee):

    def __init__(self, firstname, lastname, salary ,programming_lang):
        super().__init__(firstname,lastname,salary)
        self.prog_langs = programming_lang

    def addLanguage(self, lang):
        self.prog_langs = lang


employee1 = employee("Jon", "Smith", 100000)

print (employee1.salary)

dev1 = developer ("Jon", "Smith", 100000, ["python", "C"])

dev1.giveRaise(120000)

print(f"The salary of {dev1.firstname} is {dev1.salary}")


