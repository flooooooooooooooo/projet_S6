import numpy as np
import math
import matplotlib.pyplot as plt
import os
import subprocess

def open_input_file():
    """Ouvre le fichier input et met les informations dans chaque variables"""
    with open(r"C:\Users\avene\Documents\code\programme_complet\projet_calcul_scientifique\projet_S6\input.txt", "r") as f:
        text = f.readlines()

    for line in text:
        line = line.split("=")
        if line[0] == "C_0":
            C_0 = float(line[1])
        elif line[0] == "L":
            L = float(line[1])
        elif line[0] == "x_d":
            x_d = float(line[1])
        elif line[0] == "x_f":
            x_f = float(line[1])
        elif line[0] == "D":
            D = float(line[1])
        elif line[0] == "N_x":
            N_x = int(line[1])
        elif line[0] == "t_fin":
            t_fin = float(line[1])
        elif line[0] == "N_t":
            N_t = int(line[1])
    
    return C_0, L, x_d, x_f, D, N_x, t_fin, N_t

def initialize_data_numerical_solving(t_fin, N_t, L, N_x, C_0, x_d, x_f, D):
    """Initialise les données pour la résolution du schéma numérique"""
    dt = t_fin / (N_t + 1)
    dx = L / (N_x + 1)
    x = 0
    t = 0
    C = np.zeros((N_x+1,N_t+1))
    R = D * dt / (dx ** 2)

    for i in range(0,N_x+1):
        x = i * dx
        if x - x_d < 0 and x - x_f < 0:
            C[i,0] = 0
        elif x - x_d > 0 and x - x_f < 0:
            C[i,0] = C_0
        else:
            C[i,0] = 0
    
    return dt, dx, x, t, C, R

def initialize_data_exact_solving(N_x):
    """Initialise les données pour la résolution exacte"""
    C_verif = np.zeros((N_x+1,N_t+1))
    return C_verif

def solve_concentration_numericaly(N_t, N_x, R, C,t_fin,dt):
    """Résout le schéma numérique"""
    for i in range(0,N_t):
        t = i * dt
        for j in range(0,N_x + 1):
            if j == 0:
                w = 10*math.pi/t_fin
                C[j,i+1] = 1 + 1*math.sin(w*t) # potentiel fonction
            elif j == N_x:
                C[j,i+1] = 0 # potentiel fonction
            else:
                C[j,i+1] = R *C[j-1,i] + (1 - 2 * R) * C[j,i] + R * C[j+1,i]
    return C

def solve_concentration_exactly(dx, dt, C_verif, N_t, N_x, D):
    """Calcul la solution exacte du problème"""
    x = 0
    t = 0
    for j in range(0,N_t+1):
        for i in range(0,N_x+1):
            x = i * dx
            C_verif[i,j] = 1 - math.erf(x/(2*math.sqrt(D*(t))))
        t = j * dt
    return C_verif

def initialize_output_file():
    """Initialise le dossier output"""
    if os.path.isdir("output") == False:
        os.mkdir("output")

def plot_concentration(C, N_t):
    """Plot la concentration en fonction du temps"""
    for i in range(0,N_t+1):
        plt.plot(C[:,i])
        plt.savefig("output/C_000{}.png".format(i))
        plt.clf()

def plot_numerical_exact_comparison(C_verif, C):
    """Plot la comparaison entre la solution exacte et la solution numérique"""
    plt.plot(C_verif[:,N_t])
    plt.plot(C[:,N_t])
    plt.savefig("output/numerical_exact_comparison.png")
    plt.clf()

def video_concentration():
    subprocess.call("ffmpeg -s 800x600 -i output/C_%d.png -vcodec libx264 -crf 25 -pix_fmt yuv420p output/video_concentration.mp4", shell=True)

"""Main"""
C_0, L, x_d, x_f, D, N_x, t_fin, N_t = open_input_file()
dt, dx, x, t, C, R = initialize_data_numerical_solving(t_fin, N_t, L, N_x, C_0, x_d, x_f, D)
C = solve_concentration_numericaly(N_t, N_x, R, C,t_fin,dt)
initialize_output_file()
plot_concentration(C, N_t)
video_concentration()