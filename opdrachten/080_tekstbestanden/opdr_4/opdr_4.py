# Opdracht 4 Tekst opslaan
# Naam student: Jasper Samsom
# Groep: IT2A

# Lijst met vragen voor de feestgangers
vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]


with open("feestgangers.txt", "a") as bestand:

    antwoorden = {}
    for i, vraag in enumerate(vragen, 1):
        antwoord = input(f"{i}. {vraag}\n")
        sleutel = ["voornaam", "achternaam", "drank", "eten"][i - 1]
        antwoorden[sleutel] = antwoord


    bestand.write("\n".join([f"{key}: {value}" for key, value in antwoorden.items()]) + "\n\n")


    print("\nBedankt voor het invullen!")
    print("See you at the party.")