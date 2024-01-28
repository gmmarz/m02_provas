# Crie um programa em Python que permita adicionar, remover e visualizar alunos e seus números de matrícula usando um dicionário.
# O programa deve fornecer as seguintes funcionalidades:
# Adicionar um aluno: O usuário poderá adicionar o nome e o número de matrícula de um aluno ao dicionário.
# Remover um aluno: O usuário poderá remover um aluno do dicionário informando o número de matrícula.
# Visualizar todos os alunos: O usuário poderá visualizar todos os alunos registrados no dicionário, exibindo seus respectivos números de matrícula.
# O programa deve ser executado em um loop contínuo até que o usuário escolha sair.


print('Programa de alunos')

flg_prog = True
alunos_inf ={}

def remover_aluno(dic_alunos):
    print('\nRemover aluno')
    print('---------------------')
    flg_remove = 0

    if len(dic_alunos) >= 1:
        pass

        while True:
            if flg_remove == 0:
                try:
                    id_remover = int(input('Digite a matricula que deseja remover digite -1 para cancelar:'))
                    if id_remover == -1:
                        print('Remover abortado')
                        break
                    flg_remove = 1
                    id_sel = dic_alunos.get(id_remover,-1)
                except ValueError:
                    print('Digite apenas valores numericos')
                    flg_remove = 0
            if flg_remove == 1:
                if id_sel == -1:
                    print('Valor de matricula digitado não encontrado. Favor digitar novamente ')
                    flg_remove = 0
                else:
                    escolha = input(f'Deseja apagar o aluno: {dic_alunos[id_remover]}, s- sim, n- não, x- sair: ').lower()

                    match escolha:
                        case 's':
                            del dic_alunos[id_remover]
                            print('Aluno removido')
                            break
                        case 'n':
                            flg_remove = 0
                        case 'x':
                            print('Remover aluno abortado')
                            break
                        case _:
                            print('Digite uma das opções validas')
    else:
        print('Nenhum aluno cadastrado')                        
    return dic_alunos

def adicionar_aluno(dic_alunos):
    print('\nAdicionar aluno')
    print('---------------------')

    if len(dic_alunos) >= 1:
        lst_matricula = dic_alunos.keys()
        nova_matricula =  max(lst_matricula) + 1
    else:
        nova_matricula = 1
    flg_add = 0
    while True:
        if flg_add == 0:
            novo_aluno = input('Digite o nome do aluno: ')
            flg_add = 1
        print(f'Nome digitado: {novo_aluno}')
        escolha = input('Deseja confirmar: s - sim, n - não, x - abortar: ').lower()
        match escolha:
            case 's':
                dic_alunos.update({nova_matricula:novo_aluno})
                break
            case 'n':
                flg_add = 0
            case 'x':
                print('Adicionar aluno abortado')
                break
            case _:
                print('Digite uma das opções validas')
    return dic_alunos


def listar_alunos(dic_alunos):
    print('\nlistar alunos')
    print('---------------------')

    if len(dic_alunos) >= 1:
        lst_alunos = dic_alunos.items()
        for aluno in lst_alunos:
            print(f'Matricula: {aluno[0]}, Nome: {aluno[1]}')
    else:
        print('Nenhum aluno cadastrado')

while flg_prog:
    print('\nSelecione uma das opções:\n1-Adicionar novo aluno'+
            '\n2-Remover aluno' +
            '\n3-Listar todos os alunos' +
            '\n4-Finalizar'    
          )
    try:
        flg_select = int(input('Digite a opção desejada: '))
        match flg_select:
            case 1:
                alunos_inf = adicionar_aluno(alunos_inf)
            case 2:
                remover_aluno(alunos_inf)
            case 3:
                listar_alunos(alunos_inf)
            case 4:
                print('\nPrograma finalizado')
                break
            case _:
                print('\nDigitar apenas uma das opções indicadas')

    except ValueError:
        print('\nDigite apenas os numeros indicados nas opções')
