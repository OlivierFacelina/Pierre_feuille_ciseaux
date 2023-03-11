import random

# Déclaration de variable 
player_score = 0
ordi_score = 0
round_player = 0
round_ordi = 0
win_game_player = 0
win_game_ordi = 0

# • L’utilisateur pourra choisir parmi les 3 signes à l’aide de son pavé numérique, tant que la
# saisie ne sera pas valide, le programme lui demandera une nouvelle saisie

# On boucle tant que le nombre de manches est inférieur à 3
while round_player < 3 or round_ordi < 3:
    sign = input("Choisir entre 3 signes : pierre, feuille, ciseaux")
    while sign != 'Pierre' and sign != 'Feuille' and sign != 'Ciseaux':
        print("Saisie invalide")
        sign = input("Choisir entre 3 signes : pierre, feuille, ciseaux")   

    sign_list = ["Pierre","Feuille","Ciseaux"]
    player_sign = sign 
    # print(f"Le joueur a pris : {player_sign}")
    player_ordi = random.choice(sign_list)
    print(f"L'ordi a tiré au sort : {player_ordi}")

 
    #Condition de victoire
    if player_sign == 'Pierre' and player_ordi == 'Ciseaux' or player_sign == 'Ciseaux' and player_ordi == 'Feuille' or player_sign == 'Feuille' and player_ordi == 'Pierre':
        player_score += 1
        round_player += 1
        # print(round_player)
        print(f"BRAVOOOO ! Score actuel : {player_score} - {ordi_score}")
        if round_player == 3:
            win_game_player += 1
            print(f"Vous avez gagné la partie !!! Score final : {player_score} - {ordi_score}")
            print(f"Nombre total de partie gagnée pour le joueur : {win_game_player}")
            restart = input("Voulez-vous rejouer une partie ? O/N")
            if restart == 'O':
                player_score = 0
                ordi_score = 0
                round_player = 0
                round_ordi = 0
            elif restart == 'N': 
                break
            else: 
                print("Saisie invalide")
                restart = input("Voulez-vous rejouer une partie ? O/N")
        
    #Egalité
    if player_sign == player_ordi:
        print(f"Egalité. Score actuel : {player_score} - {ordi_score}")

    #Condition de défaite
    if player_sign == 'Ciseaux'and player_ordi == 'Pierre' or player_sign == 'Feuille' and player_ordi == 'Ciseaux' or player_sign == 'Pierre' and player_ordi == 'Feuille':
        ordi_score += 1
        round_ordi += 1
        # print(round_ordi)
        print(f"Noooon. Score actuel : {player_score} - {ordi_score}")
        if round_ordi == 3:
            win_game_ordi += 1
            print(f"Vous avez perdu la partie... Score final : {player_score} - {ordi_score}")
            print(f"Nombre total de partie gagnée pour l'ordi : {win_game_ordi}")
            restart = input("Voulez-vous rejouer une partie ? O/N")
            if restart == 'O':
                player_score = 0
                ordi_score = 0
                round_player = 0
                round_ordi = 0
            elif restart == 'N': 
                break
            else: 
                print("Saisie invalide")
                restart = input("Voulez-vous rejouer une partie ? O/N")
                

    