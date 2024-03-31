from portais.webMotors import botWebMotors
from portais.iCarros import botICarros
from portais.chaveNaMao import botChaveNaMao
import json
import sys
import time
import random
import os

# User agent para a requisição
userAgent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0"}

# Lista auxiliar para salvar o retorno dos robos
auxiliarDeRepostas = list()

# Abre arquivo para respostas finais
arquivo = open("scrap.json", "a")
arquivo.write('[')

def adicionaRespostasFinais(auxiliarDeRepostas):
    for carro in auxiliarDeRepostas:
        arquivo.write(json.dumps(carro, indent=4, ensure_ascii=False).encode('utf8').decode())
        arquivo.write(',\n')
        

def chamaRoboWebMotors(quantidadeDePaginas):
    if(quantidadeDePaginas == 0):
        return None
    for pagina in range(1, int(quantidadeDePaginas)+1):
        auxiliarDeRepostas = (botWebMotors.exec(pagina, userAgent))
        adicionaRespostasFinais(auxiliarDeRepostas)
        time.sleep(random.randint(60, 120))
       
def chamaRoboChaveNaMao(quantidadeDePaginas):
    if(quantidadeDePaginas == 0):
        return None
    for pagina in range(1, int(quantidadeDePaginas)+1):
        auxiliarDeRepostas = (botChaveNaMao.exec(pagina, userAgent))
        adicionaRespostasFinais(auxiliarDeRepostas)
        time.sleep(random.randint(60, 120))
        
def chamaRoboICarros(quantidadeDePaginas):
    if(quantidadeDePaginas == 0):
        return None
    for pagina in range(1, int(quantidadeDePaginas)+1):
        auxiliarDeRepostas = (botICarros.exec(pagina, userAgent))
        adicionaRespostasFinais(auxiliarDeRepostas)
        time.sleep(random.randint(60, 120))


# Chama robo para o portal Web Motors
chamaRoboWebMotors(sys.argv[2])
# Chama robo para o portal Chave Na Mão
chamaRoboChaveNaMao(sys.argv[4])
# Chama o robo para o portal iCarros
chamaRoboICarros(sys.argv[6])

#Tratamento para remoção de vírgula extra
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