Nom du programme : main.py

Date de dernière modification : 16/06/2023

# Auteur : 
Alison Da Silva, Florio Avenel

# Objectif :  
Programme de resolution d'une equation de diffusion
par une methode de différence finie
(schéma Euler explicite en temps et centré en espace)

# Fichier d'entrée:   
Le fichier d'entrée est un fichier texte qui sera selectionner dans le programme si le module tkinter
est installé, sinon il faut le mettre dans le répertoire du programme
avec le nom "input.txt"
le fichier doit être de la forme:
```
C_0=
L=
x_d=
x_f=
D=
N_x=
t_fin=
N_t=
boundary_0=
boundary_L=
```

les fonctions dans les deux conditions aux limites peuvent contenir: pi, cos, sin, exp, t, *, +, -, /

# Fichiers résultats :
Création de graphique: 
![Exemple de graphique](assets/Concentration_boundary_0.png)
images et vidéos stocké dans le dossier output dans le répertoire du programme


# Pour exécuter le programme : 
Afin d'exécuter le programme il faut utiliser la commande `python3 main.py` ou `python main.py`

# Module python aditionnel 
+ module nécessaire : numpy, matplotlib, os, sys, math, subprocess
+ module optionnel : concurrent futures, functools, tkinter