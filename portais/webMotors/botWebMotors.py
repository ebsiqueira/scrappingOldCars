import requests
import json
from random import randint
import time
import processadorWebMotors

# Disable console warning
requests.packages.urllib3.disable_warnings()

userAgent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0"}

urlAtual = ""

def coletarCarros(pagina):
    # URL para coleta dos carros
    url = "https://www.webmotors.com.br/api/search/car?url=https://www.webmotors.com.br/carros-usados%2Festoque%2Fate.1980%3Ftipoveiculo%3Dcarros-usados%26anoate%3D1980&actualPage="+str(pagina)+"&displayPerPage=24&order=1&showMenu=true&showCount=true&showBreadCrumb=true&testAB=false&returnUrl=false"  

    # Mantém a URL atualizada, visto que a API não force a URL
    global urlAtual 
    urlAtual = url

    # Cria sessão
    sessao = requests.Session()
    requisicao = sessao.get(url, headers=userAgent)
    
    # Pega o JSON da resposta da requisição
    resultadoJson = requisicao.json()
    
    # Coleta somente os carros da resposta
    carros = resultadoJson["SearchResults"]
    
    # Retorna carros
    return carros

def main():
    # Tenta processar o portal WebMotors

    try:
        resultadoRaspagem = []
        
        for pagina in range(1,2):
            carros = coletarCarros(pagina)
        
            for carro in carros:
                objetoCarro = processadorWebMotors.processaInfoCarrosWebMotors(carro, urlAtual)
                resultadoRaspagem.append(objetoCarro)    
            
            print("Pagina lida WebMotors: {}".format(pagina))
            
            #time.sleep(float(randint(60,120)))
            
        bytesJson = json.dumps(resultadoRaspagem, indent=4, ensure_ascii=False).encode('utf8')
        
        f = open("resultadoWebMotors.txt", "w")
        f.write(bytesJson.decode())
        f.close()

    except Exception as e:
      print(f"An error occurred: {str(e)}")

main()