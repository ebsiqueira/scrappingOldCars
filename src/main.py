# Necessario para nao criar arquivos de cache do python
import sys
sys.dont_write_bytecode = True
from ferramentas import chamadorDeRobos
from ferramentas import montadorDeResultados

# Inicia processo de montagem do arquivo final
arquivoDeResultado = montadorDeResultados.iniciaConstrucaoDoResultadoFinal()
# Chama robos
chamadorDeRobos.iniciaRobos(sys.argv, arquivoDeResultado)
# Finaliza processo de montagem do arquivo final
montadorDeResultados.finalizaConstrucaoDoResultadoFinal(arquivoDeResultado)

# Resultado completo
# Intervalo entre requisições: entre 20 e 30 segundos
# Tempo: 25m 48s
# Carros: 1260
# webMotors: 20 páginas
# chaveNaMao: 20 páginas
# iCarros: 20 páginas

# Execução
# python main.py --webMotors 20 --chaveNaMao 20 --iCarros 20