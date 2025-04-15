# Opdracht 1 while-loops
# Naam student: Jasper Samsom
# Groep: IT2A

# Lijst met enquêtevragen
vragen = [
    "Wat vind je van de huidige regering?",
    "Wat vind je van de Python-lessen tot nu toe?",
    "Wat vind jij de mooiste stad van Nederland?"
]

# Open een bestand om de antwoorden op te slaan
with open("enquete_resultaten.txt", "w") as bestand:
    bestand.write("=== Enquêteresultaten ===\n\n")

    # Stel elke vraag en sla het antwoord op
    for vraag in vragen:
        antwoord = input(vraag + "\n> ")
        bestand.write(f"Vraag: {vraag}\nAntwoord: {antwoord}\n\n")

print("\nBedankt voor het invullen van de enquête! De resultaten zijn opgeslagen in 'enquete_resultaten.txt'")