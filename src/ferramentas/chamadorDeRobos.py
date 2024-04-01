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

# Inicia todos os robos
def iniciaRobos(listaParametros, arquivoDeResultado):
    # Itera em cima dos parametros impares para pegar os parametros
    for indiceParametro in range(1, len(listaParametros), 2):
        # Salva nome do portal
        nomePortal = listaParametros[indiceParametro]
        # Salva a quantidade de paginas (numero seguinte a indicacao do portal)
        quantidadeDePaginas = listaParametros[indiceParametro+1]
        # Transforma em inteiro o numero lido
        quantidadeInteira = int(quantidadeDePaginas)
        
        # Tratamento WebMotors
        if nomePortal == "--webMotors":
            # Encerra logo quando não é solicitado esse portal
            if(quantidadeInteira == 0):
                break
            # Chama o respectivo robo para cada pagina
            for pagina in range(1, int(quantidadeInteira)+1):
                respostaDoRobo = (botWebMotors.exec(pagina, userAgent))
                # Monta o resultado final e o adiciona no arquivo final
                montadorDeResultados.adicionaRespostasFinais(respostaDoRobo, arquivoDeResultado)
                # Delay para não ter IP banido
                time.sleep(random.randint(20, 30))

        # Tratamento ChaveNaMao
        elif nomePortal == "--chaveNaMao":
            # Encerra logo quando não é solicitado esse portal
            if(quantidadeInteira == 0):
                break
            # Chama o respectivo robo para cada pagina
            for pagina in range(1, int(quantidadeInteira)+1):
                respostaDoRobo = (botChaveNaMao.exec(pagina, userAgent))
                # Monta o resultado final e o adiciona no arquivo final
                montadorDeResultados.adicionaRespostasFinais(respostaDoRobo, arquivoDeResultado)
                # Delay para não ter IP banido
                time.sleep(random.randint(20, 30))

        # Tratamento ICarros
        elif nomePortal == "--iCarros":
            # Encerra logo quando não é solicitado esse portal
            if(quantidadeInteira == 0):
                break
            # Chama o respectivo robo para cada pagina
            for pagina in range(1, int(quantidadeInteira)+1):
                respostaDoRobo = (botICarros.exec(pagina, userAgent))
                # Monta o resultado final e o adiciona no arquivo final
                montadorDeResultados.adicionaRespostasFinais(respostaDoRobo, arquivoDeResultado)
                # Delay para não ter IP banido
                time.sleep(random.randint(20, 30))
            # Apaga os arquivos de suporte para o portal ICarros
            os.remove("portais/iCarros/output.txt")
            os.remove("portais/iCarros/resultadoScrapICarros.txt")
        
        # Exibe fim de trabalho do robo
        print("Bot {} finalizado com sucesso!".format(nomePortal[2:]))
