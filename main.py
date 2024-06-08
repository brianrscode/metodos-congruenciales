# CSpell: disable
from tkinter import *
from tkinter import ttk
from metodos import *


def mostrar_resultado_cuadrados_medios(semilla):
    resultado = cuadrados_medios(semilla)
    salida_p1.delete(1.0, END)
    salida_p1.insert(END, resultado)


def mostrar_resultado_productos_medios(x0, x1):
    resultado = productos_medios(x0, x1)
    salida_p2.delete(1.0, END)
    salida_p2.insert(END, resultado)


def mostrar_resultado_multiplicador_constante(x0, a):
    resultado = multiplicador_constante(x0, a)
    salida_p3.delete(1.0, END)
    salida_p3.insert(END, resultado)


########################


def mostrar_resultado_lineal(x0, k, g, c):
    resultado = algoritmo_congruencial_lineal(x0, k, g, c)
    salida_1.delete(1.0, END)
    salida_1.insert(END, resultado)


def mostrar_resultado_multiplicativo(x0, k, g, formula):
    resultado = algoritmo_congruencial_multiplicativo(x0, k, g, formula)
    salida_2.delete(1.0, END)
    salida_2.insert(END, resultado)


def mostrar_resultado_aditivo(semillas, m):
    resultado = algoritmo_congruencial_aditivo(semillas, m)
    salida_3.delete(1.0, END)
    salida_3.insert(END, resultado)


def mostrar_resultado_congruencial_cuadratico(x0, m, a, b, c):
    resultado = algoritmo_congruencial_cuadratico(x0, m, a, b, c)
    salida_4.delete(1.0, END)
    salida_4.insert(END, resultado)


root = Tk()

##### Configuraciones para fuente y espaciado entre elementos #####
paddings = lambda x=10, y=10: {"padx": x, "pady": y}
fuente = lambda fn="Arial", tam=12: {"font": (fn, tam)}


def ventana_no_congruenciales():
    global salida_p1, salida_p2, salida_p3

    ventana_no_congruenciales = Toplevel(root)
    ventana_no_congruenciales.geometry("400x450")
    ventana_no_congruenciales.title("Métodos No Congruenciales")

    ################## Pestañas que contiene el panel ######################
    ########################################################################
    # Permite hacer un panel donde se almacenan las pestañas (tabs)
    panel = ttk.Notebook(ventana_no_congruenciales)
    panel.pack(fill="both", expand="yes")

    tab1 = ttk.Frame(panel)
    panel.add(tab1, text="Cuadrados medios")
    tab2 = ttk.Frame(panel)
    panel.add(tab2, text="Productos medios")
    tab3 = ttk.Frame(panel)
    panel.add(tab3, text="Multiplicador constante")

    ############# Contenido Pestaña 1 #############
    ###############################################
    label_semilla_p1 = ttk.Label(tab1, text="Ingresa la semilla:", **fuente()).pack(
        **paddings()
    )
    entry_semilla_p1 = ttk.Entry(tab1)
    entry_semilla_p1.pack(**paddings())
    boton_p1 = ttk.Button(
        tab1,
        text="Generar",
        command=lambda: mostrar_resultado_cuadrados_medios(int(entry_semilla_p1.get())),
    ).pack(**paddings())
    salida_p1 = Text(tab1, wrap=WORD, **fuente("Helvetica", 10))
    salida_p1.pack(fill="x", **paddings())

    ############# Contenido Pestaña 2 #############
    ###############################################
    label_semilla1_p2 = ttk.Label(tab2, text="Ingresa la semilla 1:", **fuente()).pack(
        **paddings(x=10, y=5)
    )
    entry_semilla1_p2 = ttk.Entry(tab2)
    entry_semilla1_p2.pack(**paddings(x=5, y=5))
    label_semilla2_p2 = ttk.Label(tab2, text="Ingresa la semilla 2:", **fuente()).pack(
        **paddings(x=10, y=5)
    )
    entry_semilla2_p2 = ttk.Entry(tab2)
    entry_semilla2_p2.pack(**paddings(x=5, y=5))
    boton_p2 = ttk.Button(
        tab2,
        text="Generar",
        command=lambda: mostrar_resultado_productos_medios(
            int(entry_semilla1_p2.get()), int(entry_semilla2_p2.get())
        ),
    )
    boton_p2.pack(**paddings())
    salida_p2 = Text(tab2, wrap=WORD, **fuente("Helvetica", 10))
    salida_p2.pack(fill="x", **paddings())

    ############# Contenido Pestaña 3 #############
    ###############################################
    label_semilla_p3 = ttk.Label(tab3, text="Ingresa la semilla:", **fuente()).pack(
        **paddings(x=10, y=5)
    )
    entry_semilla_p3 = ttk.Entry(tab3)
    entry_semilla_p3.pack(**paddings(x=5, y=5))
    label_constante_p3 = ttk.Label(tab3, text="Ingresa la constante:", **fuente()).pack(
        **paddings(x=10, y=5)
    )
    entry_constante_p3 = ttk.Entry(tab3)
    entry_constante_p3.pack(**paddings(x=5, y=5))
    boton_p3 = ttk.Button(
        tab3,
        text="Generar",
        command=lambda: mostrar_resultado_multiplicador_constante(
            int(entry_semilla_p3.get()), int(entry_constante_p3.get())
        ),
    )
    boton_p3.pack(**paddings())
    salida_p3 = Text(tab3, wrap=WORD, **fuente("Helvetica", 10))
    salida_p3.pack(fill="x", **paddings())


