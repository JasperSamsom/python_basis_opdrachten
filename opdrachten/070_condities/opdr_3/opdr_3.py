# Opdracht 3 condities
# Naam student: Jasper Samsom
# Groep: IT2A

normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

print("Geef uw leeftijd in aantal jaar")
leeftijd_input = int(input())

for groep, (min_leeftijd, max_leeftijd) in leeftijd.items():
    if min_leeftijd <= leeftijd_input <= max_leeftijd:
        korting = kortings_percentages[groep]
        toegangsprijs = normale_toegangsprijs * (100 - korting) / 100
        print(f"U behoort tot de groep {groep}")
        print(f"U krijgt {korting}% korting")
        print(f"U betaalt daarom {toegangsprijs:.2f}")
        break
