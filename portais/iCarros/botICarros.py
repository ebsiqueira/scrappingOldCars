import requests
from bs4 import BeautifulSoup
import json
from portais.iCarros import processadorICarros

# Função de raspagem de carros
def coletarCarros(pagina, userAgent):
    # URL para coleta de carros
    url = "https://www.icarros.com.br/ache/listaanuncios.jsp?pag="+str(pagina)+"&ord=35&sop=nta_17|44|51.1_-amf_1980.1_-kmm_1.1_-rai_50.1_-esc_4.1_-sta_1.1_"  

    # Cria sessão
    sessao = requests.Session()
    b = sessao.get(url, headers=userAgent)
    
    # Monta a "sopa"
    soup = BeautifulSoup(b.content, 'html.parser')
 
    # Obtém a tag script com os carros raspados
    scriptTagCarros = soup.find_all('script', {"type":"text/javascript"})
    
    # Chama processador para coletar somente os carros
    carros = processadorICarros.processaCarrosICarros(scriptTagCarros)
    
    # Transforma os carros raspados para o formato JSON
    carrosJson = json.loads(carros)
    
    # Retorna carros coletados
    return carrosJson

def exec(pagina, userAgent):
    resultadoRaspagem = list()

    carros = coletarCarros(pagina, userAgent)

    for carro in carros["items"]:
        objetoCarro = processadorICarros.processaInfoCarroICarros(carro)
        resultadoRaspagem.append(objetoCarro)
    
    print("Pagina lida botICarros: {}".format(pagina))
    
    return resultadoRaspagem
            
            
        