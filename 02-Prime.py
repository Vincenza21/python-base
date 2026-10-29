def numeroPrimo(num):
    primo = True
    if num<2:
        primo = False
    for i in range (2, num):
        if num%i==0:
            primo = False
    return primo

num = int(input("Inserire il numero: "))
primo = numeroPrimo(num)
if primo:
    print(f"Il numero {num} è primo")
else:
    print(f"Il numero {num} non è primo")