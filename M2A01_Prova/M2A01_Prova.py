#Aluno: Guilherme Melo Marzano
#Enunciado - Programa que cadastra um email e uma senha e em seguida pede para o usuário digitar o email e a senha.
#          - Enquanto o email e senha for inválido continua no loop assim que acertar finaliza
import getpass

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
        #Validando email:
        if len(dic_user['user_email']) <=1 or '@' not in dic_user['user_email'] or '.' not in dic_user['user_email']:
            print('email inválido') 
        elif len(dic_user['user_email'].split('@')[0])< 1 or len(dic_user['user_email'].split('@')[1])< 1:
            print('email inválido')
        else:
            dic_user['pass'] = getpass.getpass('Digite sua senha: ')
            break
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
        dic_login['log_pass'] = getpass.getpass('Digite sua senha: ')
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


    
