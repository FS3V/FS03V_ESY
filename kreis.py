# pi-monte_carlo.py

# pi-Bestimmung mit der Methode von Monte Carlo

from random import random

print ("Monte Carlo Methode zur")

print ("Näherung für pi:")

g = int(input("Gesamtzahl der Tropfen: "))

v = 0

x=0; y=0  # Koordinaten des Punktes P

for i in range(1,g+1): 

      x = random()

      y = random()

      if x*x+y*y<= 1:  

         v = v + 1 

pi_naeh = 4.0*v/g

print (g,"Tropfen, davon",v,"Tropfen im Viertelkreis,")

print ("pi etwa",pi_naeh)