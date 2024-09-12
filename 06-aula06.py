print(" Algoritmo do Voto Obrigatório")

idade = int(input("digite sua idade: "))

if (idade >= 18 and idade < 65):
    print("Voto obrigatório!!!")
elif (16<= idade < 18 or idade >= 65):
    print("voto opcional!!!")
else:
    print("voto não permitido!!!")     
    