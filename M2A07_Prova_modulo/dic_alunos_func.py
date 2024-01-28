from func_auxiliares import continuar_operacao

def adicionar_alunos(dic_alunos:dict)-> dict:
    while True:
        print('Adicionar alunos')
        print('-'*30)
        try:
            aluno_id = int(input('Digite a matricula do aluno: '))
            if aluno_id in dic_alunos:
                print('Matricula digitada já existe, tente novamente com outra matrícula')
            else:
                aluno_nome = input('Digite o nome do aluno: ').capitalize()
                dic_alunos.update({aluno_id:aluno_nome}) 
        except ValueError:
            print('Para Matricula digitar apenas número inteiro')
        if not continuar_operacao():
            return dic_alunos

def remover_alunos(dic_alunos:dict)-> dict:
    
    while True:
        print('Remover alunos')
        print('-'*30)

        if len(dic_alunos) == 0:
            print('Dicionário de alunos vazio')
            print('Não é possível continuar com a remoção')
            return dic_alunos
        else:

            try:
                aluno_id = int(input('Digite a matrícula do aluno: '))
                if aluno_id not in dic_alunos:
                    print('Matricula digitada não existe. Não é possível excluir')
                else:
                    print(f'Matricula: {aluno_id}, nome: {dic_alunos[aluno_id]} foi removido')
                    dic_alunos.pop(aluno_id)
            except ValueError:
                print('Para Matricula digitar apenas números inteiros')
        if not continuar_operacao():
            return dic_alunos
        
def atualizar_alunos(dic_alunos:dict)->dict:

    while True:
        print('Atualizar cadastro aluno:')
        print('-'*30)
        if len(dic_alunos) == 0:
            print('Dicionário de alunos vazio\nNão é possível atualizar')
            print('Favor adicionar um aluno na opção adicionar aluno')
            return dic_alunos
        try:
            aluno_id = int(input('Digite a matrícula do aluno: '))
            if aluno_id not in dic_alunos:
                print('Matricula digitada não existe. Não é possível alterar')
            else:
                novo_nome = input('Digite o novo nome do aluno:').capitalize()
                print(f'O aluno de matricula {aluno_id}, nome: {dic_alunos[aluno_id]}')
                dic_alunos[aluno_id] = novo_nome
                print('foi alterado para:')
                print(f'Matrícula: {aluno_id}\nnome: {dic_alunos[aluno_id]}')
        except ValueError:
            print('Para Matricula digitar apenas números inteiros')
        if not continuar_operacao():
            return dic_alunos
        
def ver_alunos(dic_alunos:dict):
    print('\nLista de Alunos cadastrados')
    print('-'*30)
    
    if len(dic_alunos) == 0:
        print('Nenhum aluno cadastrado')
    else:
        for id,nome in dic_alunos.items():
            print(f'Matricula: {id} - nome: {nome}')

if __name__ == '__main__':
    print('Este arquivo é um módulo e não deve ser executado diretamente')