
import requests
with open('lista.txt', 'r') as kkk:
    diretorio = kkk.readlines()

try:    
    
    url = input('digite a URL :')
    for dir in diretorio:
        
        oi = requests.get(f'{url}/{dir}')
        status = oi.status_code
        if status == 200:
            print(f'diretorio encontrado \033[32m{oi.url}\033[0;0m')
            print('tentando encontrar ....')
except:
    print('erro , tente digitar parâmetro certo ')
