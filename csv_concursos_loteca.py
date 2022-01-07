import csv
import requests

base_url = 'http://loterias.caixa.gov.br/wps/portal/loterias/landing/loteca/!ut/\
p/a1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOLNDH0MPAzcDbz8vTxNDRy9_Y2NQ13CDA3cDYEKIoEKnN0\
dPUzMfQwMDEwsjAw8XZw8XMwtfQ0MPM2I02-AAzgaENIfrh-FqsQ9wBmoxN_FydLAGAgNTKEK8DkRrAC\
PGwpyQyMMMj0VAbNnwlU!/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_HGK818G0KOCO10AFFGUTGU00\
04/res/id=buscaResultado/c=cacheLevelPage/=/?timestampAjax=0000000000000'
concurso_url = '&concurso='
n_concurso = '1'

cabecalho = [
    'concurso',
    'apuracao',
    '14_ganhadoras',
    '14_premio',
    '13_ganhadoras',
    '13_premio'
    ]

for i in range(1, 15):
    cabecalho.extend([
        'time_casa_' + str(i),
        'gols_casa_' + str(i),
        'time_visitante_' + str(i),
        'gols_visitante_' + str(i),
        'coluna_' + str(i)
        ])                     

with open('loteca.csv', 'w', newline='') as lotecacsv:
    loteca_writer = csv.writer(lotecacsv)
    loteca_writer.writerow(cabecalho)

    proximo = True
    while proximo:
        request = requests.get(base_url + concurso_url + n_concurso)
        dados_concurso = request.json()

        linha = [
            n_concurso,
            dados_concurso['dtApuracaoStr'],
            dados_concurso['qtGanhadorFaixa1'],
            dados_concurso['vrRateioFaixa1'],
            dados_concurso['qtGanhadorFaixa2'],
            dados_concurso['vrRateioFaixa2'],
            ]

        for jogo in dados_concurso.get('jogos'):
            coluna = 0
            if jogo['colunaMeio']:
                coluna = 1
            elif jogo['colunaDois']:
                coluna = 2
            
            linha.extend([
                jogo['noTime1'],
                jogo['qt_gol_time1'],
                jogo['noTime2'],
                jogo['qt_gol_time2'],
                coluna
                ])

        loteca_writer.writerow(linha)

        if dados_concurso['proximoConcurso'] is None:
            proximo = False
        else:
            n_concurso = str(dados_concurso['proximoConcurso'])
        

    

                     
            
            
        
    
