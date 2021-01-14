print('Lista zakupów')
print()
slownik = {'piekarnia': ['chleb', 'pączek', 'bułki'], 'warzywniak': ['marchew', 'seler', 'rukola']}

suma=0
for klucz in slownik:
    suma+=len(slownik[klucz])
    #print('suma: {}'.format(suma))
    print('Idę do {}, kupuję tu następujące rzeczy: {}'.format(klucz.capitalize(), [x.capitalize() for x in slownik[klucz]] ))
   
    #print(idę do klucz i kupuję tam)

