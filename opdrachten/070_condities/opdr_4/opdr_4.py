# Opdracht 4 condities
# Naam student: Jasper Samsom
# Groep: IT2A


toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00), ("ansjovis", 2.50)]

# Maak een lijst van alleen de topping-namen voor de keuzemogelijkheid
beschikbare_toppings = [topping[0] for topping in toppings]

# Vraag de gebruiker om een keuze te maken
keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings}\n")

# Zoek de gekozen topping in de lijst en toon de prijs
for topping, prijs in toppings:
    if topping == keuze:
        print(f"U heeft {keuze} besteld. Dat kost {prijs}")
        break

else:
    print("Sorry, deze topping hebben we niet.")