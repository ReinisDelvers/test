class Person:
    
    def __init__(self, name, sex, age = 0):
        self.name = name
        self.sex = sex
        self.age = age

    def tellmeaboutmyself(self):
        if self.sex == "V":
            sexname = "Virietis"
        elif self.sex == "S":
            sexname = "Sieviete"
        else:
            sexname = self.sex

        print(f"Sveiki mani sauc {self.name}. Man ir {self.age} gadi. Es esmu {sexname}")
    
    def sexchange(self):
        if self.sex == "V":
            self.sex = "S"
        elif self.sex == "S":
            self.sex = "V"
        persona.tellmeaboutmyself()


    def birthday(self):
        self.age += 1
        persona.tellmeaboutmyself()

    
    def namechange(self, newname):
        self.name = newname
        persona.tellmeaboutmyself()

class Women(Person):
    
    def __init__(self, name, haircolor, age = 0):
        super().__init__(name,"S", age)
        self.haircolor = haircolor
        self.tellmeaboutmyself()
        
    def tellmeaboutmyself(self):
        super().tellmeaboutmyself()
        print(f"Mana matu krāsa ir {self.haircolor}")

class Men(Person):
    
    def __init__(self, name, hobby, age = 0):
        super().__init__(name,"S", age)
        self.hobby = hobby
        self.tellmeaboutmyself()
        
    def tellmeaboutmyself(self):
        super().tellmeaboutmyself()
        print(f"Mans hobijs ir {self.hobby}")


persona = Person("Aleksis", "V", 18)
persona.tellmeaboutmyself()
persona.birthday()
persona.sexchange()
persona.namechange("Alex")

persona = Women("Anna", "blonda", 23)
persona = Men("Pēteris", "sērfošana", 35)
