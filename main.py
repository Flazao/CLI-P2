print("=-" * 20)
print("CLI de Controle de Biblioteca")
print("=-" * 20)

usuarios = []
livros = {}

contagem_de_cadastro = 0

def cadastrar_usuario(nome: str, cpf: int):
    global contagem_de_cadastro
    id_usuario = 1000 + contagem_de_cadastro
    contagem_de_cadastro += 1
    user = (id_usuario, nome, cpf)
    usuarios.append(user)
    return print("Usuário cadastrado com sucesso!")

def validar_cpf(cpf):
    contar_cpf = str(cpf)
    if len(contar_cpf) > 11 or len(contar_cpf) < 11:
        print('CPF inválido!')

def cadastrar_livro(nome, genero, autor, id_livro):
    return None

def emprestar_livro():
    return None

def devolver_livro():
    return None

def ver_historico_usuario():
    return None

print("\nOlá seja bem-vindo!")
print("Qual operação deseja realizar?")
print("1 para cadastrar usuario")
print("2 para cadastrar livro")
print("3 para emprestimo de livro")
print("4 para devolver livro")
print("5 para ver o Historico de Emprestimo")
print("6 para deletar livro")
print("7 para deletar usuario")
print("0 para finalizar\n")

while True:
    operacao = int(input("Insira a opção: "))

    if operacao == 0:
        break
    if operacao == 1:
        nome = str(input("Nome do usuário: "))
        cpf = int(input("CPF do usuário: "))
        validar_cpf(cpf)
        cadastrar_usuario(nome, cpf)

print(usuarios)