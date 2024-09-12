from test import Women

peoplelist = []

for i in range(20):
    peoplelist.append(Women("Anna", "blonda", i))

for women in peoplelist:
    if women.age % 2 == 0:
        women.sexchange()

print("-------------")
for women in peoplelist:
    women.tellmeaboutmyself()