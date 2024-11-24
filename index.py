import os  # LIMPAR A TELA
import time  # TIME SLEEP
import sys  # ESSE É PARA DAR UM EXIT

def menu_criar_nome():
    try:
        os.system("cls")  # limpa a tela
        while True:

            print("==========[LOGIN]==========")
            print("[0]-[\u2795 Registrar Nome    ]") #emoji +
            print("[1]-[\u25B6  Continuar sem nome]") #emoji play
            print("[2]-[\U0001F6AA Sair              ]") #emoji porta
            print("==========================")
            opc_escolhida = int(input("Qual Opção deseja:"))
            if (opc_escolhida == 2):
                msg("Saindo da aplicação", 1)
                break
            elif (opc_escolhida == 1):
                menu_principal("Guest")
            elif (opc_escolhida == 0):
                criar_nome()
            elif (opc_escolhida>2): #DEIXAR COM QUE O USUÁRIO USE APENAS OS NÚMEROS DO MENU
                msg("\u26A0 Não existe essa opção \u26A0", 1)

    except ValueError:
        msg("\u26A0 Você digitou um valor inválido", 1)
        menu_criar_nome()

    except:
        print("\u26A0 Ocorreu algum erro na sua aplicação")

def criar_nome():
    try:
        os.system("cls")
        while True:

            print("==========[NOME]==========")
            print("[\U0001F464]-[Nome...]") #emoji pessoa
            print("==========================")
            nome = input("\U0001F464:") #emoji pessoa
            opc_escolhida = input("\u26A0 Voce deseja salvar (s/n):").lower() #emoji de alerta

            nome_arr = nome.split()

            if (opc_escolhida == "s" or opc_escolhida == "sim"):  # VAZIO TA DANDO ERRO ""
                with open("login_db.txt", "w", encoding="utf-8") as file:
                    file.write(f"{nome_arr[0]}")
                    msg("Criando usuário", 1)
                    cadastrou = True
                    break
            else:
                cadastrou = False
                msg("Cancelando", 1)
                break

        if (cadastrou):
            main()

    except ValueError:
        msg("\u26A0 Você digitou um valor inválido", 1)
        criar_nome()

    except:
        print("\u26A0 Ocorreu algum erro na sua aplicação")

def msg(msg: str, tempo: float): #FUNÇÃO DE MENSAGEM PERSONALIZADO 
    print(msg+"...")
    time.sleep(tempo)
    os.system("cls")

def menu_principal(nome):
    try:
        os.system("cls")
        if (validar_usuario_logado()):

            while True:
                print(f"="*7 + "[Bem vindo]" + "=" * 6)
                print("[0]-[\U0001F4DD Cadastrar carro ]") #emoji  papel e lápis
                print("[1]-[\U0001F50D Buscar carro    ]") #emoji lupa
                print("[2]-[\u2716  Excluir usuário ]") #emoji X
                print("[3]-[\U0001F6AA Sair            ]") #emoji porta
                print("="*24)  # calculo para ajustar com o nome
                opc_escolhida = int(input("Qual Opção deseja:"))

                if(opc_escolhida == 0):
                    cadastrar_carro(nome)
                elif(opc_escolhida == 1):
                    menu_buscar_carro()
                elif(opc_escolhida == 2):
                    msg("Excluindo usuário", 1)
                    with open("login_db.txt", "w") as file:
                        file.write("Guest")
                    menu_criar_nome()
                    break
                elif(opc_escolhida == 3):
                    msg("Saindo da aplicação", 1)
                    sys.exit()
                elif(opc_escolhida > 3):
                    msg("\u26A0 Não existe essa opção \u26A0", 1)
        else:
            while True:
                print(f"="*7 + "[Bem vindo]" + "=" * 6)
                print("[0]-[\U0001F4DD Cadastrar carro  ]") #emoji  papel e lápis
                print("[1]-[\U0001F50D Buscar carro     ]") #emoji lupa
                print("[2]-[\U0001F464 Cadastrar usuário]") #emoji pessoa
                print("[3]-[\U0001F6AA Sair             ]") #emoji porta
                print("="*24)
                opc_escolhida = int(input("Qual Opção deseja:"))

                if (opc_escolhida == 0):
                    print("\u26A0 Você precisa se cadastrar para efetuar essa ação \u26A0") #emoji de alerta
                    time.sleep(3)
                    os.system("cls")
                elif (opc_escolhida == 1):
                    menu_buscar_carro()
                elif (opc_escolhida == 2):
                    criar_nome()
                elif (opc_escolhida == 3):
                    msg("Saindo da aplicação", 1.0)
                    sys.exit()
                elif(opc_escolhida > 3):
                    msg("\u26A0 Não existe essa opção \u26A0", 1)

    except ValueError:
        msg("\u26A0 Você digitou um valor inválido", 1)
        menu_principal(nome)

    except:
        print("\u26A0 Ocorreu algum erro na sua aplicação")

def main():
    os.system("cls")
    with open("login_db.txt", "r", encoding="utf-8") as file:
        nome = file.read()

    if (nome == "Guest"):
        menu_criar_nome()
    else:
        menu_principal(nome)

