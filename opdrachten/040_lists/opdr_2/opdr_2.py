# Opdracht 2 lists
# Naam student:
# Groep:

rivier_info = {
    "rijn": ["nederland", "duitsland", "frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())

print("De rivier", rivieren[0].capitalize(), "stroomt onder andere door", rivier_info[rivieren[0]][1].capitalize())
