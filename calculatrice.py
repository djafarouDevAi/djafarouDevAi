import tkinter as tk

def calculer(expression):
    try:
        return str(eval(expression))
    except Exception as e:
        return "Erreur: " + str(e)

def ajouter_caractere(caractere):
    champ_texte.insert(tk.END, caractere)

def effacer():
    champ_texte.delete(0, tk.END)

def bouton_clic(bouton):
    if bouton == '=':
        expression = champ_texte.get()
        resultat = calculer(expression)
        champ_texte.delete(0, tk.END)
        champ_texte.insert(tk.END, resultat)
    elif bouton == 'C':
        effacer()
    else:
        ajouter_caractere(bouton)

fenetre = tk.Tk()
fenetre.title("Calculatrice")

# Agrandir la fenêtre et centrer
fenetre_width = 200
fenetre_height = 300
screen_width = fenetre.winfo_screenwidth()
screen_height = fenetre.winfo_screenheight()
position_top = int(screen_height / 2 - fenetre_height / 2)
position_right = int(screen_width / 2 - fenetre_width / 2)
fenetre.geometry(f"{fenetre_width}x{fenetre_height}+{position_right}+{position_top}")

# Champ de texte
champ_texte = tk.Entry(fenetre)
champ_texte.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Boutons
boutons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

row_val = 1
col_val = 0
for bouton in boutons:
    tk.Button(fenetre, text=bouton, width=5, command=lambda b=bouton: bouton_clic(b)).grid(row=row_val, column=col_val, sticky="nsew")
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Configuration du redimensionnement des boutons
for i in range(4):
    fenetre.grid_columnconfigure(i, weight=1)
    fenetre.grid_rowconfigure(i + 1, weight=1)

fenetre.mainloop()
 
