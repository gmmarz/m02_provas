from Cls_Elevador import Elevador

def configurar_elevador() -> Elevador:
    flg_config = True

    while flg_config:
        try:
            capacidade_total = int(input("Digite a capacidade total de pessoas do elevador: "))
            total_andar = int(input("Digite a quantidade total de andares: "))
            
            if capacidade_total == 0 or total_andar == 0:
                print("-"*30)
                print("Error: Total de andares e capacidade total devem ter valores maiores que 0")
            else:
                flg_config = False

        except ValueError:
            print("Digitar apenas números inteiros")

    flg_config = True
    while flg_config:
        try:
            pessoas_atual = int(input("Digite a quantidade de pessoas atual, ou 0 para começar vazio: "))
            andar_atual = int(input("DIgite o andar atual, ou 0 para começar do Terreo: "))

            if pessoas_atual > capacidade_total or andar_atual > total_andar:
                print("Error: Valores atuais devem ser iguais ou memores que os valores totais")
            else:
                flg_config = False
        except ValueError:
            print("Valores digitados dever ser inteiros")
    nw_elevador = Elevador(capacidade_total, pessoas_atual, total_andar,andar_atual)
    print("="*30)
    print("Elevador configurado")
    print(f"{nw_elevador}")
    return nw_elevador

def utilizar_elevador(elevador: Elevador) -> int:
    flg_utilizando = True

    while flg_utilizando:
        print("-"*30)
        try:
            print("Digite:\
                \n1:Entrar pessoa\
                \n2:Sair pessoa\
                \n3:Subir andar\
                \n4:Descer andar\
                \n5:Andar atual\
                \n6:Status elevador\
                \n7:Parar operação")
            opcao = int(input("Digite uma opção: "))
            print('')

            match opcao:
                case 1:
                    elevador.entrar()
                case 2:
                    elevador.sair()
                case 3:
                    elevador.subir()
                case 4:
                    elevador.descer()
                case 5:
                    print("-"*30)
                    print(f"O Andar atual é: {elevador.get_andar_atual()}")
                case 6:
                    print("-"*30)
                    print(elevador)
                case 7:
                    flg_utilizando = False
                case _ :
                    print("Digite apenas uma das opções indicadas")
        
        except ValueError:
            print("Digite apenas uma das opções indicadas")
    if flg_utilizando == False:
        return -1


flg_app = True

print("ELEVADOR APP CLASSE TESTE")
print("-"*30)
elevador1 = Elevador(0,0,0,0)
while flg_app:
    
    try:
        print("-"*30)
        print("Escolha 1: Configurar Elevador")
        print("        2: Utilizar Elevador")
        print("        3:Sair do programa")
        usuario_escolha = int(input("Digite sua escolha: "))

        match usuario_escolha:
            case 1:
                elevador1 = configurar_elevador()
                
            case 2:
                chck_cfg = elevador1.get_capatidade_total()
                if chck_cfg == 0:
                    print("Elevador deve ser configurado primeiro")
                else:
                    flg_operacao = utilizar_elevador(elevador1)
                    if flg_operacao == -1:
                        print("Operação abortada pelo usuário")
                        flg_app = False
                    else:
                        flg_operacao = 0
            case 3:
                print("Aplicativo fechado pelo usuário")
                flg_app = False
            case _:
                print("Por favor digite apenas as opções indicadas")
      
    except ValueError:
        print("Digite apenas uma das opções indicadas")