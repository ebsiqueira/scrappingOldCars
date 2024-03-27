import requests
from bs4 import BeautifulSoup
import json
from random import randint
import time

# Disable console warning
requests.packages.urllib3.disable_warnings()

userAgent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0"}

def coletarCarros(pagina):    
    url = "https://www.chavesnamao.com.br/carros-usados/brasil/?&filtro={%22amax%22:1980}&pg="+str(pagina)+""  

    sessao = requests.Session()
    b = sessao.get(url, headers=userAgent)
    
    soup = BeautifulSoup(b.content, 'html.parser')
  
    div = soup.find_all('div', class_="veiculos__Card-sc-3pfc6p-0 igtaVV")

    jsonCarros = list()
    
    for scripts in div:
        jsonCarros.append(scripts.find('script'))
    
    carrosJson = list()
        
    for carrosTexto in jsonCarros:
        temp = json.loads(carrosTexto.text)
        carrosJson.append(temp)

    return carrosJson

def coletarInformacoesDosCarros(carro):
    especificacaoFormatada = tratamentoEspecificacao(carro["object"])
    
    objetoCarro = {
        "Portal": "ChaveNaMão",
        "Caracteristicas": especificacaoFormatada,
        "Preco": carro["object"]["offers"]["price"],
        "URL": carro["object"]["offers"]["url"]
    }
    
    return objetoCarro
    
def tratamentoEspecificacao(especificacao):
    dadosEspecificacao = {
        "Fabricante":especificacao["brand"]["name"],
        "Modelo":especificacao["model"],
        "Ano":especificacao["vehicleModelDate"],
        "Quilometragem":especificacao["mileageFromOdometer"]["value"],
        "Transmissão":especificacao["vehicleTransmission"],
        "Cor":especificacao["color"]
    }

    return dadosEspecificacao

def main():
    try:
        resultadoRaspagem = []
        
        for pagina in range(1,2):
            carros = coletarCarros(pagina)
        
            for carro in carros:
                objetoCarro = coletarInformacoesDosCarros(carro)
                resultadoRaspagem.append(objetoCarro)    
            
            print("Pagina lida ChaveNaMão: {}".format(pagina))
            
            #time.sleep(float(randint(60,120)))
            
        bytesJson = json.dumps(resultadoRaspagem, indent=4, ensure_ascii=False).encode('utf8')
        
        f = open("resultadoChaveNaMao.txt", "w")
        f.write(bytesJson.decode())
        f.close()

    except Exception as e:
        print(f"An error occurred: {str(e)}")

main()