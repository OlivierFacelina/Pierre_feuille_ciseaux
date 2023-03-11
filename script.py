team = 'Paris'

# Demander à l'utilisateur de saisir "Paris a gagné" ou "Paris a perdu"
result = input('saisir Paris a gagné ou Paris a perdu')


#Si Paris a gagné, alors tu leur mets 3 points.
if result == 'Paris a gagné':
    score = 3
#Sinon, tu leur enlèves 3 points.
else: score = -3
print(score)