import requests
from bs4 import BeautifulSoup
import json
from random import randint
import time

# Disable console warning
requests.packages.urllib3.disable_warnings()

userAgent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0"}

def coletarCarros(pagina):    
    url = "https://www.chavesnamao.com.br/carros-usados/brasil/?&filtro={%22amax%22:1980}&pg="+pagina+""  

    sessao = requests.Session()
    b = sessao.get(url, headers=userAgent)
    
    resultadoJson = b.json()
    
    carros = resultadoJson["SearchResults"]
    
    return carros

def coletarInformacoesDosCarros(carro):
    especificacaoFormatada = tratamentoEspecificacao(carro["Specification"])
    localizacaoFormatada = tratamentoLocalizacao(carro["Seller"]["Localization"][0])
    
    objetoCarro = {
        "Portal": "WebMotors",
        "Caracteristicas": especificacaoFormatada,
        "Localizacao": localizacaoFormatada,
        "Preco": carro["Prices"]["Price"]
    }
    
    return objetoCarro
    
def tratamentoEspecificacao(especificacao):
    dadosEspecificacao = {
        "Fabricante":especificacao["Make"]["Value"],
        "Modelo":especificacao["Model"]["Value"],
        "Versao":especificacao["Version"]["Value"],
        "Ano":especificacao["YearModel"],
        "Quilometragem":especificacao["Odometer"],
        "Cambio":especificacao["Transmission"],
        "Portas":especificacao["NumberPorts"],
        "Cor":especificacao["Color"]["Primary"]
    }

    return dadosEspecificacao

def tratamentoLocalizacao(localizacao):
    dadosLocalizacao = {
        "Logradouro":localizacao["AbbrState"],
        "CEP":localizacao["ZipCode"],
        "Bairro":localizacao["Neighborhood"],
        "Cidade":localizacao["City"],
        "Estado":localizacao["State"],
        "Pais":localizacao["Country"],
    }
    
    return dadosLocalizacao

def main():
    try:
        resultadoRaspagem = []
        
        for pagina in range(1,2):
            carros = coletarCarros(pagina)
        
            for carro in carros:
                objetoCarro = coletarInformacoesDosCarros(carro)
                resultadoRaspagem.append(objetoCarro)    
            
            print("Pagina lida WebMotors: {}".format(pagina))
            
            time.sleep(float(randint(60,120)))
            
        bytesJson = json.dumps(resultadoRaspagem, indent=4, ensure_ascii=False).encode('utf8')
        
        f = open("resultadoWebMotors.txt", "a")
        f.write(bytesJson.decode())
        f.close()

    except Exception as e:
      print(f"An error occurred: {str(e)}")

main()