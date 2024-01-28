#Aluno Guilherme Melo Marzano
#Objetivo: [PY-A02] - Faça um programa que solicite ao usuário que digite 10 valores para
#                     preencher uma lista. Em seguida, o programa deve separar os números pares e ímpares em listas diferentes.
#                     Por fim, exiba na tela os números pares, os números ímpares em uma tupla, a quantidade de números pares e ímpares presentes na lista, e a soma de todos os números pares e ímpares, respectivamente.

#Recebendo dados:
lst_num = []
for i in range(10):
    num = int(input(f'Digite o {i+1}º número inteiro: '))
    lst_num.append(num)

#Separando as listas de pares e impares
lst_par = []
lst_impar = []

for num in lst_num:
    if num % 2 == 0:
        lst_par.append(num)
    else:
        lst_impar.append(num)

#Criando tuplas de numeros pares e impares
tupla_par = tuple(lst_par)
tupla_impar = tuple(lst_impar)

#Gerando as respostas:
print('\n------------------------------------------------------------------')
print('Informação números pares')
print(f'A tupla de números pares é {tupla_par} do tipo: {type(tupla_par)}')
print(f'A quantidade de números pares é: {len(tupla_par)} e a soma deles é {sum(tupla_par)}')
print('\n------------------------------------------------------------------')
print('Informação números impares')
print(f'A tupla de números impares é {tupla_impar} do tipo: {type(tupla_impar)}')
print(f'A quantidade de números pares é: {len(tupla_impar)} e a soma deles é {sum(tupla_impar)}')
