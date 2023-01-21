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
import warnings
warnings.filterwarnings('ignore')
import requests
import re
from bs4 import BeautifulSoup
import sys
sys.path.append("../")
import src.biblioteca as bb
sys.path.append("../")
import src.herramientas_scrapeo as hs
sys.path.append("../")
import src.soporte as sp




def merc_subcat(numero_cate, diccionario, lista_errores):
    """ Scrap of one category from Mercadona

    Args:
        numero_cate (int): number ob the category that you want to scrap
        diccionario (dic): dicctionary with the structure of the future dataframe
        lista_errores (set): a set where where errors are added
    """
    driver = webdriver.Chrome("../src/chromedriver.exe")
    today = date.today()
    url = f"https://tienda.mercadona.es/categories/{numero_cate}"
    driver.get(url)
    try:
        driver.implicitly_wait(5)
        driver.find_element("css selector", '#root > div.cookie-banner > div > div > button.ui-button.ui-button--small.ui-button--primary.ui-button--positive').click()
        sleep(5)
        driver.find_element("css selector", "#root > div.ui-focus-trap > div > div:nth-child(2) > div > form > div > input").click()
        driver.find_element("css selector", "#root > div.ui-focus-trap > div > div:nth-child(2) > div > form > div > input").send_keys("28018",Keys.ENTER)
    except:
        driver.implicitly_wait(5)
        driver.find_element("css selector", "#modal-info > div > div > div > button").click()
        lista_errores.add(numero_cate)
    sleep(2)
    for n2 in range(2, 10):
        try:
            for n in range(1, 50):
                rutaselector = f"#root > div.grid-layout > div.grid-layout__main-container > div.grid-layout__content > div > div > section:nth-child({n2}) > div > div:nth-child({n}) > button"
                try:
                    sleep(2)
                    driver.implicitly_wait(3)
                    driver.find_element("css selector", rutaselector).click()
                    driver.implicitly_wait(3)
                    diccionario["name"].append(driver.find_element("css selector", "#root > div.ui-focus-trap > div > div:nth-child(2) > div > div.private-product-detail > div.private-product-detail__content > div.private-product-detail__right > h1").text)
                    try:
                        diccionario["category"].append((driver.find_element("css selector", "#root > div.ui-focus-trap > div > div:nth-child(2) > div > div.private-product-detail > div.private-product-detail__breadcrumb").text).replace(" >","").replace(" ", "_"))
                    except:
                        diccionario["category"].append(np.nan)
                        lista_errores.add(numero_cate)
                        sleep(60)
                    try:    
                        precio_chungo = driver.find_element("css selector", "#root > div.ui-focus-trap > div > div:nth-child(2) > div > div.private-product-detail > div.private-product-detail__content > div.private-product-detail__right > div.product-price").text
                        diccionario["price"].append(float(precio_chungo.split(" €")[0].replace(",",".")))
                    except:
                        diccionario["price"].append(np.nan)
                    try:    
                        diccionario["reference_price"].append(float((driver.find_element("css selector", "#root > div.ui-focus-trap > div > div:nth-child(2) > div > div.private-product-detail > div.private-product-detail__content > div.private-product-detail__right > div.product-format.product-format__size").text).split("| ")[1].split(" €")[0]).replace(",","."))
                    except:
                        diccionario["reference_price"].append(np.nan)
                    try:    
                        diccionario["reference_unit"].append((driver.find_element("css selector", "#root > div.ui-focus-trap > div > div:nth-child(2) > div > div.private-product-detail > div.private-product-detail__content > div.private-product-detail__right > div.product-format.product-format__size").text).split("/")[1])
                    except:
                        diccionario["reference_unit"].append(np.nan)
                    diccionario["category_id"].append(numero_cate)
                    diccionario["insert_date"].append(today)
                    sleep(2)
                    driver.implicitly_wait(5)
                    driver.find_element("css selector", '#root > div.ui-focus-trap > div > div:nth-child(2) > div > div.modal-content__header > button').click()
                except:
                    try:
                        driver.implicitly_wait(5)
                        driver.find_element("css selector", "#modal-info > div > div > div > button").click()
                        lista_errores.append(numero_cate)
                        sleep(60)
                        break
                    except:
                        break
        except:
            try:
                driver.implicitly_wait(5)
                driver.find_element("css selector", "#modal-info > div > div > div > button").click()
                lista_errores.append(numero_cate)
                break
            except:
                break

def scrap_mercadona(lista_recorrer, dic, lista_errores):
    """Scraps every category in Mercadona

    Args:
        lista_recorrer (list): list of categories that you want to scrap
        dic (dic): diccionary with the structure of the future dataframe
        lista_errores (set): set where errors are added
    """
    for categ in lista_recorrer:
        hs.merc_subcat(categ, dic, lista_errores)
        sleep(10)
  

def scrap_dia():
    """Scraps every product from the supermarket Dia

    Returns:
        dic: dictionary with a structure to make a dataframe
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
                        productos_dia["category"].append(producto.find("a").get("href").split("/compra-online/")[1].split("/p/")[0].replace("/", "-").replace("-","_"))
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