def ventana_congruenciales():
    global salida_1, salida_2, salida_3, salida_4  # , salida_5
    ventana_congruenciales = Toplevel(root)
    ventana_congruenciales.geometry("400x450")
    ventana_congruenciales.title("Métodos Congruenciales")

    ################## Pestañas que contiene el panel ######################
    ########################################################################
    # Permite hacer un panel donde se almacenan las pestañas (tabs)
    panel = ttk.Notebook(ventana_congruenciales)
    panel.pack(fill="both", expand="yes")

    tab1 = ttk.Frame(panel)
    panel.add(tab1, text="Lineal")
    tab2 = ttk.Frame(panel)
    panel.add(tab2, text="Multiplicativo")
    tab3 = ttk.Frame(panel)
    panel.add(tab3, text="Aditivo")
    tab4 = ttk.Frame(panel)
    panel.add(tab4, text="Cuadrático")
    # tab5 = ttk.Frame(panel)
    # panel.add(tab5, text="Blum, Blum, Shub")

    ############# Contenido Pestaña 1 #############
    ###############################################
    label_semilla_1 = ttk.Label(tab1, text="Ingresa la semilla:", **fuente()).pack()
    entry_semilla_1 = ttk.Entry(tab1)
    entry_semilla_1.pack()
    label_k_1 = ttk.Label(tab1, text="Ingresa k:", **fuente()).pack()
    entry_k_1 = ttk.Entry(tab1)
    entry_k_1.pack()
    label_g_1 = ttk.Label(tab1, text="Ingresa g:", **fuente()).pack()
    entry_g_1 = ttk.Entry(tab1)
    entry_g_1.pack()
    label_constante_1 = ttk.Label(tab1, text="Ingresa c:", **fuente()).pack()
    entry_constante_1 = ttk.Entry(tab1)
    entry_constante_1.pack()

    boton_1 = ttk.Button(
        tab1,
        text="Generar",
        command=lambda: mostrar_resultado_lineal(
            int(entry_semilla_1.get()),
            int(entry_k_1.get()),
            int(entry_g_1.get()),
            int(entry_constante_1.get()),
        ),
    ).pack(**paddings(x=5, y=5))
    salida_1 = Text(tab1, wrap=WORD, **fuente("Helvetica", 10))
    salida_1.pack(fill="x")

    ############# Contenido Pestaña 2 #############
    ###############################################
    label_semilla_2 = ttk.Label(tab2, text="Ingresa la semilla:", **fuente()).pack()
    entry_semilla_2 = ttk.Entry(tab2)
    entry_semilla_2.pack()

    label_k_2 = ttk.Label(tab2, text="Ingresa k:", **fuente()).pack()
    entry_k_2 = ttk.Entry(tab2)
    entry_k_2.pack()
    label_g_2 = ttk.Label(tab2, text="Ingresa g:", **fuente()).pack()
    entry_g_2 = ttk.Entry(tab2)
    entry_g_2.pack()
    label_formula_a_2 = ttk.Label(
        tab2, text="Selecciona una formula", **fuente()
    ).pack()
    formula_a = ttk.Combobox(
        tab2, state="readonly", values=["a = 3 + 8k", "a = 5 + 8k"]
    )
    formula_a.pack()
    formula_a.set("a = 3 + 8k")

    boton_2 = ttk.Button(
        tab2,
        text="Generar",
        command=lambda: mostrar_resultado_multiplicativo(
            int(entry_semilla_2.get()),
            int(entry_k_2.get()),
            int(entry_g_2.get()),
            formula_a.get(),
        ),
    ).pack(**paddings(x=5, y=5))

    salida_2 = Text(tab2, wrap=WORD, **fuente("Helvetica", 10))
    salida_2.pack(fill="x")

    ############# Contenido Pestaña 3 #############
    ###############################################
    label_semillas_3 = ttk.Label(
        tab3, text="Ingresa todas las semillas separadas por un espacio", **fuente()
    ).pack()
    entry_semillas_3 = ttk.Entry(tab3)
    entry_semillas_3.pack()

    label_m_3 = ttk.Label(tab3, text="Ingresa m:", **fuente()).pack()
    entry_m_3 = ttk.Entry(tab3)
    entry_m_3.pack()

    boton_3 = ttk.Button(
        tab3,
        text="Generar",
        command=lambda: mostrar_resultado_aditivo(
            list(map(int, entry_semillas_3.get().split())), int(entry_m_3.get())
        ),
    ).pack(**paddings(x=5, y=5))

    salida_3 = Text(tab3, wrap=WORD, **fuente("Helvetica", 10))
    salida_3.pack(fill="x")

    ############# Contenido Pestaña 4 #############
    ###############################################
    label_semilla_4 = ttk.Label(tab4, text="Ingresa la semilla:", **fuente()).pack()
    entry_semilla_4 = ttk.Entry(tab4)
    entry_semilla_4.pack()

    label_m_4 = ttk.Label(tab4, text="Ingresa m:", **fuente()).pack()
    entry_m_4 = ttk.Entry(tab4)
    entry_m_4.pack()

    label_a_4 = ttk.Label(tab4, text="Ingresa a:", **fuente()).pack()
    entry_a_4 = ttk.Entry(tab4)
    entry_a_4.pack()

    label_b_4 = ttk.Label(tab4, text="Ingresa b:", **fuente()).pack()
    entry_b_4 = ttk.Entry(tab4)
    entry_b_4.pack()

    label_c_4 = ttk.Label(tab4, text="Ingresa c:", **fuente()).pack()
    entry_c_4 = ttk.Entry(tab4)
    entry_c_4.pack()

    boton_4 = ttk.Button(
        tab4,
        text="Generar",
        command=lambda: mostrar_resultado_congruencial_cuadratico(
            int(entry_semilla_4.get()),
            int(entry_m_4.get()),
            int(entry_a_4.get()),
            int(entry_b_4.get()),
            int(entry_c_4.get()),
        ),
    ).pack(**paddings(x=5, y=5))

    salida_4 = Text(tab4, wrap=WORD, **fuente("Helvetica", 10))
    salida_4.pack(fill="x")


######################### Menú principal #########################
##################################################################
boton_metodos_no_congruenciales = ttk.Button(
    root, text="Métodos No Congruenciales", command=ventana_no_congruenciales
).pack(**paddings())

boton_congruenciales = ttk.Button(
    root, text="Métodos Congruenciales", command=ventana_congruenciales
).pack(**paddings())

############# Propiedades de la ventana principal #############
###############################################################
root.title("Algoritmos")
root.geometry("210x100")  # 210x100
root.mainloop()
