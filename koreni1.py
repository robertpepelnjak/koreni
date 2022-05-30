rešitve = []
število = int(input("Koren katerega števila hočeš izračunati?\n"))
metoda = str(input("S katero metodo hočeš?\nČe hočeš z bisekcijo napiši B, če hočeš s tangentno metodo napiši T \n"))
if metoda.upper() == "T":
  x = int(input("Zapiši začetno število:\n"))
  rešitve.append(x)
  while True:
    xn = (x ** 2 + število)/(2*x)
    rešitve.append(xn)
    if round(xn, 10) == round(x, 10):
      break
    else:
      x = xn
elif metoda.upper() == "B":
  a = 0
  b = število
  while True:
    if round(a, 10) == round(b, 10):
      break
    else:
      sredina = (a+b)/2
      rešitve.append(sredina)
      if sredina ** 2 > število:
        b = sredina
      else:
        a = sredina
else:
  print("Je res tako težko slediti navodilom?")
for i in rešitve:
    print(i)
