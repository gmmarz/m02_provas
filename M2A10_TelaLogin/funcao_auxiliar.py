
def verificar_email(lst_usuarios,user_in):
    for usuario in lst_usuarios:
        if user_in == usuario["email"]:
            return True
    return False 

def verificar_senha(lst_usuarios,user_senha):
    for usuario in lst_usuarios:
        if user_senha == usuario["senha"]:
            return True
    return False

def validar_novo_email(novo_email):
    if "@" in novo_email:
        return True
    else:
        return False
    
def validor_nova_senha(nova_senha):
    if len(nova_senha)>=6:
        return True
    else:
        return False
