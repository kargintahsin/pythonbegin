sozluk = {"taso": "messi", "Ronaldo": "SUUUUUUUIIIIIII"}
print(sozluk["taso"])  # for only one item

for i, j in sozluk.items():  # for more than one item
    print(i + "=" + j)

# EXAMPLES

programmingLanguage = {"Tahsin": ["Python", "C", "C#"], "Bayram": ["C#", "C", "Dart"], "Ramazan": ["Python", "C#"]}
isim = input("İsim giriniz: ")
print("Programming languages {}'s know: ".format(isim))

for i in programmingLanguage[isim]:
    print(i)
