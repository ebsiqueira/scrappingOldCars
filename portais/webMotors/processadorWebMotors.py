def processaInfoCarrosWebMotors(carro, urlAtual):
    especificacaoFormatada = tratamentoEspecificacao(carro["Specification"])
    localizacaoFormatada = tratamentoLocalizacao(carro["Seller"]["Localization"][0])
    
    objetoCarro = {
        "Portal": "WebMotors",
        "Caracteristicas": especificacaoFormatada,
        "Localizacao": localizacaoFormatada,
        "Preco": carro["Prices"]["Price"],
        "URL": urlAtual
    }
    
    return objetoCarro

def tratamentoEspecificacao(especificacao):
    dadosEspecificacao = {
        "Fabricante":especificacao["Make"]["Value"],
        "Modelo":especificacao["Model"]["Value"],
        "Ano":especificacao["YearModel"],
        "Quilometragem":especificacao["Odometer"],
        "Transmissão":especificacao["Transmission"],
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
        "Pais":localizacao["Country"]
    }
    
    return dadosLocalizacao