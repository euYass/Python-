contador = 0

while contador < 100:
    contador +=1

    if(contador == 6):
        print("não mostrar o 6")
        continue 

    if (contador>=10 and contador <= 27):
        print(f"não mostrar o {contador}")
        continue 

   # Se o número não for ,imprime o valor do contador
    print(contador)

    if contador == 40: 
        break   # para a execução do while, sai do loop de repetição 
# Após o término do loop, impreme a mensagem de finalização
print("Fim do programa!")