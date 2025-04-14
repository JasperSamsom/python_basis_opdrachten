# Opdracht 3 input functie
# Naam student: Jasper Samsom
# Groep: IT2A

input_lijst = input("'Amsterdam', 'Zwolle', 'Dronten', 'Haarlem', 'Zaanstad'")

# Split de invoer in een lijst en verwijder eventuele spaties
objecten = [obj.strip() for obj in input_lijst.split(',')]

# Controleer of er minimaal 5 objecten zijn ingevoerd
if len(objecten) < 5:
    print("Je moet minimaal 5 objecten invoeren!")
else:
    gesorteerd = sorted(objecten, key=lambda x: (not x.lower().startswith('z'), x), reverse=True)

    # Print de gesorteerde lijst
    print(gesorteerd)

