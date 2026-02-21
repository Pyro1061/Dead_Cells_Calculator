from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage


def calculate(*args):
    total_a.set(total.get())
    try: 
        dano1 = float(base.get())
        dano2 = float(adicional.get())
        per_a = float(percentual.get())
        total.set(float((dano1 + dano2)+((dano1+dano2)*(per_a/100))))
    except ValueError:
        pass


def reset(*args):
    total_a.set(0)
    base.set(0)
    adicional.set(0)
    percentual.set(0)
    total.set(0)


# ===== SISTEMA DE IDIOMA =====
idiomas = {
    "pt": {
        "titulo": "Dead Cells Calculadora",
        "dano_base": "Dano Base:",
        "dano_adicional": "Dano adicional:",
        "percentual": "Percentual adicional de dano:",
        "total": "Dano total da arma:",
        "total_anterior": "Dano total calculado anteriormente:",
        "calcular": "Calcular",
        "resetar": "Resetar",
        "idioma": "Idioma:"
    },

    "en": {
        "titulo": "Dead Cells Calculator",
        "dano_base": "Base Damage:",
        "dano_adicional": "Additional Damage:",
        "percentual": "Additional damage percentage:",
        "total": "Total weapon damage:",
        "total_anterior": "Previously calculated damage:",
        "calcular": "Calculate",
        "resetar": "Reset",
        "idioma": "Language:"
    }
}


def mudar_idioma(*args):
    lang = idioma_var.get()
    textos = idiomas[lang]

    root.title(textos["titulo"])
    label_base.config(text=textos["dano_base"])
    label_adicional.config(text=textos["dano_adicional"])
    label_percentual.config(text=textos["percentual"])
    label_total.config(text=textos["total"])
    label_total_a.config(text=textos["total_anterior"])
    botao_calcular.config(text=textos["calcular"])
    botao_reset.config(text=textos["resetar"])
    label_idioma.config(text=textos["idioma"])


# ===== INTERFACE =====
root = Tk()
root.title("Dead Cells Calculadora")
root.iconbitmap("panchaku.ico")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


# Seletor de idioma
idioma_var = StringVar(value="pt")

label_idioma = ttk.Label(mainframe, text="Idioma:")
label_idioma.grid(column=1, row=0, sticky=E)

idioma_menu = ttk.OptionMenu(mainframe, idioma_var, "pt", "pt", "en", command=mudar_idioma)
idioma_menu.grid(column=2, row=0, sticky=W)


# Entradas
base = StringVar()
base_Entrada = ttk.Entry(mainframe, width=7, textvariable=base)
base_Entrada.grid(column=2, row=1, sticky=(W, E))

adicional = StringVar()
adicional_Entrada = ttk.Entry(mainframe, width=7, textvariable=adicional)
adicional_Entrada.grid(column=2, row=2, sticky=(W, E))

percentual = StringVar()
percentual_Entrada = ttk.Entry(mainframe, width=7, textvariable=percentual)
percentual_Entrada.grid(column=2, row=3, sticky=(W, E))


# Resultados
total = StringVar()
ttk.Label(mainframe, textvariable=total).grid(column=2, row=4, sticky=(W, E))

total_a = StringVar()        
ttk.Label(mainframe, textvariable=total_a).grid(column=2, row=5, sticky=(W, E))


# Labels (guardados em variáveis para tradução)
label_base = ttk.Label(mainframe)
label_base.grid(column=1, row=1, sticky=E)

label_adicional = ttk.Label(mainframe)
label_adicional.grid(column=1, row=2, sticky=E)

label_percentual = ttk.Label(mainframe)
label_percentual.grid(column=1, row=3, sticky=E)

label_total = ttk.Label(mainframe)
label_total.grid(column=1, row=4, sticky=E)

label_total_a = ttk.Label(mainframe)
label_total_a.grid(column=1, row=5, sticky=E)


# Botões
botao_calcular = ttk.Button(mainframe, command=calculate)
botao_calcular.grid(column=3, row=5, sticky=W)

botao_reset = ttk.Button(mainframe, command=reset)
botao_reset.grid(column=3, row=4, sticky=W)


reset()

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

base_Entrada.focus()
root.bind("<Return>", calculate)

mudar_idioma()  # define idioma inicial
root.mainloop()