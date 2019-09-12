x = input("Wat is de sequentie? ")
print("Totaal",str((len(x)))+" Nucleotiden")

totaal = len(x)
totaal_G = x.count("G")
totaal_C = x.count("C")
totaal_GC = totaal_C+totaal_G

GC =(totaal_G+totaal_C)/totaal*100

print("Totaal GC basen is", totaal_GC)
print("Het GC% is "+str(GC)+"%")

