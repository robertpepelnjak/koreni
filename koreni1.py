število = int(input("Koren katerega števila hočeš izračunati?\n"))
metoda = str(input("S katero metodo hočeš?\nČe hočeš z bisekcijo napiši B, če hočeš s tangentno metodo napiši T \n"))
if metoda.upper() == "T":
  x = int(input("Zapiši začetno število:\n"))
  rešitve = [x]
  for number in range(2):
    xn = (x ** 2 + število)/(2*x)
    x = xn
    rešitve.append(xn)
    n = int(0)
  while rešitve[n] != rešitve[n-2]:
    x=xn
    xn = (x ** 2 + število)/(2*x)
    rešitve.append(xn)
    n+=1
  for število in rešitve:
    print(število)
