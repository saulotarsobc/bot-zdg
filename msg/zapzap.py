import requests
import re


def formatNumero(numero):
    x = re.split('^\(([0-9]+)\)\s([0-9]+)-([0-9]+)$', numero)

    ddd = int(x[1])

    if ddd > 30:
        if len(x[2]) > 4:
            p1 = x[2][1:]
        else:
            p1 = x[2]
    else:
        p1 = x[2]

    p2 = x[3]

    return f'55{ddd}{p1}{p2}'


def sendMessage(url, numero, mensagem):
    return requests.post(url, {
        'number': f'{formatNumero(numero)}',
        'message': f'{mensagem}'
    }).json()


if __name__ == "__main__":
    cont = 0
    while True:
        
        print(sendMessage(
            'http://127.0.0.1:8000/send-message',
            '(93) 9213-5722',
            cont
        ))
        cont = cont+1
