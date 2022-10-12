#! /usr/bin/env python3
"Ce module se charge uniquement du calcul d'une approximation de π. "

import random
import time
import sys

def dans_cercle(point, centre, rayon):
    """ Renvoie True si le point est dans le cercle, False sinon."""
    return (point[0] - centre[0])**2 + (point[1] - centre[1])**2 <= rayon**2

def simulation(nb_points):
    " On prend un entier et on applique la méthode de Monte Carlo."
    compteur = 0
    abscisse, ordonnee = 0, 0
    for _ in range(nb_points):
        abscisse, ordonnee = random.uniform(-1, 1), random.uniform(-1, 1)
        if dans_cercle([abscisse,ordonnee], [0,0], 1):
            compteur += 1
    return 4*compteur/nb_points

def main():
    """ Renvoie l'approximation"""
    # ----- Entrées -----
    taille = int(sys.argv[1])
    nb_points=int(sys.argv[2])
    # ----- Exceptions -----
    assert (len(sys.argv) == 3), "PAS LE BON NOMBRE D'ARGUMENTS"
    if nb_points <= 0:
        raise ValueError("nb_points n'est pas un entier strictement positif")
    if taille <= 0:
        raise ValueError("taille n'est pas un entier strictement positif")

    deb = time.time()
    print(simulation(nb_points))
    fin = time.time()
    print(fin-deb)

if __name__ == "__main__":
    main()
