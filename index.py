from bs4 import BeautifulSoup
import requests

def resultado(titulo_site, titulo_tabela, horario, bichos):
    listaDeBichos = list()
    listaDeBichos.append(titulo_site)
    listaDeBichos.append(titulo_tabela)
    listaDeBichos.append(horario)

    count = -1
    naoTem = ['O', 'resultado', 'não', 'saiu', 'ainda']

    for bicho in bichos:
        count += 1

        if bicho.get('title') == '0':
            bicho['title'] = naoTem[count]

        listaDeBichos.append(bicho.get("title"))

    return listaDeBichos

try:
    url = requests.get("https://www.ojogodobicho.com/deu_no_poste.htm")
    soup = BeautifulSoup(url.content, "html.parser")

    titulo_site = soup.title.string
    titulo_tabela = soup.find("caption").string
    bichos_horario = soup.find_all(string=["PTM", "PT", "PTV", "FED", "COR"], limit=5)

    bichos_manha = soup.select("tbody tr > td:nth-child(2)", limit=5)
    bichos_tarde = soup.select("tbody tr > td:nth-child(3)", limit=5)
    bichos_federal = soup.select("tbody tr > td:nth-child(5)", limit=5)

    print(" ".join(resultado(titulo_site, titulo_tabela, 'p.t.m', bichos_manha)))
    print(" ".join(resultado(titulo_site, titulo_tabela, 'p.t', bichos_tarde)))
    print(" ".join(resultado(titulo_site, titulo_tabela, 'federal', bichos_federal)))

except Exception as err:
    print(err)
