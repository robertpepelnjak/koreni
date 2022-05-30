
število = int(input("Koren katerega števila hočeš izračunati?\n"))
metoda = str(input("S katero metodo hočeš?\nČe hočeš z bisekcijo napiši B, če hočeš s tangentno metodo napiši T \n"))
if metoda.upper() == "T":
  x = int(input("Zapiši začetno število:\n"))
  rešitve = [x]
  while True:
    xn = x
    xn = (x ** 2 + število)/(2*x)
    rešitve.append(xn)
    if round(xn, 10) == round(x, 10):
      break
    else:
      x = xn
      xn = (x ** 2 + število)/(2*x)
      rešitve.append(xn)
  for i in rešitve:
    print(i)