def validar_usuario_logado():
    with open("login_db.txt", "r", encoding="utf-8") as file:
        nome= file.read()

        if (nome== "Guest"):
            return False
        else:
            return True

def cadastrar_carro(nome):# função para cadastrar carros
    try:
        os.system("cls")
        while True:
            # menu de cadastro
            print(f"======[CADASTRAR]======")
            print("[\U0001F464] <- Nome")  #emoji pessoa
            print("[\U0001F4B0] <- Preço") #emoji sacola de moedas
            print("[\U0001F5D3 ] <- Ano")  #emoji calendário
            print("[\u2699 ] <- Estado")   #emoji engrenagem
            print("========================")

            # inputs do menu de cadastro
            nome_car = input("\U0001F464:").rstrip()     #emoji pessoa
            preco = input("\U0001F4B0:").rstrip()  #emoji sacola de moedas
            ano = input("\U0001F5D3 :").rstrip()    #emoji calendário
            estado = input("\u2699 :").rstrip()           #emoji engrenagem
            autor = nome

            # validações para ver se é válido o carro
            if(int(ano)<=0 or float(preco)<0):
                msg("\u26A0 O valor não pode ser negativo ou igual a zero \u26A0", 1)
            else:
                # cadastrando no txt
                with open("estoque_carros.txt", "a", encoding="utf-8") as file:
                    file.write(f"{nome_car},{preco},{ano},{estado},{autor}"+"\n")  # vai add no arquivo txt
                msg("Cadastrando", 0.5)
                msg("Sucesso!!", 1)

            opc_escolhida = input(
                "\u26A0 Você deseja continuar cadastrando carros ? (s/n) \u26A0 :") #emoji de alerta
            if (opc_escolhida == "n" or opc_escolhida == "não"):
                break

        main()

    except ValueError:
        msg("\u26A0 Você digitou um valor inválido", 1)
        cadastrar_carro(nome)

    except:
        print("\u26A0 Ocorreu algum erro na sua aplicação")

def dados_tratados_arquivo_carros(): 
    os.system("cls")
    carros = []
    with open("estoque_carros.txt", "r", encoding="utf-8") as file:
        for carro in file:
            carro = carro.split(",")
            carros.append({"Nome":carro[0], "Preco": carro[1], "Ano": carro[2], "Estado": carro[3],"Autor": carro[4].replace("\n", "")})
    return carros

def buscar_carro(o_que_deseja_buscar):
    try:
        resultado_da_pesquisa = []
        carros = dados_tratados_arquivo_carros()

        nome_carro_usr = input(f"Digite o {o_que_deseja_buscar.lower()} do carro:")

        msg("Buscando", 1)

        for carro in carros:
            if (carro[o_que_deseja_buscar].lower() == nome_carro_usr.lower()):
                resultado_da_pesquisa.append(carro)
        print("=======================================")
        print(f"[\u26A0 ] - Total:[{len(resultado_da_pesquisa)}] | Pesquisa:[{o_que_deseja_buscar}]   |")
        print("---------------------------------------")
        i = 1
        for carro in resultado_da_pesquisa:
            print(f"[\U0001F50D ]-{i} Nome:{carro["Nome"]}")
            print(f" - Valor: {carro["Preco"]}")
            print(f" - Ano: {carro["Ano"]}")
            print(f" - Estado: {carro["Estado"]} ")
            print(f"   [{carro["Autor"]}]")
            if (len(resultado_da_pesquisa) > 1):
                print("\n")
            i += 1
        print("=======================================")

    except ValueError:
        msg("\u26A0 Você digitou um valor inválido", 1)
        buscar_carro()

    except:
        print("\u26A0 Ocorreu algum erro na sua aplicação")

def menu_buscar_carro():
    try:
        os.system("cls")
        while True:
            os.system("cls")
            # menu de buscar carro
            print(f"======[BUSCAR]======")
            print("[0]-[\U0001F464 Nome  ]")
            print("[1]-[\U0001F4B0 Preço ]")
            print("[2]-[\U0001F5D3  Ano   ]")
            print("[3]-[\u2699  Estado]")
            print("=====================")

            # opção do menu escolhida
            opc_escolhida = int(input("Você deseja buscar pelo?:"))

            # busca por nome
            if (opc_escolhida == 0):
                buscar_carro("Nome")

            # busca por preço
            elif (opc_escolhida == 1):
                buscar_carro("Preco")

            # busca por ano
            elif (opc_escolhida == 2):
                buscar_carro("Ano")

            # busca por estado
            elif (opc_escolhida == 3):
                buscar_carro("Estado")
            
            # opção que não existe
            elif(opc_escolhida > 3):
                    msg("\u26A0 Não existe essa opção \u26A0", 1)

            continuar = input(
                "\u26A0 Você deseja continuar procurando carros ? (s/n) \u26A0 :")
            if (continuar == "n" or continuar == "não"):
                break
        main()

    except ValueError:
        msg("\u26A0 Você digitou um valor inválido", 1)
        menu_buscar_carro()

    except:
        print("\u26A0 Ocorreu algum erro na sua aplicação")

main()  # PAREI AQUI

# FALTA TRATAR OS ERROS
