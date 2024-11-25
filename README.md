# 🚗 Sistema de Gerenciamento de Carros

Um sistema simples em Python para **cadastrar** e **buscar carros**, armazenando os dados localmente em um arquivo. Ideal para quem deseja aprender ou explorar conceitos básicos de manipulação de arquivos, menus interativos e validações em Python.

---

## 🛠️ Funcionalidades

### 📋 Menu Principal
- [0] **Cadastrar Carro**: Permite adicionar informações de novos carros ao sistema.
- [1] **Buscar Carro**: Realiza a busca de carros cadastrados com base em diferentes critérios.
- [2] **Sair**: Encerra o programa.

### 🚗 Cadastro de Carros
- Armazena os seguintes dados:
  - **Nome** do carro.
  - **Preço** do carro.
  - **Ano** de fabricação.
  - **Estado** (novo, usado, etc.).
- Os dados são salvos no arquivo `estoque_carros.txt`.

### 🔍 Busca de Carros
- Critérios de busca disponíveis:
  - Nome.
  - Preço.
  - Ano.
  - Estado.
- Mostra os resultados encontrados de forma organizada.

---

## 🖥️ Requisitos

- **Python 3.x** instalado na máquina.
- Funciona apenas com bibliotecas nativas do Python:
  - `os`: Para limpeza de tela.
  - `time`: Para atrasos controlados (sleep).
  - `sys`: Para encerrar o programa.

---

## 🚀 Como Usar

### 1️⃣ Executando o Programa
1. Clone o repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/sistema-carros.git

### 📂 Estrutura do Projeto

sistema-carros/
├── sistema_carros.py   # Arquivo principal do sistema.
├── estoque_carros.txt  # Arquivo onde os carros cadastrados são armazenados.
