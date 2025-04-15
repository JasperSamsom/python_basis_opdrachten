# Opdracht 1 functies
# Naam student: Jasper Samsom
# Groep: IT2A

def kilometers_naar_miles(km):
    """Converteer kilometers naar miles"""
    return km / 1.609344

def miles_naar_kilometers(miles):
    """Converteer miles naar kilometers"""
    return miles * 1.609344

#Voorbeeld
kilometers = 1223
miles = 867

converted_miles = kilometers_naar_miles(kilometers)
converted_km = miles_naar_kilometers(miles)

print(f"{kilometers} kilometers = {converted_miles} miles")
print(f"{miles} miles = {converted_km} kilometers")