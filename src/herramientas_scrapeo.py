import pandas as pd
import numpy as np
import re
from selenium import webdriver
from time import sleep
from datetime import date
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from fuzzywuzzy import process, fuzz
import pickle
import warnings
warnings.filterwarnings('ignore')
import requests
import re
from bs4 import BeautifulSoup
import sys
sys.path.append("../")
import src.biblioteca as bb
import numpy as np
import sys
sys.path.append("../")
import src.herramientas_scrapeo as hs
import sys
sys.path.append("../")
import src.soporte as sp




def merc_subcat(numero_cate, diccionario):
    """scrapeo de una sola categoria de mercadona de hoy

    Args:
        numero_cate (int): el número asociado a la categoria que se quiere scrapear
        diccionario (dic): diccionario donde se apendearán los datos scrapeados, son 6 keys necesarias
    """
    driver = webdriver.Chrome("../src/chromedriver.exe")
    today = date.today()
    url = f"https://tienda.mercadona.es/categories/{numero_cate}"
    driver.get(url)
    sleep(1)
    try:
        driver.find_element("css selector", '#root > div.cookie-banner > div > div > button.ui-button.ui-button--small.ui-button--primary.ui-button--positive').click()
        sleep(2)
        driver.find_element("css selector", "#root > div.ui-focus-trap > div > div:nth-child(2) > div > form > div > input").click()
        driver.find_element("css selector", "#root > div.ui-focus-trap > div > div:nth-child(2) > div > form > div > input").send_keys("28018",Keys.ENTER)
        sleep(2)
    except:
        driver.implicitly_wait(5)
        driver.find_elemeny("css selector", "#modal-info > div > div > div > button").click()
        sleep(2)
        driver.find_element("css selector", '#root > div.cookie-banner > div > div > button.ui-button.ui-button--small.ui-button--primary.ui-button--positive').click()
        sleep(2)
        driver.find_element("css selector", "#root > div.ui-focus-trap > div > div:nth-child(2) > div > form > div > input").click()
        driver.find_element("css selector", "#root > div.ui-focus-trap > div > div:nth-child(2) > div > form > div > input").send_keys("28018",Keys.ENTER)
        sleep(2)
    for n2 in range(2, 10):
        try:
            for n in range(1, 50):
                rutaselector = f"#root > div.grid-layout > div.grid-layout__main-container > div.grid-layout__content > div > div > section:nth-child({n2}) > div > div:nth-child({n}) > button"
                try:
                    driver.implicitly_wait(3)
                    driver.find_element("css selector", rutaselector).click()
                    driver.implicitly_wait(3)
                    diccionario["name"].append(driver.find_element("css selector", "#root > div.ui-focus-trap > div > div:nth-child(2) > div > div.private-product-detail > div.private-product-detail__content > div.private-product-detail__right > h1").text)
                    diccionario["category"].append((driver.find_element("css selector", "#root > div.ui-focus-trap > div > div:nth-child(2) > div > div.private-product-detail > div.private-product-detail__breadcrumb").text).replace(" >","").replace(" ", "_"))
                    precio_chungo = driver.find_element("css selector", "#root > div.ui-focus-trap > div > div:nth-child(2) > div > div.private-product-detail > div.private-product-detail__content > div.private-product-detail__right > div.product-price").text
                    diccionario["price"].append(precio_chungo.split(" €")[0])
                    diccionario["reference_price"].append((driver.find_element("css selector", "#root > div.ui-focus-trap > div > div:nth-child(2) > div > div.private-product-detail > div.private-product-detail__content > div.private-product-detail__right > div.product-format.product-format__size").text).split("| ")[1].split(" €")[0])
                    diccionario["reference_unit"].append((driver.find_element("css selector", "#root > div.ui-focus-trap > div > div:nth-child(2) > div > div.private-product-detail > div.private-product-detail__content > div.private-product-detail__right > div.product-format.product-format__size").text).split("/")[1])
                    diccionario["insert_date"].append(today)
                    driver.implicitly_wait(5)
                    driver.find_element("css selector", '#root > div.ui-focus-trap > div > div:nth-child(2) > div > div.modal-content__header > button').click()
                except:
                    try:
                        driver.implicitly_wait(5)
                        driver.find_elemeny("css selector", "#modal-info > div > div > div > button").click()
                        driver.implicitly_wait(3)
                        driver.find_element("css selector", rutaselector).click()
                        driver.implicitly_wait(3)
                        diccionario["name"].append(driver.find_element("css selector", "#root > div.ui-focus-trap > div > div:nth-child(2) > div > div.private-product-detail > div.private-product-detail__content > div.private-product-detail__right > h1").text)
                        diccionario["category"].append((driver.find_element("css selector", "#root > div.ui-focus-trap > div > div:nth-child(2) > div > div.private-product-detail > div.private-product-detail__breadcrumb").text).replace(" >","").replace(" ", "_"))
                        precio_chungo = driver.find_element("css selector", "#root > div.ui-focus-trap > div > div:nth-child(2) > div > div.private-product-detail > div.private-product-detail__content > div.private-product-detail__right > div.product-price").text
                        diccionario["price"].append(precio_chungo.split(" €")[0])
                        diccionario["reference_price"].append((driver.find_element("css selector", "#root > div.ui-focus-trap > div > div:nth-child(2) > div > div.private-product-detail > div.private-product-detail__content > div.private-product-detail__right > div.product-format.product-format__size").text).split("| ")[1].split(" €")[0])
                        diccionario["reference_unit"].append((driver.find_element("css selector", "#root > div.ui-focus-trap > div > div:nth-child(2) > div > div.private-product-detail > div.private-product-detail__content > div.private-product-detail__right > div.product-format.product-format__size").text).split("/")[1])
                        diccionario["insert_date"].append(today)
                        driver.implicitly_wait(5)
                        driver.find_element("css selector", '#root > div.ui-focus-trap > div > div:nth-child(2) > div > div.modal-content__header > button').click()
                    except:
                        break
        except:
            break

