def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag, personen):
    bedrag_pp = bedrag / personen 
    return f"Het bedrag per persoon is {bedrag_pp} euro"

# Naam functie onderstreep(), parameter tekst met standaardwaarde ""
# Variabele is uit, dit is een lege list (uit =[])
# Gebruik .append() om de waarde van de parameter tekst als element toe te voegen aan list uit
# Voeg tweede element toe aan list uit, dit is een string met een aantal =-tekens. 
# Het aantal =-tekens moet gelijk zijn aan het aantal karakters in de parameter tekst.
# De functie geeft de waarde van de variabele uit als uitvoer

def onderstreep(tekst=""):
    uit = []
    uit.append(tekst)
    uit.append("=" * len(tekst))
    return uit
