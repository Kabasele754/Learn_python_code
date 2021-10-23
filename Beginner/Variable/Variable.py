
# Les noms de variables doivent être de la forme :
# ma_variable
# ma_variable1
# ma_variable_1
# mon_module

# Les constantes sont écrites en majuscules :

# MA_CONSTANTE
# MA_CONSTANTE1
# MA_CONSTANTE_1

"""
Types de données en Python

Python intègre par défaut les types de données suivants, dans ces catégories :

Types numériques :		int, float, complex
Type de texte :			str
Type booléen :			bool
Types de séquences :		list, tuple, range
Type de mappage :		dict
Types d'ensemble :		set, frozenset
Types binaires :			bytes, bytearray, memoryview

"""

# Declaration de variable et initialisation ou affectation des valeurs à l'aide de l'oparateur =

# Exemple Types numériques 1 int, float, complex

print(" Exemple Types numériques 1 int, float, complex ")
print() # Separarer le deux codes pour la visibilité

# 1.1 Type entier declaration et assignation de trois manieres
nombre_entier = 123456789
nombre_entier1 = int(123789)
nombre_entier2 : int = 456321

# 1.2 Type float declaration et assignation de trois manieres
nombre_float = 1.23456789
nombre_float1 = float(12.345)
nombre_float2 : float = 123.45

# 1.3 Type complexe declaration et assignation trois manieres
nombre_complex = 123j
nombre_complex1 = complex(12j)
nombre_complex2 : complex = 1j

# Une autre facon d'initialialiser une variable  
nombre_entier_vide1  = int() # une variable vide de type entier
#nombre_entier_vide2  : int   # une variable vide de type entier

nombre_float_vide1   = float() # une variable vide de type float
nombre_float_vide2   : float  # une variable vide de type float

nombre_complex_vide1 = complex() # une variable vide de type complexe
nombre_complex_vide2 : complex


# Afficher type 1.1 entier
print("je suis une valeur : ", nombre_entier, " du type ", type(nombre_entier))
# Afficher type 1.2 float
print("je suis une valeur : ", nombre_float, " du type ", type(nombre_float))
# Afficher type 1.3 complexe
print("je suis une valeur : ", nombre_complex, " du type ", type(nombre_complex))

# Affiché  Une autre facon d'initialialiser une variable avec sa valeur

print()
# Afficher type 1.1 entier
print("je suis une valeur vide : ", nombre_entier_vide1, " toujour du type ", type(nombre_entier_vide1))
#print("je suis une valeur vide : ", nombre_entier_vide2, " toujour du type ", type(nombre_entier_vide2))

print()
# Afficher type 1.2 float
print("je suis une valeur vide : ", nombre_float_vide1, " toujour du type ", type(nombre_float_vide1))
#print("je suis une valeur vide : ", nombre_float_vide2, " toujour du type ", type(nombre_float_vide2))


print()
# Afficher type 1.3 complexe
print("je suis une valeur vide : ", nombre_complex_vide1, " toujour du type ", type(nombre_complex_vide1))

# Exemple Types string 2

print() #Separarer les inscructions de types de donnés pour la visibilité

print(" Exemple Types string 2 ")

print() # Separarer le deux codes pour la visibilité

ma_chaine   = "Je suis une chaine de caracteur "
ma_chaine_1 = 'Je suis une autre chaine de caracteur '
# Une autre facon d'initialialiser une variable 
ma_chaine_vide1 = "" # une chaine vide
ma_chaine_vide_2 = str() # une chaine vide
ma_chaine_vide_3 : str 

# Afficher type string 2
print("je suis une valeur : ", ma_chaine, " du type ", type(ma_chaine))
print("je suis une valeur : ", ma_chaine_1, " du type ", type(ma_chaine_1))
# Affiché  Une autre facon d'initialialiser une variable 
print()
print("je suis une valeur vide : ", ma_chaine_vide1, " toujour du type ", type(ma_chaine_vide1))
print("je suis une valeur vide : ", ma_chaine_vide_2, " toujour du type ", type(ma_chaine_vide_2))

print() # Separarer les inscructions de types de donnés pour la visibilité

# Exemple Types boolean False et True

print(" Exemple Types boolean 3 ")

print() # Separarer le deux codes pour la visibilité

ma_bool = True
ma_bool_1 = False

# Une autre facon d'initialialiser une variable 
ma_bool_vide1 = bool()
ma_bool_vide2 : bool

# Afficher type boolean 3
print("je suis une valeur : ", ma_bool, " du type ", type(ma_bool))
print("je suis une valeur : ", ma_bool_1, " du type ", type(ma_bool_1))

# Affiché  Une autre facon d'initialialiser une variable 
print()
print("je suis une valeur vide : ", ma_bool_vide1, " toujour du type ", type(ma_bool_vide1))