def scrap_mercadona():
    """Scrapea todos los productos de mercadona de hoy

    Returns:
        dic: diccionario con estructura ideal para pasar a df
    """
    productos_mercadona = {"name": [], "category": [], "price": [], "reference_price": [], "reference_unit": [], "insert_date": []}
    for categ in bb.listacategorias_merc:
        hs.merc_subcat(categ, productos_mercadona)
    return productos_mercadona

def scrap_dia():
    """Función que scrapea todos los productos del Dia de hoy

    Returns:
        dic: Un diccionario con los nombres, categorias, precios y demás datos que los da en formato ideal para pasar a df
    """
    productos_dia = {
        "name": [],
        "category": [],
        "price": [],
        "reference_price": [],
        "reference_unit": [],
        "insert_date": []}
    today = date.today()
    for cate in bb.categoria_n_dia:
        for n in range(150):
            if n == 0:
                url = f"https://www.dia.es/compra-online/{cate}/cf"
            else: 
                url = f"https://www.dia.es/compra-online/{cate}/cf?page={n}"
            try:
                res = requests.get(url)
                sopa = BeautifulSoup(res.content, 'html.parser') 
                productos_dia_sopa = sopa.find_all("div", {"class": "product-list__item"})
                for producto in productos_dia_sopa:
                    try:
                        productos_dia["name"].append(producto.find("a").get("title"))
                    except:
                        productos_dia["name"].append(np.nan)
                    try:
                        productos_dia["category"].append(producto.find("a").get("href").split("/compra-online/")[1].split("/p")[0].replace("/", "-").replace("-","_"))
                    except:
                        productos_dia["category"].append(np.nan)
                    try:
                        productos_dia["price"].append(float(producto.find_all("p")[0].text.split()[0].replace(",",".")))
                    except:
                        productos_dia["price"].append(np.nan)
                    try:   
                        productos_dia["reference_price"].append(float(producto.find_all("p")[1].text.split()[0].replace(",",".")))
                    except:
                        productos_dia["reference_price"].append(np.nan)
                    try:
                        productos_dia["reference_unit"].append(producto.find_all("p")[1].text.split()[1].split("/")[1].rstrip("."))
                    except:
                        productos_dia["reference_unit"].append(np.nan)
                    productos_dia["insert_date"].append(today)
            except:
                pass
    return productos_dia


# Prueba por categorias que ha fallado T_T
"""
def scrap_cat():

    for catego in listacategorias.keys():
        url = f"https://tienda.mercadona.es/categories/{catego}"
        driver.get(url)
        for minicat in range(listacategorias[catego]):
            scrap_subcat()
            if minicat == (listacategorias[catego] - 1):
                print("categoria scrapeada al completo")
            else:
                driver.implicitly_wait(4)
                driver.find_element("css selector", "#root > div.grid-layout > div.grid-layout__main-container > div.grid-layout__content > div > div > button").click()
"""

