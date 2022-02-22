import json
import ixc
import zapzap
import mycsv
from tabulate import tabulate

url = 'http://127.0.0.1:8000/send-message'

cont = 1
sucessos = []
erros = []

mycsv.setCsv("sucessos", sucessos)
mycsv.setCsv("erros", erros)

# conexao = 'BOA ESP. RADIO'
conexao = ''
concentrador = ''

while conexao == "":
    conexao = input('\nQual é a conexão dos clientes? ')

while concentrador == "":
    concentrador = input('\nQual é o ID do concentrador dos clientes? ')


logins = ixc.getLogins([
    {"TB": "radusuarios.conexao", "OP": "=", "P": conexao},
    {"TB": "radusuarios.id_concentrador", "OP": "=", "P": concentrador}
])

if logins:
    dataTable = []
    for login in logins:
        dataTable.append([
            login['id_cliente'], login['login'], login['conexao'], login['id_concentrador']
        ])
    print(tabulate(dataTable, tablefmt='pretty', headers=[
        "ID Cliente", "Login", "Conexão", "ID Concentrador"
    ]))

else:
    print('\n😁 Nenhum login encontrado\n')
    exit()

continuar = ""
while continuar == "":
    continuar = input('\nContinuar? S | N : ').upper()

if continuar == "N":
    print('\nsaindo...\n')
    exit()

mensagem = input('Sua mensagem: (Use a variável "{nome}") ')

if logins:
    for login in logins:

        cliente = ixc.getClientById(login['id_cliente'])

        whatsapp = cliente['whatsapp']
        if whatsapp == '':
            whatsapp = cliente['telefone_celular']

        nome = cliente['razao']

        numero = '(93) 99213-5722'

        print(
            f'{cont} >>> {login["conexao"]} >>> {login["concentrador"]} >>> {nome}')

        res = zapzap.sendMessage(url, numero, mensagem.replace('{nome}', nome))

        if (res['status']):
            sucessos.append([nome, whatsapp, mensagem.replace('{nome}', nome)])
        else:
            erros.append([nome, whatsapp, res['message']])

        cont = cont + 1
else:
    print('\n😁 Nenhum login encontrado\n')
    exit()


mycsv.setCsv("sucessos", sucessos)
mycsv.setCsv("erros", erros)
