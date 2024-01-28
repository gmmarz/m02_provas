#Aluno: Guilherme
#Enunciado -
# [PY-A05] Considere uma lista de números inteiros 
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Utilizando as funções map(),filter() e reduce(), escreva um código que execute as seguintes operações:

# 1.Função map() para obter uma nova lista com o quadrado de cada número da lista numeros

# 2.Função filter() para obter uma nova lista com números pares da lista numeros

# 3.Função reduce()  para obter a soma de todos os números da lista numeros

# -Qual o resultado obtido após a execução das operações acima?

#Importando a biblioteca para poder utilizar a função reduce do exercicío 3
from functools import reduce


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f'\nEsta é a lista dada para a prova:  {numeros}')
print('-'*30)

print('Função map() para obter uma nova lista com o quadrado de cada número da lista numeros')

quadrados_lst = list(map(lambda x: x**2,numeros ))

print(f'Resposta da função map, fazendo o quadrado de cada membro de numeros, transformada em lista é {quadrados_lst}')

print('-'*30)
print('2.Função filter() para obter uma nova lista com números pares da lista numeros')

pares = list(filter(lambda x: x%2 ==0, numeros ))

print(f'Resposta da função filter, filtrando apenas os numeros pares da lista numeros, transformada em lista é {pares}')

print('-'*30)
print('Função reduce()  para obter a soma de todos os números da lista numeros')

soma = reduce(lambda x,y: x + y , numeros)

print(f'Resposta da função reduce, somando os elementos da lista numeros, é {soma}')


