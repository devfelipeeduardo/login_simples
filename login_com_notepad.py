import stdiomask
import string
from os import system

# Variáveis
login = ''
senha = ''
cadastros = ['admin', 'admin_senha']

def exibir_menu():
    while True:
        print("----------------------")
        print("| Escolha uma opção: |")
        print("| [1] Fazer Cadastro |")
        print("| [2] Fazer Login    |")
        print("| [3] Sair           |")
        print("----------------------\n")
        opcao = input("Opção: ")

        if opcao in ['1', '2', '3']:
            system('cls')
            return (opcao)
        else:
            print("Digite uma opção entre [1] ou [2] ou [3] ")
# Chama a função fazer login, onde o usuário insere o login e senha.

CARACTERES_PERMITIDOS = string.ascii_letters + string.digits + "_"

def validar_login(login):
    for caractere in login:
        if caractere not in CARACTERES_PERMITIDOS:
            return False
    return True

def fazer_login():
    while True:

        login = input("Login:")
        senha = stdiomask.getpass(prompt='Senha: ', mask='*')

        if not validar_login(login):
            print("Seu login não pode conter espaços ou caracteres especiais")
        else:
            return (login, senha)
        
        if login == senha:
            print('Sua senha deve ser diferente do login.')
            continue

            

# Chama a função buscar usuário, onde faz o tratamento para cadastrar o usuário. Caso o usuário não tenha cadastro
# ele é cadastrado. Se já houver, solicita uma nova senha.
# Caso não encontre o arquivo cadastros, ele emite um erro.

def buscar_usuario(login, senha):
    cadastros = ['admin', 'admin_senha']
    try:
        with open('cadastros.txt', 'r+', encoding = 'Utf-8', newline='') as arquivo:
            for linha in arquivo:
                linha = linha.strip(",")
                cadastros.append(linha.split())

            for cadastro in cadastros:
                login_digitado = cadastro[0]
                senha_digitada = cadastro[1]
                if login == login_digitado and senha == senha_digitada:
                    return True
    except FileNotFoundError:
        ...

while True:
    
    # Exibe o menu
    opcao = exibir_menu()

    # Tratamento de Opções
    if opcao == '1':
        print("FAZENDO CADASTRO...")
        login, senha = fazer_login()

        usuario = buscar_usuario(login, senha)

        if usuario == True:
            print("Usuário já existe.")

        else:
            with open('cadastros.txt', 'a+', encoding = 'Utf-8', newline='') as arquivo:
                arquivo.writelines(f'{login} {senha}\n')
                print("Cadastro aprovado")

    if opcao == '2':
        while True:
            print("FAZENDO LOGIN...")
            login, senha = fazer_login()

            usuario = buscar_usuario(login, senha)

            if usuario == True:
                print('Login realizado com sucesso!')
                login_concluido = True
            else:
                print(" Você deve ter digitado seu nome de usuário ou senha errado\n Por favor, verifique.")
                login_concluido = False
            
            if login_concluido == True:
                break


    if opcao == '3':
        print('Volte sempre!')
        exit()
        
    else:
        print('Volte sempre!')
        

