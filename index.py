from bs4 import BeautifulSoup
import requests


def resultado(titulo_site, titulo_tabela, horario, bichos):
    if len(bichos) == 0:
        return ['O resultado não saiu ainda']

    listaDeBichos = list()
    listaDeBichos.append(titulo_site)
    listaDeBichos.append(titulo_tabela)
    listaDeBichos.append(horario)

    for bicho in bichos:
        if bicho.get('title') == '0':
            return ['O resultado não saiu ainda']

        listaDeBichos.append(bicho.get('title'))

    return listaDeBichos


try:
    url = requests.get('https://www.ojogodobicho.com/deu_no_poste.htm')
    soup = BeautifulSoup(url.content, 'html.parser')

    titulo_site = soup.title.string
    titulo_tabela = soup.find('caption').string

    bichos_manha = soup.select('tbody tr > td:nth-child(2)', limit=5)
    bichos_tarde = soup.select('tbody tr > td:nth-child(3)', limit=5)
    bichos_noite = soup.select('tbody tr > td:nth-child(4)', limit=5)
    bichos_federal = soup.select('tbody tr > td:nth-child(5)', limit=5)
    bichos_corujinha = soup.select('tbody tr > td:nth-child(6)', limit=5)

    print(' '.join(resultado(titulo_site, titulo_tabela, 'p.t.m', bichos_manha)))
    print(' '.join(resultado(titulo_site, titulo_tabela, 'p.t', bichos_tarde)))
    print(' '.join(resultado(titulo_site, titulo_tabela, 'p.t.v', bichos_noite)))
    print(' '.join(resultado(titulo_site, titulo_tabela, 'federal', bichos_federal)))
    print(' '.join(resultado(titulo_site, titulo_tabela, 'corujinha', bichos_corujinha)))

except Exception as err:
    print(err)
