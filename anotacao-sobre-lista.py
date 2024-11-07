#Imprimir a lista inteira
minha_lista = [1,2,"Olá",3,4,"Olá"]
print(minha_lista)

# Acessar elementos: lista[0]
minha_lista.append(6)
print(minha_lista)

item = int(input("Digite um inteiro:"))
minha_lista.append(item)
print(minha_lista)

minha_lista.remove("Olá")
print(minha_lista)

minha_lista.pop(2)
print(minha_lista)


#modificar elementos: lista[2] = 10
#adiciona elementos no final na lista: lista.append(6) 
#inserir elemento em posiçao especifica :lista.insert(2,8)
#remover o primeiro elemento com o valor especifico: lista.remove("ola")
#remove e retorna o elemento em uma posiçao especifica: lista.pop(1)
#verificar existencica: if 3 in list


#len(lista): tamanho da lista
#min: menor valor da lista / mesma estrutura do len
#Max: maior valor da lista/ mesma coisa
#sum: soma os valores da lista "("A soma da lista:", sum(minha_lista))"


#frutas = ["maça","banana","laranja"]
#for fruta in frutas: / vai percorrer a lista 
#print(fruta)

print("Tamanho da lista:", len(minha_lista))