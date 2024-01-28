from classes import Material,Livro,Revista

def listar_materiais(materiais: list[Material]) -> None:
    for material in materiais:
        print("-"*30)
        material.exibir_informacoes()
        
def aquisitar_genero(dados_livro: dict) -> tuple:
    flg_aquisitar = True
    genero_ok = False
    resultado = (bool,dict)
    
    while flg_aquisitar:
        op = ""
        if not genero_ok :
            genero = input("Digite o genero do livro: ")
        if len(genero) <=1:
            print("genero do livro deve ter mais que 1 letra")
            genero_ok = False
        else:
            genero_ok = True

        if genero_ok:
            print('-'*30)
            print(f"Genero digitado foi:\nGenero: {genero} deseje alterar digite 1: genero, 2:Confirmar, 3:Cancelar")
            op = input("Digite a opção desejada: ")
            match op:
                case "1":
                    titulo_ok = False
                case "2":
                    dados_livro.update({"genero": genero})
                    resultado= (True,dados_livro)
                    flg_aquisitar = False
                case "3":
                    dados_livro = {"cancelado": -1}
                    resultado = (False,dados_livro)
                    flg_aquisitar = False
                case _:
                    print("Digite apenas uma das opções indicadas")
                    flg_aquisitar = False
                    op = ""
        else:
            print('-'*30)
            print("Genero fornecido está errado, favor inserir novamente")
            op = input("Digite 1:Consertar, 2:Cancelar : ")
            match op:
                case "1":
                    op = ""
                    flg_aquisitar = True
                case "2":
                    dados_livro = {"cancelado": -1}
                    resultado = (False,dados_livro)
                    flg_aquisitar = False
                case _:
                    print("Digite apenas uma das opções indicadas")
                    op = ""
                    flg_aquisitar = True
    return resultado

def aquisitar_edicao(dados_livro: dict) -> tuple:
    flg_aquisitar = True
    edicao_ok = False
    resultado = (bool,dict)
    
    while flg_aquisitar:
        op = ""
        if not edicao_ok :
            edicao = input("Digite o edicao da revista: ")
        if len(edicao) <=1:
            print("edicao da revista deve ter mais que 1 letra")
            edicao_ok = False
        else:
            edicao_ok = True

        if edicao_ok:
            print('-'*30)
            print(f"edicao digitado foi:\nedicao: {edicao} deseje alterar digite 1: edicao, 2:Confirmar, 3:Cancelar")
            op = input("Digite a opção desejada: ")
            match op:
                case "1":
                    titulo_ok = False
                case "2":
                    dados_livro.update({"edicao": edicao})
                    resultado= (True,dados_livro)
                    flg_aquisitar = False
                case "3":
                    dados_livro = {"cancelado": -1}
                    resultado = (False,dados_livro)
                    flg_aquisitar = False
                case _:
                    print("Digite apenas uma das opções indicadas")
                    flg_aquisitar = False
                    op = ""
        else:
            print('-'*30)
            print("edicao fornecida está errada, favor inserir novamente")
            op = input("Digite 1:Consertar, 2:Cancelar : ")
            match op:
                case "1":
                    op = ""
                    flg_aquisitar = True
                case "2":
                    dados_livro = {"cancelado": -1}
                    resultado = (False,dados_livro)
                    flg_aquisitar = False
                case _:
                    print("Digite apenas uma das opções indicadas")
                    op = ""
                    flg_aquisitar = True
    return resultado
    
    

