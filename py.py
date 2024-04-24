import os

msg = []

nome = input("Nome: ")

while True:
    os.system('cls')

    if len(msg) > 0:
        for m in msg:
            print(m['nome'], "-", m['texto'])

    print("_____________")

    texto = input("mensagem: ")
    if texto == "fim":
        break

    msg.append({
        "nome": nome,
        "texto": texto
    })

#usa o terminal com: python nomedoarquivo.py