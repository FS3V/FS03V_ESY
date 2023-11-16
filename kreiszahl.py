# pi-berechn2.py

from math import sqrt, pi

n = 6  
s = 1  

print ("Schrittweise Naeherung von pi mit Hilfe eines 2n-Ecks")

for i in range(1,21):

    pi_naeherung = 0.5*n*s
    print (round(pi_naeherung,11))
    s = s/sqrt(2+sqrt(4-s*s))
    n = 2*n  # doppelte Eckenzahl

print ("Gute Iteration!")

print ("pi =",round(pi,11))
