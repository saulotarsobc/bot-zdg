import requests
import base64
import json


def getLogins(params):
    url = "https://www.conectsantarem.com.br/webservice/v1/radusuarios"
    token = "33:bb65672cc3d4efdf79b7295fee382e79451b5dc88e2472cec0e66850b5972c0d".encode(
        'utf-8')
    headers = {
        'ixcsoft': 'listar',
        'Authorization': 'Basic {}'.format(base64.b64encode(token).decode('utf-8')),
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
        'qtype': 'radusuarios.id',
        'query': '',
        'oper': '!=',
        'page': '1',
        'rp': '99999999',
        'sortname': 'radusuarios.id',
        'sortorder': 'asc',
        'grid_param': json.dumps(params)
    })

    res = requests.post(url, data=payload, headers=headers).json()
    if res['total'] == '0':
        return False
    else:
        return res['registros']


def getClientById(id_cliente):
    url = "https://www.conectsantarem.com.br/webservice/v1/cliente"
    token = "33:bb65672cc3d4efdf79b7295fee382e79451b5dc88e2472cec0e66850b5972c0d".encode(
        'utf-8')
    headers = {
        'ixcsoft': 'listar',
        'Authorization': 'Basic {}'.format(base64.b64encode(token).decode('utf-8')),
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
        'qtype': 'cliente.id',
        'query': id_cliente,
        'oper': '=',
        'sortname': 'cliente.id'
    })

    return requests.post(url, data=payload, headers=headers).json()['registros'][0]


if __name__ == "__main__":
    logins = getLogins(
        [{
            "TB": "radusuarios.conexao",
            "OP": "=",
            "P": "PEREMA-INTELBRAS-01-PON01"
        }]
    )

    # print(len(logins))

    for i in logins:
        id_cliente = i['id_cliente']
        # print(id_cliente)
        print(getClientById(id_cliente))
