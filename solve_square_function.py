from math import sqrt   #  sqrt() ist die Quadratwurzelfunktion

print "Quadratische Gleichung mit den \nKoeffizienten a, b und c lösen."

a = float(input("a eingeben: "))        # \n bedeutet: neue Zeile

b = float(input("b eingeben: "))

c = float(input("c eingeben: "))

d = b*b-4*a*c

if d > 0:

   x1 = (-b - sqrt(d))/(2*a)

   x2 = (-b + sqrt(d))/(2*a)

   print ("Die Gleichung hat die beiden Lösungen:")

   print ('x1 =',x1,'; x2 =',x2)

elif d == 0:

   x1 = (-b)/(2*a);

   print ("Die Gleichung hat die Lösung:")

   print ('x =',x1)

else:

   print ("Die Gleichung hat keine Lösung!") 