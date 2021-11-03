# forme générale
if (une condition ici):
    # ...
    # des instructions ici
    # ...
else:
    # ...
    # des instructions ici
    # ...

# affichage si un test est vrai
temperature = 28
if temperature>25:
    print('il fait chaud !')

# affichages distincts selon un test
temperature = 28
if temperature>25:
    print('il fait chaud !')
else:
    print('il fait frais...')

# enchaînement de tests
temperature = 28
if temperature>25:
    print('il fait chaud !')
elif temperature>20:
    print('il fait bon.')
else:
    print('il fait frais...')
