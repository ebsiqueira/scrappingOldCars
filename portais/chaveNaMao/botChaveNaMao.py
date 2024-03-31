import requests
from bs4 import BeautifulSoup
from portais.chaveNaMao import processadorChaveNaMao

# Função de raspagem de carros
def coletarCarros(pagina, userAgent):    
    # URL para coleta de carros
    url = "https://www.chavesnamao.com.br/carros-usados/brasil/?&filtro={%22amax%22:1980}&pg="+str(pagina)+""  

    # Cria sessão
    sessao = requests.Session()
    b = sessao.get(url, headers=userAgent)
    
    # Monta a "sopa"
    soup = BeautifulSoup(b.content, 'html.parser')
    # Obtém a div com os carros raspados
    divCarros = soup.find_all('div', class_="veiculos__Card-sc-3pfc6p-0 igtaVV")

    # Chama processador para coletar somente os carros
    carrosJson = processadorChaveNaMao.processaCarrosChaveNaMao(divCarros)
    # Retorna carros coletados
    return carrosJson

# Main
def exec(pagina, userAgent):
    resultadoRaspagem = list()

    carros = coletarCarros(pagina, userAgent)
    
    for carro in carros:
        objetoCarro = processadorChaveNaMao.processaInfoCarrosChaveNaMao(carro)
        resultadoRaspagem.append(objetoCarro)
    
    print("Pagina lida botChaveNaMao: {}".format(pagina))
    
    return resultadoRaspagem