import requests
from bs4 import BeautifulSoup
import json
from random import randint
import time
import regex

# Disable console warning
requests.packages.urllib3.disable_warnings()

userAgent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0"}

def coletarCarros(pagina):    
    url = "https://www.icarros.com.br/ache/listaanuncios.jsp?pag="+str(pagina)+"&ord=35&sop=nta_17|44|51.1_-amf_1980.1_-kmm_1.1_-rai_50.1_-esc_4.1_-sta_1.1_"  

    sessao = requests.Session()
    b = sessao.get(url, headers=userAgent)
    
    soup = BeautifulSoup(b.content, 'html.parser')
 
    script = soup.find_all('script', {"type":"text/javascript"})
    
    anuncios = ""
    
    for resultado in script:
        if "const anuncios =" in str(resultado):
            anuncios = resultado
            
    stringAnuncios = str(anuncios)
    listAnuncios = stringAnuncios[82:-143]
    
    f = open("suporteICarros/resultadoScrapICarros.txt", "w")
    f.write(listAnuncios)
    f.close()
    
    with open( 
    "suporteICarros/resultadoScrapICarros.txt", 'r') as r, open( 
        'suporteICarros/output.txt', 'w') as o: 
        for line in r: 
            if line == "           ,\n":
                line = " "
            #strip() function 
            if line.strip():
                o.write(line)
             
    
    k = open("suporteICarros/output.txt", "r")
    oString = k.read()
    j = oString.replace("`", "\"")
    
    # Função para adicionar aspas duplas ao redor das ocorrências capturadas
    def adicionar_aspas(match):
        palavra = match.group()
        return "\"" + palavra + "\""

    # Aplicando a substituição
    texto_com_aspas = regex.sub(r'(?<=\{|\s{3})(\w+)(?=:)', adicionar_aspas, j)
    
    jsonFile = open("suporteICarros/output.json", "w")
    textoFinal = texto_com_aspas.replace(",\n    ]}", "\n    ]}")
    jsonFile.write(textoFinal)
    k.close()

    carrosJson = json.loads(textoFinal)
    
    return carrosJson

def coletarInformacoesDosCarros(carro):
    especificacaoFormatada = tratamentoEspecificacao(carro)
    localizacaoFormatada = tratamentoLocalizacao(carro)
    
    objetoCarro = {
        "Portal": "iCarros",
        "Caracteristicas": especificacaoFormatada,
        "Localizacao": localizacaoFormatada,
        "Preco": carro["price"],
        "URL": "https://www.icarros.com.br/" + carro["link"],
    }
    
    return objetoCarro
    
def tratamentoEspecificacao(especificacao):
    dadosEspecificacao = {
        "Fabricante":especificacao["item_brand"],
        "Modelo":especificacao["item_name"],
        "Ano":especificacao["item_variant"],
        "Quilometragem":especificacao["item_category"],
        "Transmissão":especificacao["cambio"],
        "Cor":especificacao["cor"]
    }

    return dadosEspecificacao

def tratamentoLocalizacao(localizacao):
    dadosLocalizacao = {
        "Cidade":localizacao["item_category4"],
        "Estado":localizacao["item_category3"]
    }
    
    return dadosLocalizacao

def main():
    try:
        resultadoRaspagem = []
        
        for pagina in range(1,2):
            carros = coletarCarros(pagina)
        
            for carro in carros["items"]:
                objetoCarro = coletarInformacoesDosCarros(carro)
                resultadoRaspagem.append(objetoCarro)
            
            print("Pagina lida botICarros: {}".format(pagina))
            
            #time.sleep(float(randint(60,120)))
            
        bytesJson = json.dumps(resultadoRaspagem, indent=4, ensure_ascii=False).encode('utf8')
        
        f = open("resultadoICarros.txt", "w")
        f.write(bytesJson.decode())
        f.close()

    except Exception as e:
        print(f"An error occurred: {str(e)}")

main()