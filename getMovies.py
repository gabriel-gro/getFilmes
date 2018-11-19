import requests
import operator

chave = '5b5be94f'
titulo = input("Buscar filme por titulo! Digite o titulo: ")
pagina = 1 # primeira pagina

parametros = {'s': titulo, 'apikey': chave, 'page': pagina, 'type': 'movie'}
r = requests.get('http://www.omdbapi.com/', params=parametros)

data = r.json()

if(data['Response'] == 'False'):
    print('Nenhum resultado encontrado')
else:
    nResultados = int(data['totalResults'])
    lerResultados = len(data['Search'])
    data['Search'] = sorted(iter(data['Search']), key=operator.itemgetter('Year'), reverse=True)

    for filme in data['Search']:
        print(filme['Title'] + '\n' + filme['Year'] + '\n')

    sair = False
    while(nResultados > lerResultados and sair == False):
        op = input('Ver proxima pagina? [s|S para continuar]: ')
        if(op == 's' or op == 'S'):
            pagina += 1
            parametros = {'s': titulo, 'apikey': chave, 'page': pagina, 'type': 'movie'}
            r = requests.get('http://www.omdbapi.com/', params=parametros)

            data = r.json()
            data['Search'] = sorted(iter(data['Search']), key=operator.itemgetter('Year'), reverse=True)

            lerResultados += len(data['Search'])

            for filme in data['Search']:
                print(filme['Title'] + '\n' + filme['Year'] + '\n')

        else:
            sair = True
print("Fim da listagem de filmes!!!")
