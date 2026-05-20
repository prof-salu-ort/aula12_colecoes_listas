#Lista (list)
# A lista é a estrutura de dados mais versátil e comumente usada em Python. 
# Pense nela como um "carrinho de compras" onde você pode adicionar, remover e reordenar 
# itens a qualquer momento.

lista_compras = ['ovos', 'pão', 'leite', 'presunto'] 
print(lista_compras)
produto_01 = 'ovos'
produto_02 = 'pão'
produto_03 = 'leite'
produto_04 = 'presunto'

#Dicionario (dictionary)
# Um dicionário armazena dados em pares de chave-valor. Em vez de acessar por um índice numérico, 
# você acessa por uma chave única. Pense nele como uma agenda de contatos, onde o nome (chave) 
# leva ao número de telefone (valor)
dicionario_aluno = {'matricula' : 1234, 'nome' : 'Juca', 
                    'turma' : 3001, 'media' : 7.5} 
print(dicionario_aluno)

#Tupla (tuple)
# Uma tupla é muito parecida com uma lista, mas com uma diferença crucial: ela é imutável. 
# Uma vez criada, você não pode alterar, adicionar ou remover seus elementos.

tupla_numeros_sorteados = (23, 12, 4, 7, 11) 
print(tupla_numeros_sorteados)

#Conjunto (set)
# Um conjunto é uma coleção de itens únicos e não ordenada. Sua principal utilidade é remover 
# duplicatas e realizar operações matemáticas de conjuntos (união, interseção, etc.).

conjunto_numeros = {1, 2, 3, 4, 5, 1, 2, 3} 
print(conjunto_numeros)