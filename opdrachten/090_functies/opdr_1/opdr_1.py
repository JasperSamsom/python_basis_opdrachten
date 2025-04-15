# Opdracht 1 functies
# Naam student: Jasper Samsom
# Groep: IT2A


def write_to_file(bestandsnaam, tekst, modus='a'):
    """
    Schrijft tekst naar een bestand, voegt toe als het bestand al bestaat

    Args:
        bestandsnaam (str): Naam van het bestand
        tekst (str): Tekst die weggeschreven moet worden
        modus (str): Schrijfmode ('a' voor append, 'w' voor overwrite)
    """
    with open(bestandsnaam, mode=modus, encoding='utf-8') as bestand:
        bestand.write(tekst)