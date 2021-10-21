

text = []


f = open("CNAB.txt", "r")
# print(f.read())


for line in f:
    print({"Transação": f"{line[0:1]}",
           "Data": f"{line[1:9]}",
           "Valor": f"{int(line[9:19])/100}",
           "CPF": f"{line[19:30]}",
           "Cartão": f"{line[30:42]}",
           "Hora": f"{line[42:48]}",
           "Dono": f"{line[48:62]}",
           "Loja": f"{line[62:80]}"}, "\n")
