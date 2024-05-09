import json

arquivoLeitura = open('src/scrap.json', 'r')
arquivoLista = arquivoLeitura.read()
arquivo_json = json.loads(arquivoLista)

for i in arquivo_json:
    if (i["Caracteristicas"]["Fabricante"].upper() == "FORD"):
        print(i["Caracteristicas"]["Modelo"].upper())
        print(i["Preco"])

arquivoLeitura.close()