import json

# Cria arquivo
def iniciaConstrucaoDoResultadoFinal():
    arquivo = open("scrap.json", "a")
    # Abre a lista para esperar os carros raspados
    arquivo.write('[')
    return arquivo

# Adiciona o carro, depois de formatado, no arquivo final
def adicionaRespostasFinais(respostaDoRobo, arquivo):
    for carro in respostaDoRobo:
        # Adiciona carro no arquivo com
        arquivo.write(json.dumps(carro, indent=4, ensure_ascii=False).encode('utf8').decode())
        arquivo.write(',\n')

# Encerra arquivo
def finalizaConstrucaoDoResultadoFinal(arquivo):
    # Fecha o arquivo
    arquivo.close()
    # Abre para poder ler as linhas
    arquivoFinal = open('scrap.json', 'r+')
    linhas = arquivoFinal.readlines()
    arquivoFinal.close()

    # Manipula para tirar a , da ultima linha
    linhaSemVirgula = linhas[-1]
    linhas[-1] = linhaSemVirgula[:-2]
    arquivoFinal = open('scrap.json', 'w')
    arquivoFinal.writelines(linhas)
    # Escreve para fechar a lista
    arquivoFinal.write(']')
    arquivoFinal.close()

    # Tratamento para print de total de itens
    arquivoLeitura = open('scrap.json', 'r')
    arquivoLista = arquivoLeitura.read()
    # Conta o numero de carros lidos
    print(len(json.loads(arquivoLista)))
    arquivoLeitura.close()