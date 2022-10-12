#! /usr/bin/env python3

""" Module qui va nous permettre de générer l'image PPM"""
import subprocess
import sys
import random
from copy import deepcopy
import time
import numpy
import simulator

deb = time.time()
# ----- Couleurs -----
NOIR = "0 0 0"
WHITE = "255 255 255"
VIOLET = "153 0 255"
BLEU = "51 153 255"

# ----- Variables en entrée -----
taille = int(sys.argv[1])
nb_points = int(sys.argv[2])
chiffres = int(sys.argv[3])

# ----- EXCEPTIONS -----
assert (len(sys.argv) == 4), "Pas le bon nombre d'arguments"
if taille <= 0:
    raise ValueError("taille n'est pas un entier strictement positif")
if nb_points <=0:
    raise ValueError("nb_points n'est pas un entier strictement positif")
if chiffres <= 0:
    raise ValueError("chiffres n'est pas un entier strictement positif")

# ----- Etape 1 : Je définis des tableaux numpy -----
liste = [[WHITE] for _ in range(taille*taille)]
tableau = numpy.array(liste)
tableau = tableau.reshape((taille, taille))
# Copie de tableau pour pouvoir mémoriser les points colorés lors de la transition des images
M = tableau

# ----- Etape 2 : Les fonctions qui implémentent les chiffres -----
def virgule(tableau,emplacement):
    """ Ecrit une virgule dans le cercle selon la taille de l'image. """
    decalage = taille*emplacement//200
    for i in range(int(taille/2 - taille/300), int(taille/2 + taille/300)):
        for j in range(decalage + int(taille/2.25 - taille/250), decalage + \
            int(taille/2.25 + taille/500)):
            tableau[i][j] = NOIR
    return tableau

