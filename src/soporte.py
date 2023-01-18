import sys
sys.path.append("../")
import src.biblioteca as bb
import numpy as np
from fuzzywuzzy import process, fuzz
sys.path.append("../")
import src.soporte as sp

def dia_subcat2(categoria):
    frag = categoria.split("_")
    return frag[0]

def dia_subcat(categoria):
    """Depurador de subcategorias DIA

    Args:
        categoria (string): Categorias en strings

    Returns:
        string: Subcategoria
    """
    frag = categoria.split("_")
    dic_dia = {
    "congelados": bb.dia_con, "bebe": bb.dia_be, "frescos": bb.dia_fre, "al": bb.dia_fre, "perfumeria": bb.dia_per, 
    "lacteos": bb.dia_lac, "desayuno": bb.dia_des, "drogueria": bb.dia_dro, "charcuteria" : bb.dia_charc, 
    "dulces": bb.dia_des, "alimentacion": bb.dia_alim, "bodega": bb.dia_bode}
    
    if frag[0] in dic_dia:
        for k, v in dic_dia[frag[0]].items():
            if frag[-1] in v:
                return k
    elif frag[0] == "despensa":
        if frag[1] in bb.listadia1:
            return frag[1]
        elif frag[-2] == "bebidas":
            return "leche"
        elif frag[-1] in bb.listadia2:
            return bb.dia_cuid[frag[-1]]
        else:
            return frag[-1]
    elif frag[0] == "cuidado":
        if frag[-1] in bb.dia_cuid:
            return bb.dia_cuid[frag[-1]]
        else:
            return frag[-1]
    elif frag[0] == "bebidas":
        if frag[1] == "vinos":
            return ("_".join([frag[1], frag[2]]))
        else:
            for k, v in bb.dia_bebis.items():
                if frag[-1] in v:
                    return k
    elif frag[0] == "mascotas":
        if frag[1] in ["perros", "gatos"]:
            return frag[1] 
        elif frag[1] in ["resto", "roedores", "otros", "otro"]:
            return "otros"
        elif frag[1] == "accesorios":
            return frag[1]
    elif frag[0] in ["pizza", "platos"]:
        return "precocinados"
    elif frag[0] == "productos":
        return "pan"
    else: 
        "desconocido"
        
def mer_subcat(categoria):
    """Depurador de categorias MERCADONA

    Args:
        categoria (string): Categoria en string

    Returns:
        string: Subcategoria
    """
    frag = categoria.split("_")
    dic_merc1 = {"congelados": bb.mer_con, "charcuteria": bb.mer_charc}
    dic_merc2 = {"cuidado": bb.mer_cui, "huevos": bb.mer_hue, "azucar": bb.mer_azuc, "bodega": bb.mer_bod, "fruta": bb.mer_frut,
                 "limpieza": bb.mer_lim, "cereales": bb.mer_cer, "arroz": bb.mer_arr, "bebe": bb.mer_bebe, "conservas": bb.mer_cons,
                 "mascotas": bb.mer_masc, "carne": bb.mer_car, "marisco": bb.mer_mari, "aceite": bb.mer_acei, "agua": bb.mer_agua,
                 "cacao": bb.mer_cac, "postres": bb.mer_post}
    if frag[0] in bb.mer_cuid:
        return bb.mer_cuid[frag[0]]
    elif frag[0] in ["congelados", "charcuteria"]:
        for k, v in dic_merc1[frag[0]].items():
            if frag[-1] in v:
                return k
    elif frag[0] == "panaderia":
        if frag[-1] == "horno":
            return frag[-3]
        else:
            for k, v in bb.mer_pan.items():
                if frag[-1] in v:
                    return k
    else:
        for k, v in dic_merc2[frag[0]].items():
            if frag[-1] in v:
                return k

def category(categoria):
    """Generador de categorias a partir de subcategorias

    Args:
        categoria (string): Subcategorias ya limpias

    Returns:
        string: Categoria mayor que engloba las subcategorias
    """
    for k, v in bb.diccategoria.items():
        if categoria in v:
            return k

def sleep_(n1 = 4, n2 = 8, n3 = 2):
    """Generador de números aleatorios, adecuados para sleeps para scrapear

    Args:
        n1 (int, optional): el número mínimo que puede devolver. Defaults to 4.
        n2 (int, optional): el número máximo que puede devolver. Defaults to 8.
        n3 (int, optional): el número de decimales que devuelve. Defaults to 2.

    Returns:
        int: int aleatorio entre el primer número y el segundo con el tercer número de decimales
    """
    return round(np.random.randint(n1,n2) + np.random.rand(1)[0], n3)

def limpiar_reference(col1, col2):

    if col2 == "docena":
        return (col1 / 12)
    if col2 == "100ml":
        return (col1 * 10)
    if col2 == "100g":
        return (col1 * 10)
    if col2 == "g":
        return (col1 * 100)
    else:
        return col1

def limpiar_runit(col2):

    if col2 == "docena":
        return "ud"
    if col2 == "100ml":
        return "l"
    if col2 in ["100g", "g"]:
        return "kg"
    else:
        return col2

def refinar_aceite(col1):

    generos_posibles = ["aceites", "sal", "vinagre", "aliños"]
    ratio_mayor = 0
    for posibilidad in generos_posibles:
        ratio = fuzz.ratio(col1, generos_posibles)
        if ratio > ratio_mayor:
            ratio_mayor = ratio
            subgenero = posibilidad
        else:
            pass
    if subgenero == "aliños":
        return "vinagre"
    elif subgenero == "sal":
        return "especias"
    else: 
        return subgenero


def semejanza(lista1, lista2):
    lista = []
    for (a,b) in zip(lista1, lista2):
        porcentaje = fuzz.ratio(a,b)
        if porcentaje > 45:
            lista.append(True)
        else:
            lista.append(False)
    return lista