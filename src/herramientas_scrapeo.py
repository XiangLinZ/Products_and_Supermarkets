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




def scrap_subcat(numero_cate, n):
    today = date.today()
    url = f"https://tienda.mercadona.es/categories/{numero_cate}"
    driver.get(url)
    sleep(1)
    driver.find_element("css selector", '#root > div.cookie-banner > div > div > button.ui-button.ui-button--small.ui-button--primary.ui-button--positive').click()
    sleep(2)
    driver.find_element("css selector", "#root > div.ui-focus-trap > div > div:nth-child(2) > div > form > div > input").click()
    driver.find_element("css selector", "#root > div.ui-focus-trap > div > div:nth-child(2) > div > form > div > input").send_keys("28018",Keys.ENTER)
    sleep(2)
    for n2 in range(2, n+1):
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
                    productos_mercadona["insert_date"].append(today)
                    driver.implicitly_wait(5)
                    driver.find_element("css selector", '#root > div.ui-focus-trap > div > div:nth-child(2) > div > div.modal-content__header > button').click()
                except:
                    break
        except:
            break

