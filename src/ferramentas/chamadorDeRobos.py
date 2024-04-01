import os
import time
import random
from portais.webMotors import botWebMotors
from portais.iCarros import botICarros
from portais.chaveNaMao import botChaveNaMao
from ferramentas import montadorDeResultados

# User agent para a requisição
userAgent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0"}

# Lista auxiliar para salvar o retorno dos robos
respostaDoRobo = list()

def iniciaRobos(listaParametros, arquivoDeResultado):
    for indiceParametro in range(1, len(listaParametros), 2):
        nomePortal = listaParametros[indiceParametro]
        quantidadeDePaginas = listaParametros[indiceParametro+1]
        quantidadeInteira = int(quantidadeDePaginas)
        
        if nomePortal == "--webMotors":
            if(quantidadeInteira == 0):
                break
            for pagina in range(1, int(quantidadeInteira)+1):
                respostaDoRobo = (botWebMotors.exec(pagina, userAgent))
                montadorDeResultados.adicionaRespostasFinais(respostaDoRobo, arquivoDeResultado)
                time.sleep(random.randint(20, 30))

        elif nomePortal == "--chaveNaMao":
            if(quantidadeInteira == 0):
                break
            for pagina in range(1, int(quantidadeInteira)+1):
                respostaDoRobo = (botChaveNaMao.exec(pagina, userAgent))
                montadorDeResultados.adicionaRespostasFinais(respostaDoRobo, arquivoDeResultado)
                time.sleep(random.randint(20, 30))

        elif nomePortal == "--iCarros":
            if(quantidadeInteira == 0):
                break
            for pagina in range(1, int(quantidadeInteira)+1):
                respostaDoRobo = (botICarros.exec(pagina, userAgent))
                montadorDeResultados.adicionaRespostasFinais(respostaDoRobo, arquivoDeResultado)
                time.sleep(random.randint(20, 30))
            os.remove("portais/iCarros/output.txt")
            os.remove("portais/iCarros/resultadoScrapICarros.txt")
        
        print("Bot {} finalizado com sucesso!".format(nomePortal[2:]))
