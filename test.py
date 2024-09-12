class Cilveks:
    def __init__(self, vards, dzimums, vecums):
        self.vards = vards
        self.dzimums = dzimums
        self.vecums = vecums

    def dzimsanasdiena(self):
        self.vecums += 1
    
    def pastastitparsevi(self):
        if self.dzimums == "V":
            dzimumanosaukums = "Virietis"
        elif self.dzimums == "S":
            dzimumanosaukums = "Sieviete"
        else:
            dzimumanosaukums = self.dzimums

        print("Sveiki mani sauc {}. Man ir {} gadi. Es esmu {}".format(self.vards, self.vecums, dzimumanosaukums))
    
    def dzimummaina(self):
        if self.dzimums == "V":
            self.dzimums = "S"
        elif self.dzimums == "S":
            self.dzimums = "V"

    def vardamaina(self, jaunsvards):
        self.vards = jaunsvards

persona = Cilveks("Aleksis", "V", 18)
persona.pastastitparsevi()
persona.dzimsanasdiena()
persona.dzimummaina()
persona.vardamaina("Alex")
persona.pastastitparsevi()