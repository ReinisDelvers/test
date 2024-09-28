class Person:
    
    def __init__(self, name, sex, age = 0):
        self.name = name
        self.sex = sex
        self.age = age

    def info(self):
        return f"Sveiki mani sauc {self.name}. Man ir {self.age} gadi. Es esmu {self.sex}"
    
    def sexchange(self):
        if self.sex == "Vīrietis":
            self.sex = "Sieviete"
        elif self.sex == "Sieviete":
            self.sex = "Vīrietis"
        # persona.info()

    def birthday(self):
        self.age += 1
        # persona.info()

    
    def namechange(self, newname):
        self.name = newname
        # persona.info()

class Women(Person):
    
    def __init__(self, name, haircolor, age = 0):
        super().__init__(name,"S", age)
        self.haircolor = haircolor
        # self.info()
        
    # def tellmeaboutmyself(self):
    #     super().info()
    #     print(f"Mana matu krāsa ir {self.haircolor}")

class Men(Person):
    
    def __init__(self, name, hobby, age = 0):
        super().__init__(name,"S", age)
        self.hobby = hobby
        # self.info()
        
    # def tellmeaboutmyself(self):
    #     super().info()
    #     print(f"Mans hobijs ir {self.hobby}")


persona = Person("Aleksis", "V", 18)
# persona.info()
# persona.birthday()
# persona.sexchange()
# persona.namechange("Alex")

# persona = Women("Anna", "blonda", 23)
# persona = Men("Pēteris", "sērfošana", 35)
