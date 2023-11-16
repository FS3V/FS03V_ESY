# wurzel_n.py

a = float(input("Zu berechnende n.Wurzel: "))

n = float(input("Eingabe von n: "))

x = float(input("Schätzwert: "))  

print ("Iteration  Näherungswert")

print ("______________________________")   

for i in range(1,6):

  x = ((n-1)*x+a/(x**(n-1)))/n

  #  Bemerkung: x**(n-1) bedeutet x hoch n-1

  print ('   ',i,'    ',x)