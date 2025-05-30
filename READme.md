# Gabriel Flazao - 1990590 
# Juliana Moreno - 1994729 
# Maria Fernanda de Andrade - 1998066

# Sistema de Controle de Biblioteca (CLI)

O Sistema de Controle de Biblioteca é uma aplicação desenvolvida em Python com o objetivo de simular o funcionamento básico de uma biblioteca real, permitindo ao usuário realizar tarefas de forma pratica e intuitiva. O sistema foi construído utilizando apenas recursos nativos da linguagem como a biblioteca collections, que é usada para manipular filas de forma eficiente. A proposta é fornecer uma ferramenta útil e simples, de fácil compreensão, além de nos ajudar com estudo de lógica e a prática com estruturas de dados.

A interface do sistema é baseada em linha de comando (CLI), o que torna a navegação simples, mesmo para quem tem pouca familiaridade com interfaces gráficas. Ao executar o programa, o usuário é guiado por um menu interativo que apresenta 10 opções disponíveis. Basta escolher a operação desejada e fornecer os dados solicitados para que o sistema processe e execute a ação correspondente. Entre as funcionalidades implementadas estão o cadastro de livros e usuários, a realização de empréstimos, o registro de devoluções, o cancelamento de cadastros, além da possibilidade de consultar os registros armazenados e gerenciar uma fila de espera para livros já emprestados.

Os dados são organizados internamente em dicionários e listas, o que permite relacionar informações de forma eficiente e modifica-los caso necessario. Por exemplo, ao emprestar um livro, o sistema associa o ID do livro ao ID do usuário que realizou o empréstimo, armazenando essas informações em uma lista de empréstimos ativos. Isso possibilita um controle estruturado das interações dentro da biblioteca, garantindo que o sistema possa identificar facilmente quem está com qual livro, quais livros estão disponíveis, e quem está aguardando por algum título específico. Além disso, o sistema mantém um histórico de ações, permitindo um rastreamento básico das operações realizadas durante a sessão além da possibilidade de apagar usuários e livros cadastrados.

# Funcionalidades principais do sistema

O sistema implementa funcionalidades essenciais para o gerenciamento básico de uma biblioteca. A seguir estão todas as funcionalidades disponíveis do sistema:

1- Cadastro de usuários.
2- Cadastro de livros.
3- Exibição de usuários cadastrados.
4- Exibição de livros cadastrados.
5- Empréstimo de livros.
6- Devolução de livros.
7- Exibição de histórico de ações.
8- Deleção de usuários.
9- Deleção de livros.
10- Controle de fila de espera para livros emprestados.

# Cadastro de usuários

O sistema permite o cadastro de novos usuários informando o nome e o CPF. Durante o processo de cadastro, é gerado automaticamente um ID exclusivo para o usuário com base em um contador interno. O ID começa a partir de 1000 e é incrementado de um a um a cada novo cadastro.

Antes de efetuar o cadastro, o CPF é validado com base no comprimento da string. O sistema espera que o CPF tenha exatamente 11 dígitos. Caso o valor informado não atenda a esse critério, o cadastro é recusado com uma mensagem apropriada.
Uma vez validado, o usuário é adicionado a uma lista chamada usuarios e o evento é registrado no histórico.

# Cadastro de livros

Semelhante ao cadastro de usuários, o cadastro de livros solicita três informações do usuário: nome do livro, gênero e autor.
Cada livro recebe um ID exclusivo automaticamente. Esse ID começa em 100000 e é incrementado com base em um contador específico para livros. Esse ID é utilizado posteriormente para localizar, emprestar e devolver livros.
Todos os livros são cadastrados como disponíveis por padrão. Essa disponibilidade muda conforme o livro é emprestado e devolvido.
O livro é então armazenado na lista livros e seu cadastro é adicionado ao histórico.

# Exibição de usuários cadastrados

O sistema possui uma funcionalidade que exibe todos os usuários cadastrados até o momento. Caso não existam usuários na lista, uma mensagem informando isso é exibida.
Cada usuário é impresso com todas as suas chaves e valores, incluindo nome, ID, CPF e a lista de empréstimos atuais.
Essa funcionalidade é útil para visualização e verificação de cadastros existentes.

# Exibição de livros cadastrados

O funcionamento é semelhante à exibição de usuários. A função percorre a lista de livros cadastrados e exibe todas as informações de cada livro individualmente.
São exibidos o nome, o ID, o autor, o gênero e se o livro está ou não disponível no momento.
Essa opção também é registrada no histórico como uma consulta.

# Empréstimo de livros

