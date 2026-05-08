from algemene_functies import mijn_functie_2

# functie aanbieding_1 heeft drie parameters,: smaak, prijs en korting.  
def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs * (1 - korting)

    print(
        f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, "
        f"van {prijs} euro voor {nieuwe_prijs} euro."
    )
    
aanbieding_1("aardbei", 4, 0.1)

# functie inkomsten_totaal() bevat één parameter inkomsten, met argument een lijst met 7 waarden. 
# Teruggeefwaarde bevat totaal van de 7 waarden. 
# functie inkomsten_totaal() bevat extra argument btw. Dit is een float. 
# Teruggeefwaarde moet een string zijn.
inkomsten = [220, 430, 125, 160, 205, 90, 345]
btw = 0.09

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_totaal = totaal * btw
       
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_totaal} euro btw betaald dient te worden."

print(inkomsten_totaal(inkomsten,btw))

# functie laag_en_hoog() bevat één parameter mijn_lijst. 
# Argumenten zijn de 7 waarden inkomsten. 
# Teruggeefwaarde moet een lijst zijn met slechts twee elementen, hoogste en de laagste waarde.
def laag_en_hoog(mijn_lijst):
    return [min(mijn_lijst), max(mijn_lijst)]

# functie gemiddelde bevat één parameter mijn_lijst. 
# Argumenten zijn de 7 waarden inkomsten. 
# Teruggeefwaarde is een string
def gemiddelde(mijn_lijst):
    weekelijks_gem = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {weekelijks_gem} euro"

# functie meervoudig() bevat één parameter invoer_lijst
# Argument wordt een lijst van tussen de vijf en tien integers meegegeven
# Teruggeefwaarde hoogste en laagste waarde in de lijst
# Gebruik functie laag_en_hoog()
invoer_lijst = [10, 5, 3, 2, 1, 2, 9]

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

print(meervoudig(invoer_lijst))

# functie combinatie() bevat één parameter invoer_lijst_2
# roep functie laag_en_hoog() aan met als argument invoer_lijst_2
# Teruggeefwaarde wordt opgeslagen in korte_lijst
# Deze lijst dient als argument gebruikt te worden bij het aanroepen van mijn_functie_2
# Teruggeefwaarde die hierdoor gegenereerd wordt is de teruggeefwaarde van functie combinatie()
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    resultaat = mijn_functie_2(korte_lijst)
    return resultaat


