#Aluno: Guilherme Marzano
from dic_alunos_func import adicionar_alunos,remover_alunos,atualizar_alunos, ver_alunos

def init():

    dic_alunos = {}
    while True:
        print('\nGerenciamento dicionário alunos')
        print('-'*30)

        print('Digite:\n(1) Adicionar Alunos\
            \n(2) Remover Alunos\
            \n(3) Atualizar Alunos\
            \n(4) ver Lista de Alunos\
            \n(0) Finalizar programa')
        try:
            flg_op = int(input('Digite sua opção: '))
            match flg_op:
                case 1:
                    dic_alunos = adicionar_alunos(dic_alunos)
                case 2:
                    dic_alunos = remover_alunos(dic_alunos)
                case 3:
                    dic_alunos = atualizar_alunos(dic_alunos)
                case 4:
                    ver_alunos(dic_alunos)
                case 0:
                    print('Programa de cadastro finalizado')
                    print('-'*30)
                    break
                case _:
                    print('Digite apenas uma das opções indicadas')
        except ValueError:
            print('Digite apenas uma das opções indicadas')

if __name__ == '__main__':
    init()
else:
    print('Este é o arquivo da aplicação')