O sistema permite que um livro seja emprestado a um usuário cadastrado, desde que o livro esteja disponível.
Antes de efetuar o empréstimo, o sistema verifica se o ID do usuário e o ID do livro existem. Caso algum deles não seja encontrado, uma mensagem de erro é exibida.
Se o livro estiver disponível, ele é marcado como indisponível, o ID do livro é adicionado à lista de empréstimos do usuário, e o empréstimo é adicionado à lista global de emprestimos.
Esse evento também é registrado no histórico.
Caso o livro já esteja emprestado, o sistema oferece ao usuário a possibilidade de entrar em uma fila de espera.

# Fila de reservas

A fila é implementada usando a estrutura deque da biblioteca collections.
Cada fila é associada ao ID do livro e pode conter múltiplos usuários aguardando sua vez de realizar o empréstimo.
Quando um livro é devolvido, o próximo usuário da fila é automaticamente notificado e o sistema tenta emprestar o livro para ele.
Se o usuário já estiver na fila e tentar entrar novamente, o sistema informa que ele já está aguardando.

# Devolução de livros

Na devolução, o sistema primeiro verifica se o usuário e o livro informados existem.
Se o livro estiver disponível, o sistema entende que ele já foi devolvido anteriormente e informa o usuário.
Caso o livro esteja emprestado de fato, ele é marcado como disponível e removido da lista de empréstimos do usuário.
O empréstimo correspondente também é removido da lista global.
Após a devolução, o sistema verifica se há alguém na fila de espera para o livro. Se houver, o próximo da fila é chamado automaticamente.
O evento é então registrado no histórico de ações.

# Histórico de ações

O histórico é mantido ao longo da execução do programa e registra ações como cadastro de usuários, cadastro de livros, empréstimos, devoluções, consultas e deleções.
Ele é útil para rastrear as ações realizadas durante a sessão de uso do sistema, facilitando auditorias e controle interno.
O histórico é uma lista simples que armazena tuplas contendo uma breve descrição da ação, quem realizou e sobre o quê.

# Deleção de usuários

Um usuário só pode ser deletado se não tiver nenhum livro emprestado no momento.
Caso contrário, o sistema impede a remoção e exibe uma mensagem informando que existem livros em posse do usuário.
A verificação é feita com base na lista de empréstimos do próprio usuário.
Se estiver tudo certo, o usuário é removido da lista e o evento é registrado no histórico.

# Deleção de livros

A lógica para deletar livros segue a mesma ideia da deleção de usuários.
O sistema impede que livros atualmente emprestados sejam removidos. É necessário que o livro esteja marcado como disponível para que sua deleção seja efetuada.
Uma vez verificado que o livro pode ser removido, ele é excluído da lista livros e o evento é registrado no histórico.
Essa medida garante que não haja inconsistência de dados no sistema.

# Validações e mensagens

O sistema realiza diversas validações para garantir que as ações feitas pelo usuário sejam válidas, entre as validações estão:

Verificação de número de dígitos do CPF (esperado: 11).
Verificação de número de caracteres do ID do usuário (esperado: 4 dígitos).
Verificação de número de caracteres do ID do livro (esperado: 6 dígitos).
Confirmação de que o usuário e o livro existem antes de efetuar operações como empréstimos ou devoluções.
Mensagens de feedback são exibidas ao usuário sempre que uma ação é realizada ou impedida.
Essas mensagens ajudam na usabilidade e compreensão do sistema.

# Interface de linha de comando (CLI)

O sistema funciona inteiramente no terminal, através de interações com o usuário por meio da função input().
O menu principal exibe as opções disponíveis e o usuário pode digitar o número da operação desejada.
As entradas são interpretadas como inteiros e o sistema realiza a ação correspondente.
O loop principal permanece em execução até que o usuário selecione a opção de finalizar (opção 0).

# Consideração final

Este projeto foi criado com base em uma atividade, sendo uma base para sistemas mais complexos, esta estrutura é uma introdução prática à manipulação de listas, filas (FIFO), dicionários, tuplas e à organização lógica de dados em Python. Ao unir teoria e prática em um código funcional, o sistema ofereceu uma forma de reforçar conceitos vistos dentro da sala de aula, além de oferecer um jeito de entender de fato como as estruturas de dados se comportam na prática.
Durante o desenvolvimento, foi possível perceber que mesmo funcionalidades simples, como o cadastro de um usuário ou a devolução de um livro, exigem uma lógica bem  e de certa forma complexa para evitar falhas ou dados errados. O desafio de pensar nos conexões entre dados, nas validações e na comunicação com o usuário foi uma forma de nos ajudar a entender mais sobre a estrutura e funcionamento dos dados.