# Opdracht 1 functies
# Naam student: Jasper Samsom
# Groep: IT2A

import math

def kubus_vol(zijde):
    """Bereken het volume van een kubus"""
    volume = zijde ** 3
    print(f"De inhoud van deze kubus is: {volume}")
    return volume

def bol_vol(straal):
    """Bereken het volume van een bol"""
    volume = (4/3) * math.pi * (straal ** 3)
    print(f"De inhoud van deze bol is: {volume}")
    return volume

# Voorbeelden zoals gevraagd
volume_kubus = kubus_vol(5)  # Output: De inhoud van deze kubus is: 125
volume_bol = bol_vol(4)      # Output: De inhoud van deze bol is: 268.082573106329