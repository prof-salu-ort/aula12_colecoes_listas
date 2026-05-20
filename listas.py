#Uma lista é uma estrutura de dados:
# MUTAVEL
# ORDENADA 
# PERMITE VALORES DUPLICADOS

#Criando uma lista do jeito tradicional (com colchetes)
lista_numeros = [1, 2, 3, 4]
print(lista_numeros)

lista_nomes = ['Ana', 'Julia', 'Carlos', 'Juca']
print(lista_nomes)

lista_dados = [True, 102, 'Camarão', 3.1416]
print(lista_dados)

super_lista = [lista_numeros, lista_nomes, lista_dados]
print(super_lista)

#Criando uma lista atraves da função list
nome_lista = list('python')
print(nome_lista)

numero_lista = list(str(12356789))
print(numero_lista)

#Acessando os dados
frutas = ['Maçã', 'Banana', 'Uva', 'Manga', 'Morango', 'Kiwi']

#Para acessar um elemento de uma lista, precisamos utilizar o seu indice(index)
    #***************************************************************
    # REGRA 01- O primeiro elemento de uma lista, está posicionado *
    # sempre na posição ZERO [0]                                   *
    #***************************************************************

#primeiro elemento da lista --> 'Maçã'
print(frutas[0])

#terceiro elemento da lista --> 'Uva'
print(frutas[2])

#ERROR: IndexError: list index out of range (fora dos limites da lista)
#print(frutas[10]) 

#Fatiando uma lista
frutas = ['Maçã', 'Banana', 'Uva', 'Manga', 'Morango', 'Kiwi']

#Exibindo os tres primeiros valores da lista
#***CUIDADO --> Ao fatiar uma lista, o valor MAXIMO não é exibido

# 'Maçã', 'Banana', 'Uva'
print(frutas[0:3])

# 'Uva', 'Manga'
print(frutas[2:4])

#Inverte os elementos da lista
print(frutas[::-1])

#Retorna a lista sem o ultimo elemento
print(frutas[:-1])

#Retorna a lista sem os 2 ultimos elementos
print(frutas[:-2])

#Principais funções em listas
frutas = ['Maçã', 'Banana', 'Uva', 'Manga', 'Morango', 'Kiwi']

#Adiciona um elemento no final da lista
frutas.append('Melão')
print(frutas)

    #*****************************************************************************
    # REGRA 02- Em um lista não existem espaços em branco. Ao remover ou inserir *
    # um novo valor no meio da lista, sempre ocorrerá uma reorganização na lista *
    #*****************************************************************************

#Adiciona um elemento em uma determinada posoção da lista
frutas.insert(2, 'Laranja')
print(frutas)

#Remove o ultimo elemento da lista
#atual --> ['Maçã', 'Banana', 'Laranja', 'Uva', 'Manga', 'Morango', 'Kiwi', 'Melão']
frutas.pop()
print(frutas)

#Remove um elemento ['Laranja'] de uma determinada posição
#atual --> ['Maçã', 'Banana', 'Laranja', 'Uva', 'Manga', 'Morango', 'Kiwi']
fruta_removida = frutas.pop(2)
print(frutas)
print('Fruta removida:', fruta_removida)


#Remove o primeiro elemento baseado no valor passado
frutas.remove('Manga')
print(frutas)

#***CUIDADO com a função remove ***
#Retorna erro, caso não encontre o elemento a ser removido
#frutas.remove('Jaca')

pessoas = ['Juca', 'Ana', 'Juca', 'Pedro']
pessoas.remove('Juca')
print(pessoas)

carros = ['Uno', 'Gol', 'Parati', 'Saveiro', 'Brasilia']
#Retorna o tamanho de uma lista
print(len(carros))

#Ordena uma lista, coloca em ordem alfabética
carros.sort()
print(carros)

#Ordena uma lista, coloca em ordem alfabética reversa
carros.sort(reverse=True)
print(carros)

#retorna a posição (index) de um elemento na lista
print(carros.index('Gol'))

#retorna ERRO, caso o valor procurado não seja encontrado
#print(carros.index('Ferrari'))

#Verifica se um valor está presente na lista
print('Porshe' in carros)
print('Brasilia' in carros)