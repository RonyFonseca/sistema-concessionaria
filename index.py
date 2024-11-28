import os  # LIMPAR A TELA
import time  # TIME SLEEP
import sys  # ESSE É PARA DAR UM EXIT

def msg(msg: str, tempo: float): #FUNÇÃO DE MENSAGEM PERSONALIZADO 
    print(msg+"...")
    time.sleep(tempo)
    os.system("cls")

def menu_principal():
    try: #TRATAR ERRO
        os.system("cls")
        while True:
                print(f"="*7 + "[Bem vindo]" + "=" * 6)
                print("[0]-[\U0001F4DD Cadastrar carro ]") #emoji  papel e lápis
                print("[1]-[\U0001F50D Buscar carro    ]") #emoji lupa
                print("[2]-[\U0001F6AA Sair            ]") #emoji porta
                print("="*24)
                opc_escolhida = int(input("Qual Opção deseja:"))

                if(opc_escolhida == 0):
                    cadastrar_carro()
                elif(opc_escolhida == 1):
                    menu_buscar_carro()
                elif(opc_escolhida == 2):
                    msg("Saindo da aplicação", 1)
                    sys.exit()
                elif(opc_escolhida > 2):
                    msg("\u26A0 Não existe essa opção \u26A0", 1)

    except ValueError:
        msg("\u26A0 Você digitou um valor inválido", 1)
        menu_principal()

def cadastrar_carro():# função para cadastrar carros
    try:
        os.system("cls") #clear
        while True:
            # menu de cadastro
            print(f"======[CADASTRAR]======")
            print("[\U0001F464] <- Nome")  #emoji pessoa
            print("[\U0001F4B0] <- Preço") #emoji sacola de moedas
            print("[\U0001F5D3 ] <- Ano")  #emoji calendário
            print("[\u2699 ] <- Estado")   #emoji engrenagem
            print("========================")

            # inputs do menu de cadastro
            nome_car = input("\U0001F464:").strip()     #emoji pessoa
            preco = input("\U0001F4B0:").strip()        #emoji sacola de moedas
            ano = input("\U0001F5D3 :").strip()         #emoji calendário
            estado = input("\u2699 :").strip()          #emoji engrenagem

            # validações para ver se é válido o carro
            if(int(ano)<=0 or float(preco)<=0):
                msg("\u26A0 O valor não pode ser negativo ou igual a zero \u26A0", 1)
            else:
                # cadastrando no txt
                with open("estoque_carros.txt", "a", encoding="utf-8") as file:
                    file.write(f"{nome_car},{preco},{ano},{estado}"+"\n")  # vai add no arquivo txt
                msg("Cadastrando", 0.5)
                msg("Sucesso!!", 1)

                opc_escolhida = input("\u26A0 Você deseja continuar cadastrando carros ? (s/n) \u26A0 :").lower() #emoji de alerta
                if (opc_escolhida == "n" or opc_escolhida == "não"):
                    break
                else:
                    os.system("cls")

        menu_principal()

    except ValueError:
        msg("\u26A0 Você digitou um valor inválido", 1)
        cadastrar_carro()

def dados_tratados_arquivo_carros(): 
    os.system("cls")
    carros = []
    with open("estoque_carros.txt", "r", encoding="utf-8") as file:
        for carro in file:
            carro = carro.split(",")
            carros.append({"Nome":carro[0], "Preco": carro[1], "Ano": carro[2], "Estado": carro[3].replace("\n", "")})
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
            if (len(resultado_da_pesquisa) > 1):
                print("\n")
            i += 1
        print("=======================================")

    except ValueError:
        msg("\u26A0 Você digitou um valor inválido", 1)
        buscar_carro()

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

            continuar = input("\u26A0 Você deseja continuar procurando carros ? (s/n) \u26A0 :").lower()
            if (continuar == "n" or continuar == "não"):
                break
        menu_principal()

    except ValueError:
        msg("\u26A0 Você digitou um valor inválido", 1)
        menu_buscar_carro()

menu_principal()  # PAREI AQUI

# FALTA TRATAR OS ERROS2