def une(tableau, emplacement):
    """Ecrit 1 à l'endroit voulu dépendant de la taille de l'image et de l'emplacement."""
    decalage = taille*emplacement//32
    for i in range(int(taille/2 - taille/15), int(taille/2 + taille/300)):
        for j in range(decalage + int(taille/2.3 - taille/350), \
            decalage + int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    return tableau

def deux(tableau, emplacement):
    """Ecrit 2 à l'endroit voulu dépendant de la taille de l'image et de l'emplacement."""
    decalage = taille*emplacement//32
    # ----- Petites barres horizontales -----
    # la première
    for i in range(int(taille/2 - taille/15), int(taille/2 - taille/16)):
        for j in range(decalage + int(taille/2.3 - taille/50), \
            decalage + int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    # la deuxième
    for i in range(int(taille/1.87 - taille/14.5), int(taille/1.87 - taille/16)):
        for j in range(decalage + int(taille/2.3 - taille/50), decalage + \
            int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    # la troisième
    for i in range(int(taille/1.765 - taille/15), int(taille/1.765 - taille/16)):
        for j in range(decalage + int(taille/2.315 - taille/50), decalage + \
            int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    # ----- petite barre verticale droite -----
    for i in range(int(taille/2 - taille/15), int(taille/2.15 + taille/300)):
        for j in range(decalage + int(taille/2.3 - taille/350), decalage + \
            int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    # ----- grande barre gauche -----
    for i in range(int(taille/1.879 - taille/15),int(taille/1.997 + taille/300)):
        for j in range((decalage-(taille*17//800)) + int(taille/2.3 - taille/350), \
            (decalage-(taille*17//800)) + int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    return tableau

def trois(tableau, emplacement):
    """Ecrit 3 à l'endroit voulu dépendant de la taille de l'image et de l'emplacement."""
    decalage = taille*emplacement//32
    # ----- Grande barre droite -----
    for i in range(int(taille/2 - taille/15), int(taille/2 + taille/300)):
        for j in range(decalage + int(taille/2.3 - taille/350), decalage + \
            int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    # ----- Petites barres -----
    # la première
    for i in range(int(taille/2 - taille/15), int(taille/2 - taille/16)):
        for j in range(decalage + int(taille/2.3 - taille/50), decalage + \
            int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    # la deuxième
    for i in range(int(taille/1.87 - taille/14.5), int(taille/1.87 - taille/16)):
        for j in range(decalage + int(taille/2.3 - taille/50), decalage + \
            int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    # la troisième
    for i in range(int(taille/1.765 - taille/15), int(taille/1.765 - taille/16)):
        for j in range(decalage + int(taille/2.315 - taille/50), decalage + \
            int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    return tableau

def quatre(tableau, emplacement):
    """Ecrit 4 à l'endroit voulu dépendant de la taille de l'image et de l'emplacement."""
    decalage = taille*emplacement//32
    # ----- grande barre verticale à droite -----
    for i in range(int(taille/2 - taille/15), int(taille/2 + taille/300)):
        for j in range(decalage + int(taille/2.3 - taille/350), decalage + \
            int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    #  petite barre horizontale
    for i in range(int(taille/1.87 - taille/14.5), int(taille/1.87 - taille/16)):
        for j in range(decalage + int(taille/2.3 - taille/50), decalage + \
            int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    # petite barre verticale gauche
    for i in range(int(taille/2 - taille/15),int(taille/2.135 + taille/300)):
        for j in range((decalage-(taille*17//800)) + int(taille/2.3 - taille/350), \
            (decalage-(taille*17//800)) + int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    return tableau

def cinq(tableau, emplacement):
    """Ecrit 5 à l'endroit voulu dépendant de la taille de l'image et de l'emplacement."""
    decalage = taille*emplacement//32
    # ----- petite barre verticale bas droite -----
    for i in range(int(taille/1.875 - taille/15), int(taille/2 + taille/300)):
        for j in range(decalage + int(taille/2.3 - taille/350), decalage + \
            int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    # ----- petites barres horizontale -----
    # la première
    for i in range(int(taille/2 - taille/15), int(taille/2 - taille/16)):
        for j in range(decalage + int(taille/2.3 - taille/50), decalage + \
            int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    # la deuxième
    for i in range(int(taille/1.87 - taille/14.5), int(taille/1.87 - taille/16)):
        for j in range(decalage + int(taille/2.3 - taille/50), decalage + \
            int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    # la troisième
    for i in range(int(taille/1.765 - taille/15), int(taille/1.765 - taille/16)):
        for j in range(decalage + int(taille/2.315 - taille/50), decalage + \
            int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    # ----- petite barre verticale haut gauche -----
    for i in range(int(taille/2 - taille/15),int(taille/2.135 + taille/300)):
        for j in range((decalage-(taille*17//800)) + int(taille/2.3 - taille/350), \
            (decalage-(taille*17//800)) + int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    return tableau

def six(tableau, emplacement):
    """Ecrit 6 à l'endroit voulu dépendant de la taille de l'image et de l'emplacement."""
    decalage = taille*emplacement//32
    # ----- Grande barre gauche -----
    for i in range(int(taille/2 - taille/15),int(taille/1.997 + taille/300)):
        for j in range((decalage-(taille*17//800)) + int(taille/2.3 - taille/350), \
            (decalage-(taille*17//800)) + int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    # ----- Petites barres -----
    # la première
    for i in range(int(taille/2 - taille/15), int(taille/2 - taille/16)):
        for j in range(decalage + int(taille/2.3 - taille/50), decalage + \
            int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    # la deuxième
    for i in range(int(taille/1.87 - taille/14.5), int(taille/1.87 - taille/16)):
        for j in range(decalage + int(taille/2.3 - taille/50), decalage + \
            int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    # la troisième
    for i in range(int(taille/1.765 - taille/15), int(taille/1.765 - taille/16)):
        for j in range(decalage + int(taille/2.3 - taille/50), decalage + \
            int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    # ----- petite barre verticale droite -----
    for i in range(int(taille/1.875 - taille/15), int(taille/2 + taille/300)):
        for j in range(decalage + int(taille/2.3 - taille/350), decalage + \
            int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    # ----- grande barre gauche -----
    for i in range(int(taille/2 - taille/15),int(taille/1.997 + taille/300)):
        for j in range((decalage-(taille*17//800)) + int(taille/2.3 - taille/350), \
            (decalage-(taille*17//800)) + int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    return tableau

def sept(tableau, emplacement):
    """Ecrit 7 à l'endroit voulu dépendant de la taille de l'image et de l'emplacement."""
    decalage = taille*emplacement//32
    # ----- grande barre droite -----
    for i in range(int(taille/2 - taille/15), int(taille/2 + taille/300)):
        for j in range(decalage + int(taille/2.3 - taille/350), decalage + \
            int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    # ----- petite barre horizontale haute -----
    for i in range(int(taille/2 - taille/15), int(taille/2 - taille/16)):
        for j in range(decalage + int(taille/2.3 - taille/50), decalage + \
            int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    return tableau

def huit(tableau, emplacement):
    """Ecrit 8 à l'endroit voulu dépendant de la taille de l'image et de l'emplacement."""
    decalage = taille*emplacement//32
    # ----- grande barre droite -----
    for i in range(int(taille/2 - taille/15), int(taille/2 + taille/300)):
        for j in range(decalage + int(taille/2.3 - taille/350), decalage + \
            int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    # ----- petites barres ------
    # la première
    for i in range(int(taille/2 - taille/15), int(taille/2 - taille/16)):
        for j in range(decalage + int(taille/2.3 - taille/50), decalage + \
            int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    # la deuxième
    for i in range(int(taille/1.87 - taille/14.5), int(taille/1.87 - taille/16)):
        for j in range(decalage + int(taille/2.3 - taille/50), decalage + \
            int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    # la troisième
    for i in range(int(taille/1.765 - taille/15), int(taille/1.765 - taille/16)):
        for j in range(decalage + int(taille/2.3 - taille/50), decalage + \
            int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    # ----- grande barre gauche -----
    for i in range(int(taille/2 - taille/15),int(taille/1.997 + taille/300)):
        for j in range((decalage-(taille*17//800)) + int(taille/2.3 - taille/350), \
            (decalage-(taille*17//800)) + int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    return tableau

def neuf(tableau, emplacement):
    """Ecrit 9 à l'endroit voulu dépendant de la taille de l'image et de l'emplacement."""
    decalage = taille*emplacement//32
    # ---- grande barre -----
    for i in range(int(taille/2 - taille/15), int(taille/2 + taille/300)):
        for j in range(decalage + int(taille/2.3 - taille/350), decalage + \
            int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    # ----- petites barres ------
    # la première
    for i in range(int(taille/2 - taille/15), int(taille/2 - taille/16)):
        for j in range(decalage + int(taille/2.3 - taille/50), decalage + \
            int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    # la deuxième
    for i in range(int(taille/1.87 - taille/14.5), int(taille/1.87 - taille/16)):
        for j in range(decalage + int(taille/2.3 - taille/50), decalage + \
            int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    # la troisième
    for i in range(int(taille/1.765 - taille/15), int(taille/1.765 - taille/16)):
        for j in range(decalage + int(taille/2.315 - taille/50), decalage + \
            int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    # ----- petite barre verticale gauche -----
    for i in range(int(taille/2 - taille/15),int(taille/2.135 + taille/300)):
        for j in range((decalage-(taille*17//800)) + int(taille/2.3 - taille/350), \
            (decalage-(taille*17//800)) + int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    return tableau

def zero(tableau, emplacement):
    """Ecrit 0 à l'endroit voulu dépendant de la taille de l'image et de l'emplacement."""
    decalage = taille*emplacement//32
    # ----- Grande barre droite -----
    for i in range(int(taille/2 - taille/15), int(taille/2 + taille/300)):
        for j in range(decalage + int(taille/2.3 - taille/350), decalage + \
            int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    # ----- Petites barres -----
    # la première haute
    for i in range(int(taille/2 - taille/15), int(taille/2 - taille/16)):
        for j in range(decalage + int(taille/2.3 - taille/50), decalage + \
            int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR

    # la deuxième basse
    for i in range(int(taille/1.765 - taille/15), int(taille/1.765 - taille/16)):
        for j in range(decalage + int(taille/2.3 - taille/50), decalage + \
            int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    # ----- grande barre gauche ------
    for i in range(int(taille/2 - taille/15),int(taille/1.997 + taille/300)):
        for j in range((decalage-(taille*17//800)) + int(taille/2.3 - taille/350), \
            (decalage-(taille*17//800)) + int(taille/2.3 + taille/350)):
            tableau[i][j] = NOIR
    return tableau


# ----- Etape 3 : La fonction qui génère une image -----
def generate_ppm_file(approx,tableau,nb_points,nb_chiffres,fich):
    """ Génère l'image voulue à partir de l'approx de pi """
    rayon_cercle = taille//2
    centre_cercle = [taille//2, taille//2]

    # ----- Plaçage aléatoire des points de couleur BLEU et VIOLET sur l'image -----
    for _ in range(nb_points):
        i, j = random.randint(0, taille-1), random. randint(0, taille-1)
        if simulator.dans_cercle([i,j], centre_cercle, rayon_cercle) and M[i][j] == WHITE:
            M[i][j] = VIOLET
        elif not(simulator.dans_cercle([i,j], centre_cercle, rayon_cercle)) and M[i][j] == WHITE:
            M[i][j] = BLEU
    tableau = deepcopy(M) # On met à jour le tableau

    # ----- On incrémente p_i dans une liste de chaines de caractères -----
    chaine = []
    for chiffre in str(approx):
        chaine.append(chiffre)
    emplacement = 0
    for k in chaine:
        if k == '.':
            tableau = virgule(tableau, emplacement)
        elif k == '1':
            tableau = une(tableau, emplacement)
            emplacement += 1
        elif k == '2':
            tableau = deux(tableau, emplacement)
            emplacement += 1
        elif k == '3':
            tableau = trois(tableau, emplacement)
            emplacement += 1
        elif k == '4':
            tableau = quatre(tableau, emplacement)
            emplacement += 1
        elif k == '5':
            tableau = cinq(tableau, emplacement)
            emplacement += 1
        elif k == '6':
            tableau = six(tableau, emplacement)
            emplacement += 1
        elif k == '7':
            tableau = sept(tableau, emplacement)
            emplacement += 1
        elif k == '8':
            tableau = huit(tableau, emplacement)
            emplacement +=1
        elif k == '9':
            tableau = neuf(tableau, emplacement)
            emplacement += 1
        elif k == '0':
            tableau = zero(tableau, emplacement)
            emplacement += 1
    # ----- Ajout de zero si le nombre de décimales est inférieur à celui demandé -----
    if len(chaine) < nb_chiffres + 2:
        tableau = zero(tableau, emplacement)
        emplacement += 1

    # ----- Mise en forme l'image sous format ppm dans un fichier *.ppm -----
    chaine = "P3 \n" + f"{taille} {taille} \n" + "255 \n"
    for i in range(taille):
        for j in range(taille):
            if j < taille:
                chaine += tableau[i][j] + ' '
            else:
                chaine += tableau[i][j] + "\n"
    fich.write(chaine)

# ----- Etape 4 : On génère le GIF voulu à partir d'images -----
liste_images = []
for ind in range(10):
    deb_ind = time.time()
    nb = int(nb_points/10)
    p_i = round(simulator.simulation(nb_points), chiffres)
    fichier= open(f'img_pi{ind}_{p_i}.ppm', 'w')
    generate_ppm_file(p_i, tableau, nb, chiffres, fichier)
    fichier.close()
    # ----- On compresse les images en format P6 -----
    cmd_ind = ['convert', f'img_pi{ind}_{p_i}.ppm', f'img_pi{ind}_{p_i}.ppm']
    subprocess.call(cmd_ind)
    liste_images.append(cmd_ind[2])
    nb += int(nb_points/10)
    fin_ind = time.time()
    print(f"l'image {ind} est créée : {round(fin_ind - deb_ind,4)} s")

cmd = ['convert' , '-delay','100', '-loop', '0'] + liste_images + ['montecarlo.gif']
subprocess.call(cmd)

fin = time.time()
print(f"Le module a pris {fin - deb} s pour construire le GIF.")
