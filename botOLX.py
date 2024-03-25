import requests
from bs4 import BeautifulSoup
import resultParser

# Disable console warning
requests.packages.urllib3.disable_warnings()

url = "https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios?re=30&o=1"

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

## URL: https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios?re=30&o=1
# 30 = até 1980

## Infos do veiculo class="sc-bwzfXH ad__sc-h3us20-0 lbubah"
## Veiculos na pagina class="sc-f431cc3e-2 bBwRRe" -> pegar todas as sections

def get_cars():    
    try:
        # Build session
        session = requests.Session()
        b = session.get(url, headers=headers)
        
        print(b)

        # Make the soup
        soup = BeautifulSoup(b.content, 'html.parser')

        # Get div with the documents
        div_with_cars = soup.find('div', {"class": "sc-f431cc3e-2 bBwRRe"})

        print(div_with_cars)

    except Exception as e:
      print(f"An error occurred: {str(e)}")

def get_specs_from_cars():
    pass

def main():
    # chama get_cars x vezes pra x paginas
    # em cada pagina, entrar na url de cada anuncio e pegar as infos de cada carro
    # chamar as funcoes do result parser
    pass

get_cars()