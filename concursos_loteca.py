import argparse
import requests


parser = argparse.ArgumentParser(description='Imprime os resultados da LOTECA')
parser.add_argument('nconcurso', nargs='?', default='')
args = parser.parse_args()
 
base_url = 'http://loterias.caixa.gov.br/wps/portal/loterias/landing/loteca/!ut/\
p/a1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOLNDH0MPAzcDbz8vTxNDRy9_Y2NQ13CDA3cDYEKIoEKnN0\
dPUzMfQwMDEwsjAw8XZw8XMwtfQ0MPM2I02-AAzgaENIfrh-FqsQ9wBmoxN_FydLAGAgNTKEK8DkRrAC\
PGwpyQyMMMj0VAbNnwlU!/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_HGK818G0KOCO10AFFGUTGU00\
04/res/id=buscaResultado/c=cacheLevelPage/=/?timestampAjax=0000000000000'
concurso_url = '&concurso='

request = requests.get(base_url + concurso_url + args.nconcurso)
sucesso_status = 200

if request.status_code != sucesso_status:
    request = requests.get(base_url)
    print('-' * 80)
    print('{:^80}'.format('Concurso inexistente. Imprimindo resultados do ultimo ' 
                          'concurso disponivel'))

dados_concurso = request.json()
data_apuracao = dados_concurso['dtApuracaoStr']               
n_concurso = str(dados_concurso['concurso'])
n_ganhadoras_14 = str(dados_concurso['qtGanhadorFaixa1'])
n_ganhadoras_13 = str(dados_concurso['qtGanhadorFaixa2'])
premio_14 = str(dados_concurso['vrRateioFaixa1'])
premio_13 = str(dados_concurso['vrRateioFaixa2'])

print('-' * 80)
print('{0:38}  {1:>38}'.format('LOTECA CONCURSO ' + n_concurso,
                               'Apuracao em ' + data_apuracao))
print('-' * 80)
print('{0:^6} {1:^30} {2:^30} {3:>11}'.format('Jogo',
                                              'Time 1',
                                              'Time 2',
                                              'Coluna'))
print('-' * 80)

for index, jogo in enumerate(dados_concurso.get('jogos')):
    index += 1
    time_casa = jogo['noTime1']
    gols_casa = jogo['qt_gol_time1']
    time_visi = jogo['noTime2']
    gols_visi = jogo['qt_gol_time2']

    coluna = ''   
    if jogo['colunaUm']:
        coluna = 'Um'
    elif jogo['colunaMeio']:
        coluna = 'Meio'
    else:
        coluna = 'Dois'
        
    print('{0:^6} {1:26} {2:^3} {3:^3} {4:^3} {5:>26} {6:>7}'.format(str(index),
                                                                     time_casa,
                                                                     gols_casa,
                                                                     'x',
                                                                     gols_visi,
                                                                     time_visi,
                                                                     coluna))
    
print('-' * 80)
print('14 acertos {0} apostas ganhadoras. Premio R$ {1}'.format(n_ganhadoras_14,
                                                                premio_14))
print('13 acertos {0} apostas ganhadoras. Premio R$ {1}'.format(n_ganhadoras_13,
                                                                premio_13))
print('-' * 80)

    


    




