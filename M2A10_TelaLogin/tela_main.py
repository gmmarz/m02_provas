#Tela de login
from tkinter import *
from tkinter import ttk
from funcao_auxiliar import (verificar_email, verificar_senha, validar_novo_email,validor_nova_senha)

def but_cadastrar_usuario():
    novo_email = var_email.get()
    nova_senha = var_senha.get()

    email_ok = validar_novo_email(novo_email)
    if email_ok:
        senha_ok = validor_nova_senha(nova_senha)
        if senha_ok:
            novo_usuario = {"email": novo_email, "senha":nova_senha}
            lst_usuarios.append(novo_usuario)
            var_email.set("")
            var_senha.set("")
            var_cadastro_result.set("Usuário Cadastrato com sucesso")
        else:
            var_cadastro_result.set("Senha deve ter 6 ou mais digitos")
    else:
        var_cadastro_result.set("email deve conter '@'")


def abrir_janela_app():
    app_janela = Toplevel(root)

    app_janela.title(f"Janela App - usuário: {var_user_login.get()}")

    app_janela.geometry("400x200") 

    #Definindo notebook
    app_notebook = ttk.Notebook(app_janela,width=320,height=190)

    tab1 = ttk.Frame(app_notebook,relief="solid",borderwidth=1,width=1)
    tab2 = ttk.Frame(app_notebook,relief="solid",borderwidth=1,width=1)

    #Inserindo elementos na primeira aba
    #-------------------------------------------------------------------
    label_app_titulo = ttk.Label(tab1,text="Bem vindo ao aplicativo")
    label_app_titulo.pack()
    #===================================================================

    #Inserindo elementos na segunda aba
    #--------------------------------------------------------------------
    label_app_cadastro = ttk.Label(tab2,text="Pagina de cadastro")
    label_novo_email = ttk.Label(tab2,text="Email:")
    novo_email_in = ttk.Entry(tab2,textvariable=var_email)
    label_nova_senha = ttk.Label(tab2,text="Senha:")
    nova_senha_in = ttk.Entry(tab2,textvariable=var_senha,show="*")
    label_cad_result = ttk.Label(tab2, textvariable= var_cadastro_result)
    but_cadastrar = ttk.Button(tab2,text="Cadastrar",command=but_cadastrar_usuario)

    label_app_cadastro.grid(row=0,columnspan=1)
    label_novo_email.grid(row=1,column=0)
    novo_email_in.grid(row=1,column=1)
    label_nova_senha.grid(row=2,column=0)
    nova_senha_in.grid(row=2,column=1)
    label_cad_result.grid(row=3,column=1)
    but_cadastrar.grid(row=4,column=1)
    #====================================================================

    app_notebook.add(tab1, text= "App")
    app_notebook.add(tab2,text="Cadastro")

    app_notebook.pack()

def but_validar_login():
    user_in = var_email.get()
    user_senha = var_senha.get()
    user_ok = verificar_email(lst_usuarios,user_in)
    if user_ok:
        senha_ok = verificar_senha(lst_usuarios,user_senha)
        if senha_ok:
            var_user_login.set(var_email.get())
            var_email.set("")
            var_senha.set("")
            var_result.set("")
            
            abrir_janela_app()
        else:
            var_result.set("Senha incorreta")
    else:
        var_result.set("Usuário não encontrado")

root = Tk()
root.geometry("200x200")

root.title("Login")

lst_usuarios = [{"email":"admin@admin","senha":"123456"}]

var_email = StringVar()
var_senha = StringVar()
var_result = StringVar()
var_cadastro_result = StringVar()
var_user_login = StringVar()

#Criando frame de entrada
frame_in = ttk.Frame(root,relief="solid",borderwidth=1,width=180,height=80)
frame_cmd = ttk.Frame(root,relief="solid",borderwidth=1,width=180,height=80)

#Criando elementos frame in
#---------------------------------------------------------------------------
label_titulo = ttk.Label(frame_in,text="LOGIN")
label_email = ttk.Label(frame_in,text="Email: ")
email_in = ttk.Entry(frame_in, textvariable= var_email)
label_senha = ttk.Label(frame_in, text= "Senha:")
senha_in = ttk.Entry(frame_in,textvariable=var_senha, show="*")

#Posicionando os elementos no frame
label_titulo.grid(row=0, column=0,columnspan=2)
label_email.grid(row=1,column=0)
email_in.grid(row=1,column=1)
label_senha.grid(row=2,column=0)
senha_in.grid(row=2,column=1)
#=============================================================================

#Criando elementos do frame de comando
#-----------------------------------------------------------------------------
label_result = ttk.Label(frame_cmd, textvariable=var_result, width=30)
but_login  = ttk.Button(frame_cmd,text="Login!",command= but_validar_login)

label_result.pack()
but_login.pack()

#Mostrando o frame
frame_in.pack(expand=True)
frame_cmd.pack(expand=True)







root.mainloop()