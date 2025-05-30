from collections import deque

print("=-" * 20)
print("CLI de Controle de Biblioteca")
print("=-" * 20)

usuarios = []
livros = []
emprestimos = []
reservas = []
historico = []

contagem_de_cadastro = 0
contagem_de_livro = 0

def cadastrar_usuario(nome: str, cpf: int):
    global contagem_de_cadastro
    id_usuario = 1000 + contagem_de_cadastro
    contagem_de_cadastro += 1
    user = {
        "nome": nome,
        "id_usuario": id_usuario,
        "cpf": cpf,
        "emprestimos": []
    }
    usuarios.append(user)
    historico.append((f"Cadastro de usuário, {nome} recebeu o id {id_usuario}"))
    print(f"Usuário cadastrado com sucesso!\n O usuário {nome}, recebeu o id: {id_usuario}.\n")

def validar_cpf(cpf: int):
    contar_cpf = str(cpf)
    if len(contar_cpf) != 11:
        return False
    else:
        return True

def cadastrar_livro(nome: str, genero: str, autor: str):
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
    historico.append(f"Cadastro de livro,o livro {nome} recebeu o id {id_livro}")
    print(f"livro cadastrado com sucesso!\n O livro {nome} recebeu o id {id_livro}.\n")

def buscar_fila(id_livro: int):
    for reserva in reservas:
        if reserva["id_livro"] == id_livro:
            return reserva
        
def adicionar_na_fila(id_livro: int, id_usuario: int):
    reserva = buscar_fila(id_livro)

    if reserva:
        if id_usuario in reserva["fila"]:
            print(f"este usuário já está na fila de reserva deste livro.\n")
        else:
            reserva["fila"].append(id_usuario)
            print(f"este usuário foi adicionado à fila de reserva.\n")
    else:
        reservas.append({"id_livro": id_livro, "fila": deque([id_usuario])})
        print(f"este usuário foi adicionado à fila de reserva.\n")

def liberar_proximo_da_fila(id_livro: int):
    reserva = buscar_fila(id_livro)
    if reserva and len(reserva["fila"]) > 0:
        proximo_usuario = reserva["fila"].popleft()
        print(f"O próximo da fila (ID usuário: {proximo_usuario}) pode pegar o livro agora.")
        return proximo_usuario

def emprestar_livro(usuarios: list, livros: list, emprestimos: list, id_usuario: int, id_livro: int):
    usuario_encontrado = None 
    for usuario in usuarios:
        if usuario["id_usuario"] == id_usuario:
            usuario_encontrado = usuario
            break

    if usuario_encontrado is None:
        print(f"O usuário com o ID {id_usuario} não foi encontrado.")
        return

    livro_encontrado = None 
    for livro in livros:
        if livro["id_livro"] == id_livro:
            livro_encontrado = livro 
            break

    if livro_encontrado is None:
        print(f"O livro com ID {id_livro} não encontrado.")
        return

    if livro_encontrado["disponivel"] == False:
        adicionar_na_fila(id_livro, id_usuario)
        return

    livro_encontrado["disponivel"] = False

    usuario_encontrado["emprestimos"].append(id_livro)
    emprestimos.append({
        "id_usuario": id_usuario,
        "id_livro": id_livro
    })

    historico.append(f"Empréstimo de livro, livro '{livro_encontrado['nome']}' para {usuario_encontrado['nome']}")
    print(f"O livro '{livro_encontrado['nome']}' foi emprestado para {usuario_encontrado['nome']}\n")

def devolver_livro(usuarios: list, livros: list, emprestimos: list, id_usuario: int, id_livro: int):
    usuario_encontrado = None 
    for usuario in usuarios:
        if usuario["id_usuario"] == id_usuario:
            usuario_encontrado = usuario
            break

    if usuario_encontrado is None:
        print(f"O usuário com o ID {id_usuario} não foi encontrado.")
        return

    livro_encontrado = None 
    for livro in livros:
        if livro["id_livro"] == id_livro:
            livro_encontrado = livro 
            break

    if livro_encontrado is None:
        print(f"O livro com ID {id_livro} não encontrado.")
        return
    
    if livro_encontrado['disponivel']:
        print(f"O livro {livro_encontrado['nome']} está disponivel")
        return

    livro_encontrado['disponivel'] = True

    if id_livro in usuario_encontrado["emprestimos"]:
        usuario_encontrado["emprestimos"].remove(id_livro)

    for emprestimo in emprestimos:
        if emprestimo["id_usuario"] == id_usuario and emprestimo["id_livro"] == id_livro:
            emprestimos.remove(emprestimo)
            break

    historico.append(f"Devolução de livro, {usuario_encontrado['nome']} devolveu '{livro_encontrado['nome']}'.")
    print(f'O usuário {usuario_encontrado["nome"]} devolveu o livro {livro_encontrado["nome"]}!\n')

    proximo = liberar_proximo_da_fila(id_livro)
    if proximo:
        emprestar_livro(usuarios, livros, emprestimos, proximo, id_livro)

