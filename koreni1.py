rešitve = []
število = int(input("Koren katerega števila hočeš izračunati?\n"))
metoda = str(input("S katero metodo hočeš?\nČe hočeš z bisekcijo napiši B, če hočeš s tangentno metodo napiši T \n"))
if metoda.upper() == "T":#TANGENTNA METODA
  x = int(input("Zapiši začetno število:\n"))
  rešitve.append(x)
  while True:
    xn = (x ** 2 + število)/(2*x)#izračuna prvo vrednost s formulo newtonove metode
    rešitve.append(xn)#doda vrednost na seznam rešitve
    if round(xn, 10) == round(x, 10):#zaključi zanko, če sta prejšnja rešitev in nova rešitev približno enaki
      break
    else:
      x = xn#nastavi rešitev na novo rešitev

elif metoda.upper() == "B":#BISEKCIJA
  a = 0#definira spremenljivko a in b (meje intervala)
  b = število
  while True:
    if round(a, 10) == round(b, 10):#če sta se meji intervala dovolj blizu, ustavi zanko
      break
    else:
      sredina = (a+b)/2#definira sredino intervala
      rešitve.append(sredina)#doda sredino na seznam rešitev
      if sredina ** 2 > število:#če je kvadrat sredine intervala večji od desne meje intervala, vzame za meje novega intervala levo mejo in sredino
        b = sredina
      else:#če je kvadrat sredine intervala manjši od desne meje intervala, vzame za meje novega intervala desno mejo in sredino
        a = sredina

else:
  print("Je res tako težko slediti navodilom?")#v primeru da uporabnik ne zna slediti navodilom, ga program okara

if rešitve:#če rešitve niso prazna množica, jih izpiše
  for i in rešitve:
      print(i)
