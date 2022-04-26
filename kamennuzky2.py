import random
from urllib.parse import parse_qs
print("Vitej ve hre kamen, nuzky, papir.")
hrac=0
pc=0
remiza=0
l=['k','n','p']
while True:
    r = input("Vyber/K/N/P nebo Q pro konec: ").lower()
    if r == 'k' or r == 'n' or r == 'p': 
        
        p=random.choice(l)
        print('Pocitac vybral',p.upper())
        if r == 'k'and p == 'n':
            hrac += 1
            print('Vyhravas!')
        elif r == 'n' and p == 'p':
            hrac += 1
            print('Vyhravas!')
        elif r == 'p' and p == 'k':
            hrac += 1
            print('Vyharavas!')
        elif r == p:
            remiza += 1
            print('Remiza.')
        else:
            pc += 1
            print('Prohral jsi.')
           
    elif r.lower() == 'q':
        print('Priste nashle.')
        print('***Vysledky***')
        print('Hrac:',hrac)
        print('PC:',pc)
        print('Remiza:',remiza)
        print('**************')
        quit()
    else:
        print("Pouze 'K' 'N' 'P'!")
        continue