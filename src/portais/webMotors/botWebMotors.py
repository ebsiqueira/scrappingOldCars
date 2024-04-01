import requests
from portais.webMotors import processadorWebMotors

# Variável global para salvar a url que está sendo trabalhada
urlAtual = ""

# Função de raspagem de carros
def coletarCarros(pagina, userAgent):
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
    
    # Retorna carros coletados
    return carros

# Executa o robô
def exec(pagina, userAgent):
    resultadoRaspagem = list()

    # Coleta os carros
    carros = coletarCarros(pagina, userAgent)

    # Processa cada carro individualmente
    for carro in carros:
        objetoCarro = processadorWebMotors.processaInfoCarrosWebMotors(carro, urlAtual)
        resultadoRaspagem.append(objetoCarro)
    
    print("Pagina lida botWebMotors: {}".format(pagina))
    
    # Retorna resultado com carros já estruturados
    return resultadoRaspagem