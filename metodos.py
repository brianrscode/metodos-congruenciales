
N_NUMEROS = 15  # Cantidad de números a generar

#######################################################
############## MÉTODOS NO CONGRUENCIALES ##############
#######################################################

def obtener_centrales(n: int) -> str:
    """Obtiene los 4 dígitos centrales de un número"""
    centrales = str(n)
    if len(centrales) % 2 != 0:
        centrales = "0" + centrales
    if len(centrales) == 8:
        centrales = centrales[2:6]
    elif len(centrales) == 6:
        centrales = centrales[1:5]
    elif len(centrales) == 4:
        pass

    return centrales


def cuadrados_medios(semilla: int) -> str:
    """Algoritmo de cuadrados medios"""
    salida = ""
    for i in range(N_NUMEROS):
        y_n = semilla ** 2

        centrales = obtener_centrales(y_n)

        salida += f"y_{i} = ({semilla})^2 = {y_n} = {centrales}\n"
        salida += f"x_{i+1} = {centrales}\n"
        salida += f"r_{i+1} = 0.{centrales}\n"
        salida += "\n"
        semilla = int(centrales)

    return salida


def productos_medios(x0: int, x1: int) -> str:
    """Algoritmo de productos medios"""
    salida = ""
    for i in range(N_NUMEROS):
        y_n = x0 * x1
        centrales = obtener_centrales(y_n)

        salida += f"y_{i} = {x0} * {x1} = {y_n} = {centrales}\n"
        salida += f"x_{i+1} = {centrales}\n"
        salida += f"r_{i+1} = 0.{centrales}\n"
        salida += "\n"

        x0 = x1
        x1 = int(centrales)

    return salida


def multiplicador_constante(x0: int, a: int) -> str:

    salida = ""

    for i in range(N_NUMEROS):
        y_n = a * x0

        centrales = obtener_centrales(y_n)

        salida += f"y_{i} = ({a}) * ({x0}) = {y_n} = {centrales}\n"
        salida += f"x_{i+1} = {centrales}\n"
        salida += f"r_{i+1} = 0.{centrales}\n"
        salida += "\n"

        x0 = int(centrales)

    return salida


####################################################
############## MÉTODOS CONGRUENCIALES ##############
####################################################

def algoritmo_congruencial_lineal(x0: int, k: int, g: int, c: int):
    salida = ""
    a = 1 + 4 * k
    m = 2**g

    for i in range(N_NUMEROS):
        x_n = (a * x0 + c) % m
        r_n = x_n / (m - 1)

        salida += f"x_{i+1} = ({a} * {x0} + {c}) mod {m} = {x_n}\n"
        salida += f"r_{i+1} = {x_n} / ({m} - 1) = {r_n:.4f}\n"
        salida += "\n"

        x0 = x_n

    return salida

def algoritmo_congruencial_multiplicativo(x0: int, k: int, g: int, formula: str):
    a:int
    if formula == "a = 3 + 8k":
        a = 3 + 8 * k
    elif formula == "a = 5 + 8k":
        a = 5 + 8 * k
    salida = ""
    m = 2**g
    if x0 % 2 == 0:
        return "x0 no puede ser par"

    for i in range(N_NUMEROS):
        x_n = (a * x0) % m
        r_n = x_n / (m - 1)

        salida += f"x_{i+1} = ({a} * {x0}) mod {m} = {x_n}\n"
        salida += f"r_{i+1} = {x_n} / {m - 1} = {r_n:.4f}\n"
        salida += "\n"
        x0 = x_n

    return salida


def algoritmo_congruencial_aditivo(semillas: list, m: int):
    salida = ""
    tam_original = len(semillas)

    for i in range(N_NUMEROS):  # Generación de números
        nuevo_valor = (semillas[i] + semillas[-1]) % m
        semillas.append(nuevo_valor)

    for i in range(tam_original):  # Números iniciales
        salida += f"x_{i+1} = {semillas[i]}\n"
    for i in range(N_NUMEROS):  # Números generados
        r_n = semillas[tam_original + i] / (m - 1)
        salida += f"x_{tam_original + i + 1} = ({semillas[i]} + {semillas[tam_original -1 + i]}) mod {m} = {semillas[tam_original + i]}\n"
        salida += f"r_{tam_original + i + 1} = {tam_original + i} / {m - 1} = {r_n:.4f}\n"
        salida += "\n"

    return salida
################################################
####### Algoritmo congruencial no lineal #######
################################################

def algoritmo_congruencial_cuadratico(x0: int, m: int, a: int, b: int, c: int):
    salida = ""

    if a == 1 and b == 0 and c == 0:
        # Algoritmo de Blum, Blum y Shub
        for i in range(N_NUMEROS):
            x_n = x0**2 % m
            r_n = x_n / (m - 1)
            salida += f"x_{i+1} = {x0}^2 mod {m} = {x_n}\n"
            salida += f"r_{i+1} = {x_n} / ({m} - 1) = {r_n:.4f}\n"
            salida += "\n"
            x0 = x_n
    else:
        for i in range(N_NUMEROS):
            x_n = (a * x0**2 + b * x0 + c) % m
            r_n = x_n / (m - 1)
            salida += f"x_{i+1} = ({a} * {x0}^2 + {b} * {x0} + {c}) mod {m} = {x_n}\n"
            salida += f"r_{i+1} = {x_n} / ({m} - 1) = {r_n:.4f}\n"
            salida += "\n"
            x0 = x_n

    return salida


# print(cuadrados_medios(1031))
# print(productos_medios(3079, 4931))
# print(multiplicador_constante(4013, 1487))

# print(algoritmo_congruencial_lineal(83, 5, 7, 9))  # 6, 3, 3, 7 -
# print(algoritmo_congruencial_multiplicativo(137, 5, 5, "a = 3 + 8 * k"))
# print(algoritmo_congruencial_aditivo())
# print(algoritmo_congruencial_cuadratico(13, 8, 26, 27, 27))
# print(algoritmo_congruencial_cuadratico(13, 32, 1, 0, 0))