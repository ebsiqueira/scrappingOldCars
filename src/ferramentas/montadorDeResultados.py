import json

def iniciaConstrucaoDoResultadoFinal():
    arquivo = open("scrap.json", "a")
    arquivo.write('[')
    
    return arquivo
    
def adicionaRespostasFinais(respostaDoRobo, arquivo):
    for carro in respostaDoRobo:
        arquivo.write(json.dumps(carro, indent=4, ensure_ascii=False).encode('utf8').decode())
        arquivo.write(',\n')
        
def finalizaConstrucaoDoResultadoFinal(arquivo):  
    arquivo.close()
    arquivoFinal = open('scrap.json', 'r+')
    linhas = arquivoFinal.readlines()
    arquivoFinal.close()

    linhaSemVirgula = linhas[-1]
    linhas[-1] = linhaSemVirgula[:-2]
    arquivoFinal = open('scrap.json', 'w')
    arquivoFinal.writelines(linhas)
    arquivoFinal.write(']')
    arquivoFinal.close()

    # Tratamento para print de total de itens
    arquivoLeitura = open('scrap.json', 'r')
    arquivoLista = arquivoLeitura.read()
    print(len(json.loads(arquivoLista)))
    arquivoLeitura.close()