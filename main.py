print("=-" * 20)
print("CLI de Controle de Biblioteca")
print("=-" * 20)

usuarios = []
emprestimos = []
livros = []

contagem_de_cadastro = 0
contagem_de_livro = 0
contagem_de_emprestimos = 0

def cadastrar_usuario(nome: str, cpf: int):
    global contagem_de_cadastro
    id_usuario = 1000 + contagem_de_cadastro
    contagem_de_cadastro += 1
    user = {
        "id_usuario":id_usuario,
        "nome":nome,
        "cpf":cpf}
    usuarios.append(user)
    print(f"Usuario cadastrado com sucesso!\n O usuario {nome}, recebeu o id: {id_usuario}.")

def validar_cpf(cpf):
    contar_cpf = str(cpf)
    if len(contar_cpf) != 11:
        return False
    else:
        return True

def cadastrar_livro(nome, genero, autor):
    global contagem_de_livro
    id_livro = 100000 + contagem_de_livro
    contagem_de_livro += 1
    livro = {
        "id_livro": id_livro,
        "nome": nome,
        "genero": genero,
        "autor": autor,
        "disponivel": True
    }
    livros.append(livro)
    return print(f"livro cadastrado com sucesso!\n O livro {nome} recebeu o id {id_livro}.")

def emprestar_livro(usuarios, livros, emprestimos, id_usuario, id_livro):
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
        if validar_cpf(cpf) == False:
            print('CPF inválido!')
        else:
            cadastrar_usuario(nome, cpf)

    elif operacao == 2:
        nome = input("Nome do livro: ")
        genero = str(input("Gênero do livro: "))
        autor = str(input("Autor do livro: "))
        cadastrar_livro(nome, genero, autor)

    elif operacao == 3:
        None

#testes 
    elif operacao == 10:
        user_id = str(input("user "))
        livro_id = str(input("user "))
        emprestar_livro(usuarios, livros, emprestimos, livro_id, user_id)
    else:
        print("Opção inválida, tente novamente")


print(usuarios)
print(livros)