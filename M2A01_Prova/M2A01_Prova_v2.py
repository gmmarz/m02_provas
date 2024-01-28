#Aluno: Guilherme Melo Marzano
#Enunciado - Programa que cadastra um email e uma senha e em seguida pede para o usuário digitar o email e a senha.
#          - Enquanto o email e senha for inválido continua no loop assim que acertar finaliza
print('Programa verificação de senhas')

flg_prog = True
dic_user = {'user_email':'','pass':''}


#Cadastro usuário
print('Cadastro usuário')

while flg_prog:
    dic_user['user_email'] = input('Digite seu email ou digite (X) para abortar: ').lower()

    if dic_user['user_email'] == 'x':
        flg_prog = False
        break
    else:
        dic_user['pass'] = input('Digite sua senha ou (x) para abortar: ')
        if dic_user['pass'].lower() == 'x': 
            flg_prog = False
            break
        else:
            break

if flg_prog:
    print('Cadastro executado\n')
    print('--------------------')
    print('Realizando o Login')

dic_login = {'log_in':'','log_pass':''}
flg_user = False
flg_pass = False
while flg_prog:
    if not flg_user:
        dic_login['log_in'] = input('Digite seu login: ')
        if dic_login['log_in'] == dic_user['user_email']:
            print('Usuário valido')
            flg_user = True
        else:
            print('Usuário inválido')
    if flg_user:
        dic_login['log_pass'] = input('Digite sua senha: ')
        if dic_login['log_pass'] == dic_user['pass']:
            break
        else:
            print('Senha inválida')
            if input('Deseja alterar o usuário(s)Sim, (n)não: ').lower() == 's':
                flg_user = False
 

if not flg_prog:
    print('Programa abortado pelo usuário')
else:
    print('Usuário e senha corretos, login permitido')

print('---------FIM DO PROGRAMA---------------')


    
