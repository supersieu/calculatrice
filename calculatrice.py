def cal_1_input(char):
    list_char = [["I", 1], ["V", 5], ["X", 10], ["L", 50], ["C", 100], ["D", 500], ["M", 1000]]
    val = 0
    for i in range(len(list_char)):
        if list_char[i][0] == char:
            val = list_char[i][1]
    return val


def cal_2_input_ide(char):
    return cal_1_input(char[0]) * 2


def cal_n_input_ide(char):
    return cal_1_input(char[0]) * len(char)


def cal_n_input(char):
    somme = 0
    for i in range(len(char)):
        somme = somme + cal_1_input(char[i])
    return somme


def cal_n_input_sous(char):
    somme = 0
    for i in range(len(char)-1):
        if cal_1_input(char[i]) < cal_1_input(char[i+1]):
            retenu = -cal_1_input(char[i])
        else:
            retenu = cal_1_input(char[i])

        somme = somme + retenu
    somme = somme + cal_1_input(char[-1])
    return somme


def operation (op,nombre_1,nombre_2):
    resultat = 0
    if op == "+":
        resultat = plus(nombre_1, nombre_2)
    elif op == "-":
        resultat = moins(nombre_1, nombre_2)
    elif op == "*":
        resultat = mul(nombre_1, nombre_2)
    elif op == "/":
        resultat = div(nombre_1, nombre_2)
    else:
        print("Invalide operation")
    return resultat


def div(nombre_1, nombre_2):
    resultat = cal_n_input_sous(nombre_1) / cal_n_input_sous(nombre_2)
    return resultat


def mul(nombre_1, nombre_2):
    resultat = cal_n_input_sous(nombre_1) * cal_n_input_sous(nombre_2)
    return resultat


def moins(nombre_1, nombre_2):
    resultat = cal_n_input_sous(nombre_1) - cal_n_input_sous(nombre_2)
    return resultat


def plus(nombre_1, nombre_2):
    resultat = cal_n_input_sous(nombre_1) + cal_n_input_sous(nombre_2)
    return resultat


def convertir_1_c(nombre_decimal):
    list_char = [["I", 1], ["V", 5], ["X", 10], ["L", 50], ["C", 100], ["D", 500], ["M", 1000]]
    char=""
    for i in range(len(list_char)):
        if list_char[i][1] == nombre_decimal:
            char = list_char[i][0]
    return char



def convertir(nombre_dec):
    list = [["I", 1],["II", 2], ["III", 3], ["IV", 4], ["V", 5], ["VI", 6], ["VII",7], ["VIII", 8],["IX",9],["X",10]]
    coef = 0
    l = ""
    while nombre_dec != 0:
        dernier = nombre_dec % 10
        nombre_dec=nombre_dec//10
        if dernier!=0:
            char = list[dernier-1][0]
            longueur = len(char)
            for i in reversed(range(longueur)):
                val = cal_1_input(char[i])
                val = val * 10**coef
                l = convertir_1_c(val) + l
        coef = coef+1
    return l