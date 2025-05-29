print("=-" * 20)
print("CLI de Controle de Biblioteca")
print("=-" * 20)

usuarios = []
livros = []
emprestimos = []

contagem_de_cadastro = 0
contagem_de_livro = 0
contagem_de_emprestimos = 0

def cadastrar_usuario(nome: str, cpf: int):
    global contagem_de_cadastro
    id_usuario = 1000 + contagem_de_cadastro
    contagem_de_cadastro += 1
    user = {
        "nome":nome,
        "id_usuario":id_usuario,
        "cpf":cpf}
    usuarios.append(user)
    print(f"Usuario cadastrado com sucesso!\n O usuario {nome}, recebeu o id: {id_usuario}.\n")

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
    return print(f"livro cadastrado com sucesso!\n O livro {nome} recebeu o id {id_livro}.\n")

def emprestar_livro(usuarios, livros, emprestimos, id_usuario, id_livro):
    return None

def devolver_livro():
    return None

def ver_historico_usuario():
    return None

def exibir_usuarios():
    if usuarios:
        for usuario in usuarios:
            for chave, valor in usuario.items():
                print(f'{chave}: {valor}')
            print(' ')
    else:
        print("Nenhum usuário foi cadastrado")


def exibir_livros():
    if livros:
        for livro in livros:
            for chave, valor in livro.items():
                print(f'{chave}: {valor}')
            print(' ')
    else:
        print('Nenhum livro foi cadastrado')


print("\nOlá seja bem-vindo!")
print("Qual operação deseja realizar?")
print("""
1 para cadastrar usuario
2 para cadastrar livro
3 para ver usuarios cadastrados
4 para ver livros cadastrados
5 para emprestimo de livro
6 para devolver livro
7 para ver o Historico de Emprestimo
8 para deletar usuario
9 para deletar livro
0 para finalizar
      """)

while True:
    operacao = int(input("\033[32mInsira a opção: \033[m"))
    print(' ')

    if operacao == 0:
        break
    
    elif operacao == 1:
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
        exibir_usuarios()

    elif operacao == 4:
        exibir_livros()

    elif operacao == 5:
        None

    elif operacao == 6:
        None

    elif operacao == 7:
        None    

    elif operacao == 8:
        None

    
#testes 
    elif operacao == 10:
        user_id = str(input("user "))
        livro_id = str(input("user "))
        emprestar_livro(usuarios, livros, emprestimos, livro_id, user_id)
    else:
        print("Opção inválida, tente novamente")