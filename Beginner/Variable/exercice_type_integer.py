"""
En Python, les entiers sont des nombres entiers nuls, positifs ou négatifs 
sans partie fractionnaire et ayant une précision illimitée, par exemple 0, 100, -10.
 Les éléments suivants sont des littéraux entiers valides en Python.
"""




# Somme de trois nombres avec l'operateur arithmetique +

# Declaration de trois variables nbr1, nbr2 wt somme de type entier
nbr1 = 5
nbr2 = 4
somme               = nbr1+nbr2
multiplication      = nbr1*nbr2
soustraction        = nbr1-nbr2
division_floatante  = nbr1//nbr2
division_entiere    = nbr1/nbr2
modulo              = nbr1%nbr2
puissance           = nbr1^nbr2

print("La somme de deux nombres              :", nbr1, " + ", nbr2," = ", somme)
print("La multication de deux nombres        :", nbr1, " + ", nbr2," = ", multiplication)
print("La soustraction de deux nombres       :", nbr1, " + ", nbr2," = ", soustraction)
print("La division entiere de deux nombres   :", nbr1, " + ", nbr2," = ", division_floatante)
print("La division floatante de deux nombres :", nbr1, " + ", nbr2," = ", division_entiere)
print("Le modulo de deux nombres             :", nbr1, " + ", nbr2," = ", modulo)
print("La puissance de deux nombres          :", nbr1, " + ", nbr2," = ", puissance)

print()


"""
Les zéros non nuls dans les entiers non nuls ne sont pas autorisés, 

par exemple 000123 est un nombre invalide, 0000 est 0.

nbr_nbr = 01234567890

"""


# Une autre facon de faire ce de mettre _ sur le nombre

"""
Python n'autorise pas la virgule comme délimiteur de nombre. 

Utilisez _plutôt un trait de soulignement comme délimiteur.
"""

print("Une autre facon de faire ce de mettre _ sur le nombre")
print()

nbr3 = 1_234_567_890
nbr4 = 1_234_567_890
somme               = nbr3+nbr4
multiplication      = nbr3*nbr4
soustraction        = nbr3-nbr4
division_floatante  = nbr3/nbr4
division_entiere    = nbr3//nbr4
modulo              = nbr3%nbr4
puissance           = nbr3^nbr4

print("La somme de deux nombres              :", nbr1, " + ", nbr2," = ", somme)
print("La multication de deux nombres        :", nbr1, " + ", nbr2," = ", multiplication)
print("La soustraction de deux nombres       :", nbr1, " + ", nbr2," = ", soustraction)
print("La division floatante de deux nombres :", nbr1, " + ", nbr2," = ", division_entiere)
print("La division entiere de deux nombres   :", nbr1, " + ", nbr2," = ", division_floatante)
print("Le modulo de deux nombres             :", nbr1, " + ", nbr2," = ", modulo)
print("La puissance de deux nombres          :", nbr1, " + ", nbr2," = ", puissance)
print()



"""
Les entiers peuvent être des valeurs binaires, octales et hexadécimales.
"""
print("Les entiers peuvent être des valeurs binaires, octales et hexadécimales.")

"""
Binaire
Un nombre ayant 0b avec huit chiffres dans la combinaison de 0 et 1 représente les nombres binaires en Python. 
Par exemple, 0b11011000 est un nombre binaire équivalent à l'entier 216.
"""
nbr_binary   = 0b11011000 # binary

"""
Octal
Un nombre ayant 0o ou 0O comme préfixe représente un nombre octal . 

Par exemple, 0O12 est équivalent à l'entier 10.
"""
nbr_octal    = 0o12 # octal

"""
Hexadécimal
Un nombre avec 0x ou 0X comme préfixe représente un nombre hexadécimal . 

Par exemple, 0x12 est équivalent à l'entier 18.
"""
nbr_hexal    = 0x12 # hexadecimal

print()

print("Le nombre binaire converti en numerique : ", nbr_binary, " Son type est       : ", type(nbr_binary))
print("Le nombre octal converti en numerique : ", nbr_octal,  " Son type est         : ", type(nbr_octal))
print("Le nombre hexadecimal converti en numerique : ", nbr_hexal , " Son type est   : ", type(nbr_hexal))