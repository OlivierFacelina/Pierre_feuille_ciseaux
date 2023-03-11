# Déclarez les variables pour deux joueurs.
elodie = 'joueuse' 
olivier = 'joueur' 
# Leur demander de choisir si c'est pile ou si c'est face 
result = input('saisir cest pile ou cest face' )
# Si c'est pile, affiche il a gagné. 
if result == 'cest pile':
    score = 10
    print('il a gagné')
# Sinon, il a perdu
else: 
    score = -2
    print('il a perdu')
# Sinon, tu lui enlèves 2 points
print(f"Ton score est de : {score}")