### Prueba 4 hacerlo en clase , no funciona la clase =D
"""
class Mercadona_scrap:

    def __init__(self) -> None:
        self.productos_mercadona = {
            "name": [],
            "category": [],
            "price": [],
            "reference_price": [],
            "reference_unit": [],
            "insert_date": []}
        self.today = date.today()
        self.listacategorias = {"112" : 4, "156" : 6, "135" : 3, "118": 3, "89" : 5, "216" : 4, "164" : 9, "86" : 5, "46" : 9, "78" : 3, "48" : 9, "147": 10, "122" : 6,
                                "201" : 5, "192" : 12, "213" : 2, "27" : 3, "77" : 3, "226" : 14, "206" : 5, "32" : 6, "222" : 3, "65" : 9, "138" : 3, "105" : 9, "99" : 4}

    def scrap_minicat(self):

        sleep(1)
        driver.find_element("css selector", '#root > div.cookie-banner > div > div > button.ui-button.ui-button--small.ui-button--primary.ui-button--positive').click()
        sleep(2)
        driver.find_element("css selector", "#root > div.ui-focus-trap > div > div:nth-child(2) > div > form > div > input").click()
        driver.find_element("css selector", "#root > div.ui-focus-trap > div > div:nth-child(2) > div > form > div > input").send_keys("28018",Keys.ENTER)
        sleep(2)
        for n2 in range(2, 10):
            try:
                for n in range(1, 50):
                    rutaselector = f"#root > div.grid-layout > div.grid-layout__main-container > div.grid-layout__content > div > div > section:nth-child({n2}) > div > div:nth-child({n}) > button"
                    try:
                        driver.implicitly_wait(3)
                        driver.find_element("css selector", rutaselector).click()
                        driver.implicitly_wait(3)
                        productos_mercadona["name"].append(driver.find_element("css selector", "#root > div.ui-focus-trap > div > div:nth-child(2) > div > div.private-product-detail > div.private-product-detail__content > div.private-product-detail__right > h1").text)
                        productos_mercadona["category"].append(driver.find_element("css selector", "#root > div.ui-focus-trap > div > div:nth-child(2) > div > div.private-product-detail > div.private-product-detail__breadcrumb").text)
                        precio_chungo = driver.find_element("css selector", "#root > div.ui-focus-trap > div > div:nth-child(2) > div > div.private-product-detail > div.private-product-detail__content > div.private-product-detail__right > div.product-price").text
                        productos_mercadona["price"].append(precio_chungo.split(" €/")[0])
                        productos_mercadona["reference_price"].append(driver.find_element("css selector", "#root > div.ui-focus-trap > div > div:nth-child(2) > div > div.private-product-detail > div.private-product-detail__content > div.private-product-detail__right > div.product-format.product-format__size").text)
                        productos_mercadona["reference_unit"].append(driver.find_element("css selector", "#root > div.ui-focus-trap > div > div:nth-child(2) > div > div.private-product-detail > div.private-product-detail__content > div.private-product-detail__right > div.product-format.product-format__size").text)
                        productos_mercadona["insert_date"].append(self.today)
                        driver.implicitly_wait(5)
                        driver.find_element("css selector", '#root > div.ui-focus-trap > div > div:nth-child(2) > div > div.modal-content__header > button').click()
                    except:
                        break
            except:
                break
    
    def scrap_subcat(self, categoria):

        for minicats in range(self.listacategorias[categoria]):
            opciones= Options()
            opciones.add_experimental_option('excludeSwitches', ['enable-automation'])#para ocultarme como robot
            opciones.add_experimental_option('useAutomationExtension', False)
            opciones.add_argument('--start-maximized') #empezar maximizado
            opciones.add_argument('user.data-dir=selenium') #guarda las cookies
            opciones.add_argument('--incognito')#incognito window
            driver = webdriver.Chrome("../src/chromedriver.exe")
            url = f"https://tienda.mercadona.es/categories/{categoria}"
            driver.get(url)
            self.scrap_minicat()
            if minicats == (self.listacategorias[categoria] - 1):
                print("categoria scrapeada al completo")
            else:
                driver.implicitly_wait(4)
                driver.find_element("css selector", "#root > div.grid-layout > div.grid-layout__main-container > div.grid-layout__content > div > div > button").click()

    def limpiar_diccionario(self):

        for atributo in self.productos_mercadona.keys():
            self.productos_mercadona[atributo] = []

    def scrap_todo(self):

        for cate in self.listacategorias.keys():
            self.scrap_subcat(cate)

    def guardar_csv(self):
        
        dfmerca = pd.DataFrame(self.productos_mercadona)
        dfmerca.to_csv(f"../data/merca_{today}.csv")

    def proceso_completo(self):

        self.scrap_todo()
        self.guardar_csv()
        self.limpiar_diccionario()
        print (f"Se han screapeado todos los datos de Mercadona del dia {today}, un saludo LOBO")
"""
