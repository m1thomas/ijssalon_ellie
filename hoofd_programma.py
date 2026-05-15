from helper import onderstreep

# Nieuwe lijst uitvoer welke onderstreep functie gebruikt
uitvoer = onderstreep("AANBIEDING") 
uitvoer.append("Aardbeienijs, emmertje van 5 liter: 5 euro")
uitvoer.append("Slagroom, spuitbus van 1 liter: 2 euro")

print()

# for-loop om door de waarden van uitvoer te loopen en de elementen van uitvoer één voor één te printen
for el in uitvoer:
    print(el)
