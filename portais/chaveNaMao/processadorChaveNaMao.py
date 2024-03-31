import json

# Processa os carros raspados
def processaCarrosChaveNaMao(carros):
    estruturaCarros = list()
    
    # Acha os carros dentro da tag script
    for scripts in carros:
        estruturaCarros.append(scripts.find('script'))
    
    # Lista para salvar os carros como Json
    carrosJson = list()
        
    # Pega a estrutura dos carros e os salva como json
    for carrosTexto in estruturaCarros:
        carrosJson.append(json.loads(carrosTexto.text))
        
    return carrosJson

# Processamento das características dos carros raspados
def processaInfoCarrosChaveNaMao(carro):
    # Tratamento especial para caracteristicas do carro
    especificacaoFormatada = tratamentoEspecificacao(carro["object"])
    
    # Modelo Json para um carro
    objetoCarro = {
        "Portal": "ChaveNaMão",
        "Caracteristicas": especificacaoFormatada,
        "Preco": carro["object"]["offers"]["price"],
        "URL": carro["object"]["offers"]["url"]
    }
    
    return objetoCarro

# Trata as caracteristicas do carro    
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