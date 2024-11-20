import os #LIMPAR A TELA
import time #TIME SLEEP
import sys #ESSE É PARA DAR UM EXIT 
import json #TRATRAR OS TXT COMO JSON 

#LOGIN 
def login():
    os.system("cls") # limpa a tela
    while True:

        print("==========[LOGIN]==========")
        print("[0]-[\u2795 Registrar Nome    ]")
        print("[1]-[\u25B6  Continuar sem nome]")
        print("[2]-[\U0001F6AA Sair              ]")
        print("==========================")
        res = int(input("Qual Opção deseja:"))
        if(res==2):
            msg("Saindo da aplicação", 1)
            break
        elif(res==1):
            menu("Guest")
        elif(res==0):
            registrar_user()

def registrar_user():
    os.system("cls")
    while True:

        print("==========[NOME]==========")
        print("[\U0001F464]-[Nome...]")
        print("==========================")
        nome = input("\U0001F464:")
        decisao = input("\u26A0 Voce deseja salvar (s/n):").lower()
        
        nome_arr = nome.split()
        db = [{"Nome": nome_arr[0]}]

        if(decisao=="s" or decisao=="sim"):
            with open("login_db.txt", "w") as file:
                file.write(str(db))
                msg("Criando usuário", 1)
                cadastrou = True
                break
        else:
            cadastrou = False
            msg("Cancelando", 1)
            break

    if(cadastrou):
        main()

def msg(msg:str, temp:float):
    print(msg+"...")
    time.sleep(temp)
    os.system("cls")

def menu(nome):
    os.system("cls")
    if(logado()):
        
        while True:
            print(f"="*7 + "[Bem vindo]" + "=" *6)
            print("[0]-[\U0001F4DD Cadastrar carro ]")
            print("[1]-[\U0001F50D Buscar carro    ]")
            print("[2]-[\u2716  Excluir usuário ]")
            print("[3]-[\U0001F6AA Sair            ]")
            print("="*24) # calculo para ajustar com o nome 
            res = int(input("Qual Opção deseja:"))

            if(res==0):
                if(logado()):
                    cadastrar_carro(nome)
            elif(res==1):
                buscar_carro()
            elif(res==2):
                db = [{"Nome":'Guest'}]
                msg("Excluindo usuário", 1)
                with open("login_db.txt", "w") as file:
                    file.write(str(db))
                login()
                break
            elif(res==3):
                msg("Saindo da aplicação", 1)
                sys.exit()
    else:
        tamanho_da_letra = int(len(nome))
        diminuir = round(tamanho_da_letra/2)
        if(diminuir%2!=0):
            diminuir+=1
        while True:
            print("=="*diminuir + f"[Bem vindo {nome}]"+ "=="*diminuir)
            print("[0]-[\U0001F4DD Cadastrar carro  ]")
            print("[1]-[\U0001F50D Buscar carro     ]")
            print("[2]-[\U0001F464 Cadastrar usuário]")
            print("[3]-[\U0001F6AA Sair             ]")
            print("="*tamanho_da_letra + "="*12 + "="*8)
            res = int(input("Qual Opção deseja:"))

            if(res==0):
                print("\u26A0 Você precisa se cadastrar para efetuar essa ação \u26A0")
                time.sleep(3)
                os.system("cls") 
            elif(res==1):
                buscar_carro()
            elif(res==2):
                registrar_user()
            elif(res==3):
                msg("Saindo da aplicação", 1.0)
                sys.exit()


def main():
    os.system("cls")
    with open("login_db.txt", "r") as file:
        arquivo_lido_do_db = file.read()
        arquivo_lido_do_db = arquivo_lido_do_db.replace("'", '"')
    arquivo_convertido_dicionario = json.loads(arquivo_lido_do_db)

    if(arquivo_convertido_dicionario[0]["Nome"]=='Guest'):
        login()
    else:
        menu(arquivo_convertido_dicionario[0]["Nome"])

def logado():
    with open("login_db.txt", "r") as file:
        nomes = file.read()
        nomes = nomes.replace("'", '"')
        nomes = json.loads(nomes)

        if(nomes[0]["Nome"] == "Guest"):
            return False
        else:
            return True

def cadastrar_carro(nome):#função para cadastrar carros
        os.system("cls")
        while True:
            # menu de cadastro
            print(f"======[CADASTRAR]======")
            print("[\U0001F464] <- Nome")
            print("[\U0001F4B0] <- Preço")
            print("[\U0001F5D3 ] <- Ano")
            print("[\u2699 ] <- Estado")
            print("========================")

            # inputs do menu de cadastro
            nome_car = input("\U0001F464:")
            preco = input("\U0001F4B0:")
            ano = input("\U0001F5D3 :")
            estado = input("\u2699 :")
            autor = nome

            # cadastrando no txt
            with open("estoque_carros.txt", "a") as file:
                file.write(str({"Nome": nome_car, "Preco": preco, "Ano": ano, "Estado": estado, "Autor": autor})+"\n") #vai add no arquivo txt
            msg("Cadastrando...", 0.5)
            msg("Sucess!!", 1)

            # finalizar o loop while
            continuar = input("\u26A0 Você deseja continuar cadastrando carros ? (s/n) \u26A0 :")
            if(continuar == "n" or continuar == "não"):
                break

        main()

def dados_tratados_arquivo_carros():
    os.system("cls")
    carros = []
    with open("estoque_carros.txt", "r") as file:
        for i in file:
            carro = i.replace("'", '"')
            carro = json.loads(carro)
            carros.append(carro)
    return carros

def procurar(o_que_deseja_buscar):
    resultado_da_pesquisa = []
    carros = dados_tratados_arquivo_carros()

    nome_carro_usr = input(f"Digite o {o_que_deseja_buscar.lower()} do carro:")

    msg("Buscando", 1)
    # quero os dados tratados do arquivo txt
    for carro in carros:
        if(carro[o_que_deseja_buscar]==nome_carro_usr):
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
        if(len(resultado_da_pesquisa) > 1):
            print("\n")
        i+=1
    print("=======================================")
    
def buscar_carro():
    os.system("cls")
    while True:
        os.system("cls")
        #vai ficar o resultado das pesquisas

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
        if(opc_escolhida==0):
            procurar("Nome")

        # busca por preço
        elif(opc_escolhida==1):
            procurar("Preco")

        # busca por ano
        elif(opc_escolhida==2):
            procurar("Ano")

        # busca por estado
        elif(opc_escolhida==3):
            procurar("Estado")
        
        continuar = input("\u26A0 Você deseja continuar procurando carros ? (s/n) \u26A0 :")
        if(continuar == "n" or continuar == "não"):
            break
    main()


main()#PAREI AQUI 

#FALTA TRATAR OS ERROS 
