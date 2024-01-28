#Aluno: Guilherme Marzano
import tkinter as tk

def validar_entrada(valor_entrada):
    try:
        valor_num = float(valor_entrada)
        
    except ValueError:
        var_resultado.set("ERRO: Digitar apenas números")
        var_entrada.set("")
        valor_num = "error"
    return valor_num

def converter_medida():
    var_resultado.set('')
    num_in = validar_entrada(var_entrada.get())
    conv_op = var_opcao_conversao.get()

    if not num_in == "error":
        if conv_op == 1:
            var_resultado.set(num_in/100)
        else:
            var_resultado.set(num_in*100)
def limpar():
    var_resultado.set("")
    var_entrada.set("")

    #var_resultado.set(var_opcao_conversao.get())


root = tk.Tk()
root.title("Conversor medida")
root.geometry("300x200")

var_entrada = tk.StringVar()
var_opcao_conversao = tk.IntVar()
var_resultado = tk.StringVar()


#Configurando frames
frame_in = tk.Frame(root,relief="solid",borderwidth=1, width=1, height=80)
frame_cmd = tk.Frame(root,relief="solid",borderwidth=1)
frame_result = tk.Frame(root,relief="solid",borderwidth=1)

#Configuranto elementos de entrada
#----------------------------------------------------------
titulo = tk.Label(frame_in,text="Conversor de unidade")
pergunta = tk.Label(frame_in,text="Digite um número:")
entrada = tk.Entry(frame_in,textvariable=var_entrada)

#Configurando os elementos de entrada
titulo.grid(row=0,column=0, columnspan=2)
pergunta.grid(row=1,column=0)
entrada.grid(row=1, column=1)
#*************************************************************

#Configurando elementos de comando
#----------------------------------------------------------------------------------------------
op_cm_metros = tk.Radiobutton(frame_cmd,text="cm para m",variable=var_opcao_conversao,value=1)
op_metros_cm = tk.Radiobutton(frame_cmd,text="m para cm", variable=var_opcao_conversao,value=2)
but_converter = tk.Button(frame_cmd,text="Converter",command=converter_medida, width= 15)
but_clear = tk.Button(frame_cmd,text="Limpar",command=limpar,width=15)

#Configurando posicionamento nos frame de comando
op_cm_metros.grid(row=0,column=0)
op_metros_cm.grid(row=0,column=1)
but_converter.grid(row=1,column=0)
but_clear.grid(row=1,column=1)
#**************************************************************

#Configurando frame de resultado
#-----------------------------------------------------------------------------------
lbl_result_title = tk.Label(frame_result,text="Resultado")
lbl_result = tk.Label(frame_result,textvariable=var_resultado,fg="black",bg="white",width=30)

#Posicionando widgets no frame resuldato
lbl_result_title.grid(row=0,column=0)
lbl_result.grid(row=1,column=0)
#**************************************************************

#Posicionando os frames:
frame_in.pack(expand=True,fill='x')
frame_cmd.pack(expand=True,fill='x')
frame_result.pack(expand=True,fill='x')



root.mainloop()
