# sistema-concessionaria
#[AINDA SE ENCONTRA EM DESENVOLVIMENTO]
# Sistema de Gerenciamento de Concessionária

Este é um sistema básico em Python para gerenciamento de concessionárias, que permite cadastrar usuários, registrar carros, buscar informações e realizar outras operações simples.

## Funcionalidades

1. **Login e Cadastro de Usuário:**
   - Registrar um nome de usuário e salvar em um arquivo (`login_db.txt`).
   - Opção de usar o sistema como "Guest" (sem registro).
   - Exclusão de contas de usuário.

2. **Gerenciamento de Carros:**
   - Cadastrar carros com informações como nome, preço, ano e estado.
   - Buscar carros por:
     - Nome
     - Preço
     - Ano
     - Estado
   - Salvar e ler dados de carros de um arquivo (`estoque_carros.txt`).

3. **Interface Simples:**
   - Menus de texto organizados com emojis para facilitar a navegação.
   - Feedback ao usuário para ações realizadas (como cadastro e busca).

## Requisitos

- Python 3.x
- Módulos padrão do Python:
  - `os` (limpeza da tela)
  - `time` (delays para exibição)
  - `sys` (encerramento do programa)
  - `json` (manipulação de arquivos em formato JSON)

## Arquitetura do Sistema

- **Arquivos utilizados:**
  - `login_db.txt`: Armazena dados do usuário.
  - `estoque_carros.txt`: Armazena dados dos carros cadastrados.

- **Principais funções:**
  - `main()`: Ponto de entrada do sistema.
  - `login()`: Gerencia o acesso ao sistema.
  - `registrar_user()`: Registra novos usuários.
  - `menu(nome)`: Exibe o menu principal.
  - `cadastrar_carro(nome)`: Cadastra novos carros.
  - `buscar_carro()`: Realiza buscas por critérios especificados.
  - `msg(msg, temp)`: Exibe mensagens com delays.
  - `dados_tratados_arquivo_carros()`: Lê e trata dados do arquivo de carros.
  - `procurar(o_que_deseja_buscar)`: Realiza pesquisas no estoque.

## Uso

1. Clone ou baixe o código.
