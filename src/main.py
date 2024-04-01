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