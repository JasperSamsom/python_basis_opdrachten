# Opdracht 3 Tekst opslaan
# Naam student: Jasper Samsom
# Groep: IT2A

def caesar_encrypt(tekst, verschuiving=5):
    resultaat = ""
    for karakter in tekst:
        if karakter.isalpha():

            basis = ord('A') if karakter.isupper() else ord('a')

            verschoven = (ord(karakter) - basis + verschuiving) % 26
            resultaat += chr(basis + verschoven)
        else:

            resultaat += karakter
    return resultaat


tekst = input("Geef de tekst die je wilt encrypten..\n")


versleuteld = caesar_encrypt(tekst)
print(versleuteld)