def exibir_usuarios():
    historico.append(f"Consulta de usuarios cadastrados")
    if usuarios:
        for usuario in usuarios:
            for chave, valor in usuario.items():
                print(f'{chave}: {valor}')
            print(' ')
    else:
        print("Nenhum usuário foi cadastrado")

def exibir_livros():
    historico.append(f"Consulta de livros cadastrados")
    if livros:
        for livro in livros:
            for chave, valor in livro.items():
                print(f'{chave}: {valor}')
            print(' ')
    else:
        print('Nenhum livro foi cadastrado')

def deletar_usuario(usuarios: list, id_usuario: int):
    encontrado = False 

    for usuario in usuarios:
        if usuario["id_usuario"] == id_usuario:
            encontrado = True 
            if usuario["emprestimos"]:
                print(f"O usuário '{usuario['nome']}' não pode ser removido, pois possui livros emprestados.")
                return 
            usuarios.remove(usuario)
            historico.append(f"Usuário '{usuario['nome']}' deletado.")
            print(f"Usuário '{usuario['nome']}' foi deletado com sucesso.")

    if encontrado == False:
        print(f"Usuário com o ID {id_usuario} não encontrado.")

def deletar_livro(livros: list, id_livro: int):
    encontrado = False

    for livro in livros:
        if livro["id_livro"] == id_livro:
            encontrado = True
            if livro['disponivel'] == False:
                print(f"O livro '{livro['nome']}' não pode ser removido, pois está emprestado.")
                return
            livros.remove(livro)
            historico.append(f"Livro '{livro['nome']}' deletado.")
            print(f"Livro '{livro['nome']}' foi deletado com sucesso.")

    if encontrado == False:
        print(f"Livro com o ID {id_livro} não encontrado.")

print("\nOlá seja bem-vindo!")
print("Qual operação deseja realizar?")
print("""
1 para cadastrar usuario
2 para cadastrar livro
3 para ver usuários cadastrados
4 para ver livros cadastrados
5 para emprestimo de livro
6 para devolver livro
7 para ver o Historico de Emprestimo
8 para deletar usuário
9 para deletar livro
0 para finalizar
      """)

while True:
    operacao = int(input("\033[32mInsira a opção: \033[m"))
    print(' ')

    if operacao == 0:
        print("-=" * 20, "\n")
        break
    
    elif operacao == 1:
        nome = str(input("Nome do usuário: "))
        cpf = int(input("CPF do usuário: "))
        if validar_cpf(cpf) == False:
            print('CPF inválido!\n')
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
        id_usuario = int(input("Digite o ID do usuário: "))
        id_livro = int(input("Digite o ID do livro: "))
        emprestar_livro(usuarios, livros, emprestimos, id_usuario, id_livro)
        
    elif operacao == 6:
        id_usuario = int(input("Digite o ID do usuário: "))
        id_livro = int(input("Digite o ID do livro: "))
        devolver_livro(usuarios, livros, emprestimos, id_usuario, id_livro)

    elif operacao == 7:
        print(historico)  

    elif operacao == 8:
        id_usuario = int(input("Insira o ID do usuário que deseja deletar:"))
        if len(str(id_usuario)) != 4:
            print(f'ID do usuario errado, Esperado 4 Caracteres não {len(str(id_usuario))}')
        else:
            deletar_usuario(usuarios, id_usuario)

    elif operacao == 9:
        id_livro = int(input("Insira o ID do livro que deseja deletar: "))
        if len(str(id_livro)) != 6:
            print(f'ID do livro errado, Esperado 6 Caracteres não {len(str(id_livro))}')
        else:
            deletar_livro(livros, id_livro)

    else:
        print("Digite uma operação valida\n")
