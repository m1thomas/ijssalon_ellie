# Functie presenteer(), heeft een dictionary, parameter totaal

def presenteer(inkomsten, totaal):
    for item in inkomsten:
        print(item, ":" , inkomsten[item])
    print("==========================")
    print("totaal", ":" , totaal)
    return totaal

