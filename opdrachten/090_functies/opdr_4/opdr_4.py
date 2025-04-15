# Opdracht 1 functies
# Naam student: Jasper Samsom
# Groep: IT2A


def volledige_naam(lijst_met_namen):
    volledige_namen = []
    for naam_dict in lijst_met_namen:
        try:
            vn = naam_dict["voornaam"].strip()
            tv = naam_dict["tussenvoegsel"].strip()
            an = naam_dict["achternaam"].strip()

            if tv:
                volledige_namen.append(f"{vn} {tv} {an}")
            else:
                volledige_namen.append(f"{vn} {an}")
        except KeyError as e:
            print(f"Ontbrekend veld in naam: {e}")
    return volledige_namen