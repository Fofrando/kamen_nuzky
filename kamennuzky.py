import random
print("Vitej ve hre kamen, nuzky, papir.")
hrac=0
pc=0
remiza=0
l=['k','n','p']
while True:
    r = input("Vyber/k/n/p nebo q pro konec: ")
    if r.lower() == 'k' or r.lower() == 'n' or r.lower() == 'p': 
        
        p=random.choice(l)
        if r == 'k':
            if p =='n':
                print('PC vybral:',p)
                print('Vyhravas! Kamen tupi nuzky.')
                hrac+=1
                continue
            elif p == 'k':
                print('PC vybral:',p)
                print('Remiza. Kamen = Kamen.')
                remiza+=1
                continue
            else:
                print('PC vybral:',p)
                print('Prohravas! Papir bali kamen.')
                pc+=1
                continue
        elif r == 'n':
            if p =='p':
                print('PC vybral:',p)
                print('Vyhravas! Nuzky strihaji papir.')
                hrac+=1
                continue
            elif p == 'n':
                print('PC vybral:',p)
                print('Remiza. Nuzky = Nuzky.')
                remiza+=1
                continue
            else:
                print('PC vybral:',p)
                print('Prohravas! Kamen tupi nuzky.')
                pc+=1
                continue
        elif r.lower() == 'p':
            if p =='k':
                print('PC vybral:',p)
                print('Vyhravas! Kamen bali papir.')
                hrac+=1
                continue
            elif p == 'p':
                print('PC vybral:',p)
                print('Remiza. Papir = Papir.')
                remiza+=1
                continue
            else:
                print('PC vybral:',p)
                print('Prohravas! Nuzky strhaji papir.')
                pc+=1
                continue
    elif r.lower() == 'q':
        print('Priste nashle.')
        print('---Skore hry---')
        print('Hrac:',hrac)
        print('PC:',pc)
        print('Remiza:',remiza)
        quit()
    else:
        print("Pouze 'k' 'n' 'p'!")
        continue