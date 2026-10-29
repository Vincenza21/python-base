def fattoriale(num):
    fatt = 1
    for i in range(1, num+1):
        fatt *= i
    return fatt

num = int(input("Inserisci un numero intero positivo: "))
fatt = fattoriale(num)
print(f"Il fattoriale di {num} è {fatt}")