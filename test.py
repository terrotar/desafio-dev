

f = open("app/uploads/CNAB.txt", "r")
for line in f:
    transaction = line[0:1]
    date = line[1:9]
    value = float(line[9:19])/100
    cpf = line[19:30]
    card = line[30:42]
    hr = line[42:48]
    owner = line[48:62]
    store = line[62:80]
    print({"Transação": f"{transaction}",
           "Data": f"{date}",
           "Valor": f"{value}",
           "CPF": f"{cpf}",
           "Cartão": f"{card}",
           "Hora": f"{hr}",
           "Dono": f"{owner}",
           "Loja": f"{store}"}, "\n")
