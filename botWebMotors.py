import requests
from bs4 import BeautifulSoup
import resultParser
import json
from random import randint
import time

# Disable console warning
requests.packages.urllib3.disable_warnings()

user_agent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0"}

def get_cars():    
    try:
        result = []
        for page in range(1,2):
            url = "https://www.webmotors.com.br/api/search/car?url=https://www.webmotors.com.br/carros-usados%2Festoque%2Fate.1980%3Ftipoveiculo%3Dcarros-usados%26anoate%3D1980&actualPage="+str(page)+"&displayPerPage=24&order=1&showMenu=true&showCount=true&showBreadCrumb=true&testAB=false&returnUrl=false"
        
            # Build session
            session = requests.Session()
            b = session.get(url, headers=user_agent)
            
            json_result = b.json()
        
            for carros in json_result["SearchResults"]:
                objeto = {
                    "Portal":"WebMotors",
                    "ID":carros["UniqueId"],
                    "Preco":carros["Prices"]["Price"],
                    #"Descrição":carros["LongComment"],
                    "Caracteristicas":carros["Specification"]
                }
                
                result.append(objeto)
            
            print("Pagina lida: {}".format(page))
            
            time.sleep(float(randint(60,120)))
            
            
        json_str = json.dumps(result, indent=4)
        
        f = open("resultado.txt", "a")
        f.write(json_str)
        f.close()

    except Exception as e:
      print(f"An error occurred: {str(e)}")

def get_specs_from_cars():
    pass

def main():
    # chama get_cars x vezes pra x paginas
    # em cada pagina, entrar na url de cada anuncio e pegar as infos de cada carro
    # chamar as funcoes do result parser
    pass

get_cars()