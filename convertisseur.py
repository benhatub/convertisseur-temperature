#importation de tkinter 
import tkinter as tk

#définissons la fonction de conversion 
def fahrenheit_to_celsius():
    try:
        #on récupère la température saisie par l'utilisateur et on la convertit en nombre float
        fahrenheit = float(ent_temperature.get())
        
        #formule de conversion
        celsius = (fahrenheit - 32) * 5 / 9

        #affichage du résultat 
        lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
    except ValueError:
        #si l'utilisateur entre autre chose qu'un nombre, on affiche une erreur
        lbl_result["text"] = "Entrée invalide"

#création de la fenêtre principale
window = tk.Tk()

#définissons le titre de la fenêtre
window.title("Convertisseur de Température")

#rendre la taille de la fenêtre fixe
window.resizable(width=False, height=False)

#création d’un cadre pour contenir l’entrée et le label "°F"
frm_entry = tk.Frame(master=window)

#zone de saisie pour entrer la température en Fahrenheit
ent_temperature = tk.Entry(master=frm_entry, width=10)

#afficher le symbole degré Fahrenheit à côté de l'entrée
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

#placement de l'entrée et du label dans le cadre avec le gestionnaire grid
ent_temperature.grid(row=0, column=0, sticky="e")  
lbl_temp.grid(row=0, column=1, sticky="w")        

#création du bouton pour lancer la conversion
btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",   #flèche vers la droite
    command=fahrenheit_to_celsius        #fonction à appeler lors du clic
)

#affiachage du résultat de la conversion (°C)
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

#placement des éléments dans la fenêtre principale avec padding
frm_entry.grid(row=0, column=0, padx=10)     #le cadre à gauche
btn_convert.grid(row=0, column=1, pady=10)   #le bouton au milieu
lbl_result.grid(row=0, column=2, padx=10)    #le résultat à droite

#lancement de la boucle principale de l'interface graphique (attente des événements)
window.mainloop()
