import requests
from bs4 import BeautifulSoup
import json
from random import randint
import time

# Disable console warning
requests.packages.urllib3.disable_warnings()

userAgent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0"}

def coletarCarros(pagina):    
    url = "https://www.icarros.com.br/ache/listaanuncios.jsp?pag="+str(pagina)+"&ord=35&sop=nta_17|44|51.1_-amf_1980.1_-kmm_1.1_-rai_50.1_-esc_4.1_-sta_1.1_"  

    sessao = requests.Session()
    b = sessao.get(url, headers=userAgent)
    
    soup = BeautifulSoup(b.content, 'html.parser')
 
    div = soup.find_all('script')
    
    print(div)
    return None

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
        "URL": carro["object"]["offers"]["url"],
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
            
            print("Pagina lida ChaveNaMão: {}".format(pagina))
            
            time.sleep(float(randint(60,120)))
            
        bytesJson = json.dumps(resultadoRaspagem, indent=4, ensure_ascii=False).encode('utf8')
        
        f = open("resultadoChaveNaMao.txt", "a")
        f.write(bytesJson.decode())
        f.close()

    except Exception as e:
        print(f"An error occurred: {str(e)}")

coletarCarros(1)