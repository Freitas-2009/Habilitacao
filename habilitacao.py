print("--------------------------------------------------------")
print("---------------------🚗HABILITAÇÃO🚗-------------------")
print("--------------------------------------------------------")

Nome = input("Digite seu nome: ")
print("--------------------------------------------------------")
Idade = int(input("Digite sua idade: "))

if Idade >= 18:
    print("Maior de idade 🔞")

else:
    print("Menor de idade 👦🏻")
print("--------------------------------------------------------")
print("Possui carteira de motorista ?")
print("(1 - SIM) (2 - NÃO)")
Carteira_motorista = int(input("Escolha uma das opções acima: "))
print("------------------------------------------------------------------------------------------------")
if Carteira_motorista <= 1:
    print("🎉Parabéns, já pode dirigir 🚗")

else: 
    print("Se for menor de idade, espere fazer 18 para tirar sua carteira de motorista ✅")
print("------------------------------------------------------------------------------------------------")