import regex

# Processa os carros raspados
def processaCarrosICarros(carros):
    
    # Raspa corretamente os anuncios das tags obtidas
    anuncios = ""
    for resultado in carros:
        if "const anuncios =" in str(resultado):
            anuncios = resultado
    
    # Faz as transformações e remove os lixos da raspagem
    stringAnuncios = str(anuncios)
    listAnuncios = stringAnuncios[82:-143]
    # Para fazer os tratamentos, é necessário manipular o resultado em um arquivo
    f = open("portais/ICarros/suporteICarros/resultadoScrapICarros.txt", "w")
    f.write(listAnuncios)
    f.close()
    
    # Limpa do arquivo cru as linhas em branco e remove as vírgulas aleatórias
    with open( 
    "portais/ICarros/suporteICarros/resultadoScrapICarros.txt", 'r') as r, open( 
        'portais/ICarros/suporteICarros/output.txt', 'w') as o: 
        for line in r:
            # Identifica e remove as vírgulas 
            if line == "           ,\n":
                line = " "
            # Remove as linhas em branco 
            if line.strip():
                o.write(line)
             
    # Começa o tratamento para transformar os dados em JSON
    k = open("portais/ICarros/suporteICarros/output.txt", "r")
    oString = k.read()
    # Troca as crases dos valores para aspas duplas
    j = oString.replace("`", "\"")
    
    # Função para adicionar aspas duplas ao redor das ocorrências capturadas
    def adicionar_aspas(match):
        palavra = match.group()
        return "\"" + palavra + "\""

    # Aplicando a substituição através de uma expressão regular que seleciona o valor das chaves
    texto_com_aspas = regex.sub(r'(?<=\{|\s{3})(\w+)(?=:)', adicionar_aspas, j)
    
    # Escreve em um arquivo JSON final para validação e remoção da última vírgula
    jsonFile = open("portais/ICarros/suporteICarros/output.json", "w")
    textoFinal = texto_com_aspas.replace(",\n    ]}", "\n    ]}")
    k.close()
    
    return textoFinal

# Processamento das características dos carros raspados
def processaInfoCarroICarros(carro):
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

# Trata as caracteristicas do carro    
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

# Trata as informações da localização do carro    
def tratamentoLocalizacao(localizacao):
    dadosLocalizacao = {
        "Cidade":localizacao["item_category4"],
        "Estado":localizacao["item_category3"]
    }
    
    return dadosLocalizacao

