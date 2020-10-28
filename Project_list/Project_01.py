'''Programa listas'''


#RESOLUÇÃO


lista = []
print("Se você digitar: [0] irá sair do programa")
while True:
    valor = int(input("Valor: "))
    if valor == 0:
        break
    lista.append(valor)
#Alteração A
contem = int(input("Digite o valor que você deseja encontrar na lista: "))
if contem in lista:
    p = lista.index(contem)
    print(f'Ele está na posição: {p}')
else:
    print("Esse número não contém na lista! ")

#Alteração B
crescente = sorted(lista)
print(f'A lista na ordem crescente ficará: {crescente}')

#Alteração C

lista.append(0)
pos = 1
for i in range(len(lista)-1, pos-1, -1):
 lista[i] = lista[i-1]
lista[pos] = 33
print(f'Acrescentando o número 33 na posição [1] da lista: {lista}')

#Alteração D

decrescente = sorted(lista, reverse=True)
print(f'A lista na ordem decrescente ficará: {decrescente}')

# Alteração E

print("A média dos números contidos na lista é: ", sum(lista) / len(lista))

#Alteração F

cont = 0
for v in lista:
    if v > 10:
        cont += 1
porcentagem = cont / len(lista) * 100
print("Porcentagem dos números maiores que [10]: ", porcentagem)

#Alteração G

while True:
    print("Deseja adicionar mais números na listas ? Caso não queira digite [0] ")
    add = int(input("Digite o número que queira adicionar: "))
    if add == 0:
       break
    lista.append(add)
print(f'Lista com os número(s) adicionado(s) {lista}')
print("Obrigado por usar nosso programa!")
