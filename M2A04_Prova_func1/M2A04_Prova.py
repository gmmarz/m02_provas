#Aluno: Guilherme
#Objetivo: [PY-A04] Desenvolva um programa em Python que permita ao usuário digitar várias notas.
# Em seguida, crie uma função chamada "calcular_media" que irá receber as notas digitadas e calcular a média do aluno.
# Também crie uma função chamada "verificar_situacao" que, com base na média calculada, irá exibir a situação do aluno: 
#"Reprovado" se a média for menor que 7,
# "Aprovado" se a média for maior ou igual a 7,
# e "Parabéns, sua média é 10" se a média for igual a 10.

def coletar_notas() -> float:
    lst_notas = []
    i = 1
    while True:
        str_nota = input(f'Digite a {i}º nota ou digite (s) para finalizar a cadastro de notas: ')
        if str_nota == 's':
            break
        try:
            nota = float(str_nota)
            if nota < 0 or nota > 10:
                print('Favor digite uma nota dentro do range de 0 a 10')
            else:
                lst_notas.append(nota)
                i +=1
        except ValueError:
            print('Digite apenas valores númericos ou s para finalizar.')
    return lst_notas

def calcular_media(lst_nota:float) -> float:
    lst_nota = list(lst_nota)
    media = sum(lst_nota)/len(lst_nota)
    return media

def verificar_situacao(media:float) -> str:
    situacao = ''
    if media == 10:
        situacao = 'Parabéns sua média é 10\n'
    elif media >= 7 and media < 10:
        situacao = f'Aprovado com média = {media}\n'
    elif media < 7 and media >=0:
        situacao = f'Reprovado com média = {media}\n'
    else:
        situacao = f'Erro - Média = {media} que está fora do range de 0 a 10.\nVerificar notas e tentar novamente'
    return situacao

print('Programa verificará se aluno foi aprovado pela media das notas.')

lst_notas = []

while True:
    try:
        flg_opcao = int(input('Escolha uma das opções:\n(1)Cadastrar notas.\n(2)Verificar Situacao\n(3)Sair\n Digite sua opção: '))
        match flg_opcao:
            case 1:
                lst_notas = []
                lst_notas = coletar_notas()
                
            case 2:
                if len(lst_notas) == 0:
                    print('Nenhuma nota cadastrada\n')
                else:
                    media = calcular_media(lst_notas)
                    print(verificar_situacao(media))
            case 3:
                break
            case _:
                print('Digite apenas uma das opções indicadas\n')
                
    except ValueError:
        print('Favor escolha apenas uma das opções\n') 

print('-'*30)
print('Programa finalizado')

        
        
        