def aquisitar_dados_comuns() -> tuple:
    
    flg_aquisitar = True
    titulo_ok = False
    autor_editora_ok = False
    
    dados_livro = {}
    resultado = (bool,dict)
    
    while flg_aquisitar:
        op = ""
        if not titulo_ok:
            titulo = input("Digite o titulo: ")
            if len(titulo) <=1:
                print("titulo deve ter mais que 1 letra")
                titulo_ok = False
            else:
                titulo_ok = True
        if not autor_editora_ok:
            autor_editora = input("Digite o autor ou editora: ")
            if len(autor_editora) <=1:
                print("autor ou editora deve ter mais que 1 letra")
                autor_editora_ok = False
            else:
                autor_editora_ok = True
        if titulo_ok and autor_editora_ok:
            print('-'*30)
            print(f"Dados digitados foram:\nTitulo: {titulo}\nAutor ou Editora: {autor_editora}\nCaso deseje alterar digite 1: Livro, 2:Autor ou Editora, 3:Confirmar, 4:Cancelar")
            op = input("Digite a opção desejada: ")
            match op:
                case "1":
                    titulo_ok = False
                case "2":
                    autor_editora_ok = False
                case "3":
                    dados_livro = {"titulo":titulo,"autor_ou_editora": autor_editora}
                    resultado = (True,dados_livro)
                    flg_aquisitar = False
                case "4":
                    dados_livro = {"cancelado": -1}
                    resultado = (False,dados_livro)
                    flg_aquisitar = False
                case _:
                    print("\nDigite apenas uma das opções indicadas")
        else:
            print('-'*30)
            print("Uma ou mais dados fornecidos estão errados, favor inserir novamente")
            op = input("Digite 1:Consertar, 2:Cancelar : ")
            match op:
                case "1":
                    op = ""
                    flg_aquisitar = True
                case "2":
                    dados_livro = {"cancelado": -1}
                    resultado = (False,dados_livro)
                    flg_aquisitar = False
                case _:
                    print("Digite apenas uma das opções indicadas")
                    op = ""
                    flg_aquisitar = True
    return resultado
        
    
def cadastrar_livro() -> tuple:
    flg_add_livro = True
    resultado = (bool,Material)
    print("="*30)
    print("Cadastro de livro")
    dados_livro = {"titulo": "","autor_ou_editora":"","genero":""}
      
    while flg_add_livro:
        dados_ok,dados_livro =  aquisitar_dados_comuns()
        if  dados_ok:
            dados_ok,dados_livro = aquisitar_genero(dados_livro)
            if dados_ok:
                livro = Livro(dados_livro.get("titulo"),dados_livro.get("autor_ou_editora"),dados_livro.get("genero"))
                resultado = (True,livro)
                flg_add_livro = False
            else:
                resultado = (False,"")
                flg_add_livro = False
        else:
            resultado = (False,"")
            flg_add_livro = False
    return resultado

def cadastrar_revista() -> tuple:
    flg_add_revista = True
    resultado = (bool,Material)
    print("="*30)
    print("Cadastro de revista")
    dados_revista= {"titulo": "","autor_ou_editora":"","edicao":""}
      
    while flg_add_revista:
        dados_ok,dados_revista =  aquisitar_dados_comuns()
        if  dados_ok:
            dados_ok,dados_revista = aquisitar_edicao(dados_revista)
            if dados_ok:
                revista = Revista(dados_revista.get("titulo"),dados_revista.get("autor_ou_editora"),dados_revista.get("edicao"))
                resultado = (True,revista)
                flg_add_revista = False
            else:
                resultado = (False,"")
                flg_add_revista = False
        else:
            resultado = (False,"")
            flg_add_revista = False
    return resultado



def main():
    flg_app = True
    materiais = []
    
    print("Cadastro Materiais")
    while flg_app:
        op = ""
        print("Cadastro de material opções:\n--------------\n 1:Cadastrar livro\n 2:Cadastrar revista\n3:Listar materiais\n4:Sair")
        op = input("Digite uma das opções: ")
        match op:
            case "1":
                livro_ok,livro = cadastrar_livro()
                if livro_ok:
                    materiais.append(livro)
                    flg_app = True
                else:
                    print("Programa fechado pelo usuário")
            case "2":
                revista_ok,revista = cadastrar_revista()
                if revista_ok:
                    materiais.append(revista)
                    flg_app = True
                else:
                    print("Programa fechado pelo usuário")
            case "3":
                listar_materiais(materiais)
                flg_app = True
            case "4":
                print("Programa fechado pelo usuário")
                flg_app = False
            case _:
                print("Digite uma das opções indicadas")
                
def test_instancias():
    l1 = Livro("Senhor dos aneis","JJ Tokin","Fantasia")
    revista1 = Revista("Caras","Globo","Ed1")
    l2 = Livro("Storyteling com dados","Cole nussbaumer","Estudo")
    revista2 = Revista("Isto é","Globo","ed10")
    revista3 = Revista("Carros","Dufax","Ed15")
    l3 = Livro("Cristais","Ember Grand","Estudo")
    
    materiais = [l1,revista1,l2,revista2,revista3,l3]
    listar_materiais(materiais)



if __name__ == "__main__":
    
    print("*="*30)
    print("Digite 1:Para Teste customizado\n 2:Solução prova teste fixo")
    op = input("Escolha a opcao: ")
    match op:
        case "1":
            main()
        case "2":
            test_instancias()
        case _:
            print("Digite apenas uma das opções desejadas, tente de novo.")
