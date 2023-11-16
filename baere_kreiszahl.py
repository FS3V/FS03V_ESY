# pi-berechn2.py

# pi-Berechnung mit regulären 2n-Ecken

from math import sqrt, pi

n = 6  # Start mit regulärem Sechseck

s = 1  # Seitenlänge des reg. Sechsecks

print ("Schrittweise Näherung von pi mit Hilfe eines 2n-Ecks")

for i in range(1,21):

    pi_naeherung = 0.5*n*s

    print (round(pi_naeherung,11))

    s = s/sqrt(2+sqrt(4-s*s))

    n = 2*n  # doppelte Eckenzahl

print ("Gute Iteration!")

print ("pi =",round(pi,11))
