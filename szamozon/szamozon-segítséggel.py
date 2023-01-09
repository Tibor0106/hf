import random
rand = 0
win = False
gep_szami = []
jatekos_szamai = []
eredmenyek = []
i = 0
print("[--------------] Számözön [--------------]\n")
print("- Fekete: A Megadott szám megfelelő helyen van.\n- Fehér: Ez a szám megtalálható a számok között,de nem jó",
     " helyen van.\n- Nincs ilyen szám: Nincs a megadott szám a számok között.\n")
print("[--------------] -------- [--------------]\n")
text = ""

""" Gép számainak létrehozása (Nem lehet kettő db egyenlő szám)"""

while i !=5:
    rand = random.randint(1, 9)
    """Megnézzük, hogy az adott véletlne szám benne van-e már."""
    if rand not in gep_szami:
        i+=1
        gep_szami.append(rand) 
print("Gép számai",gep_szami)
"""Addig fut, míg a játékos nem nyer"""
while win != True:
    for i in range(5):
        szam = int(input("Kérek egy számot (1-9) » "))
        jatekos_szamai.append(szam)

    """Megvizsgáljuk, hogy a megadott számok megfelelőek-e, ha minden oké, a játékos nyer"""
    if(gep_szami == jatekos_szamai):
        win = True
        print("Nyertél!")
        break 
    
    for b in range(5):
        """Megnézzük, hogy az adott lista tartalmazza-e az adott számot (Ilyenkor lesz 'Fehér'). Eseteg, hogy a szám megfelelő helyen van-e (Ugye ilyenkor lesz 'Fekete')"""
        if gep_szami[b] == jatekos_szamai[b]:
            eredmenyek.append("Fekete")
        elif jatekos_szamai[b] in gep_szami:
            eredmenyek.append("Fehér")
        else:
            eredmenyek.append("Nincs ilyen szám")
    
    """Eredemányek kiírása, listák nullázása :Erre azért van szükség, hogy a következő körben ne legyenek listában az azelőtt megadott számok) """
    for i in eredmenyek:
        text += " "+i+","
    jatekos_szamai.clear()
    eredmenyek.clear() 
    print("\n"+text+"\n")
    text = ""
    print("Sajnos ez nem nyert, próbáld újra!")
print("Program vége!")

                
            
    






