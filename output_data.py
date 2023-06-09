"""import de modules"""
import os
import subprocess
import matplotlib.pyplot as plt
import numpy as np

"""import de modules facultatifs et possiblement non présent d'origine sur python"""
try:
    import concurrent.futures
    from functools import partial
except:
    pass

def initialize_output_file():
    """Initialise le dossier output"""
    if os.path.isdir("output") == False:
        os.mkdir("output")

def create_save_plot(dt,max,C,i):
    """Créer et sauvegarde un graphique de la concentration en fonction de la position à un temps donné"""
    
    plt.plot(C)
    plt.title("Concentration en fonction de la position à t = {} s".format(round(i*dt,2)))
    plt.xlabel("Position")
    plt.ylabel("Concentration")
    plt.ylim(-0.1, max + 0.1)
    plt.savefig("output/C_000{}.png".format(i))
    plt.clf()

def plot_concentration(C, N_t,dt):
    """Fait un graphique de la concentration pour chaque pas de temps calculé"""
    if os.path.isdir("output") == False:
        initialize_output_file()
    if os.path.isfile("output/C_0000.png") == True:
        answer = input("des images existe déjà dans le fichier output(elles seront supprimées), voulez-vous continuez ? (O/N)")
        if answer == "N":
            input("renomer les images ou déplacer les avant de continuer, une fois fait appuyer sur entrer pour continuer")
        else:
            subprocess.call("rm output/C_00*", shell=True)
            initialize_output_file()
    if N_t > 1000:
        print("Le temps de production des graphiques peut être long")
    C = np.transpose(C)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(partial(create_save_plot,dt,C.max()),C,range(0,N_t))
    print("Les graphiques ont été créés et sauvegardés dans le dossier output")

def plot_numerical_exact_comparison(C_verif, C, N_t):
    """Fait un graphique de la comparaison entre la solution exacte et la solution numérique"""
    plt.plot(C_verif[:,N_t-1], color="blue", linestyle="solid")
    plt.plot(C[:,N_t-1], color="red", linestyle="dashed")

    plt.plot(C_verif[:,int((N_t-1)*1/100)], color="blue", linestyle="solid")
    plt.plot(C[:,int((N_t-1)*1/100)], color="red", linestyle="dashed")
    
    plt.plot(C_verif[:,int((N_t-1)*0.50/100)], color="blue", linestyle="solid")
    plt.plot(C[:,int((N_t-1)*0.50/100)], color="red", linestyle="dashed")

    plt.plot(C_verif[:,int((N_t-1)*0.10/100)], color="blue", linestyle="solid")
    plt.plot(C[:,int((N_t-1)*0.10/100)], color="red", linestyle="dashed")

    plt.plot(C_verif[:,int((N_t-1)*0.05/100)], color="blue", linestyle="solid")
    plt.plot(C[:,int((N_t-1)*0.05/100)], color="red", linestyle="dashed")

    plt.plot(C_verif[:,int((N_t-1)*0.01/100)], color="blue", linestyle="solid")
    plt.plot(C[:,int((N_t-1)*0.01/100)], color="red", linestyle="dashed")
    
    plt.plot(C_verif[:,int((N_t-1)*0.001/100)], color="blue", linestyle="solid")
    plt.plot(C[:,int((N_t-1)*0.001/100)], color="red", linestyle="dashed")
    plt.title("Comparaison entre la solution exacte et la solution numérique")
    plt.xlabel("Position")
    plt.ylabel("Concentration")
    plt.legend(["Solution exacte", "Solution numérique"])
    plt.savefig("output/numerical_exact_comparison.png")
    plt.clf()

def video_concentration():
    """fait une vidéo de la concentration en fonction de la position à chaque pas de temps avec les images déja créées"""
    if os.path.isfile("output/video_concentration.mp4") == True:
        answer = input("une vidéo existe déjà voulez-vous la supprimer ?(O/N)")
        if answer == "O":
            input("Appuyer sur entrer pour supprimer la vidéo")
        elif answer == "N":
            input("renomer la vidéo avant de continuer, une fois renommer appuyer sur entrer pour continuer")
        os.remove("output/video_concentration.mp4")
    if os.path.isfile("output/C_0000.png") == True:
        subprocess.call("ffmpeg -s 800x600 -i output/C_000%d.png -vcodec libx264 -crf 25 -pix_fmt yuv420p output/video_concentration.mp4",shell=True)
    else:
        print("Pas de fichier image à convertir en vidéo")

def end_plot(C,N_t,N_x,t_fin):
    """Plot la concentration en fonction de la position à la fin du calcul"""
    x_coord = np.linspace(0,1000,N_x)
    plt.plot(x_coord,C[:,N_t-1])
    plt.title("Concentration en fonction de la position à t = {} s".format(t_fin))
    plt.xlabel("Position")
    plt.ylabel("Concentration")
    plt.show()