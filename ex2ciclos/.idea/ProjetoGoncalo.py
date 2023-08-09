from ProjetoGoncaloClasse import Livro, Cliente, Estado, Biblioteca

cliente1 = Cliente("Tiago Pinto")
cliente2 = Cliente("Beatriz Charrua")
cliente3 = Cliente("Margarida Almeida")
cliente4 = Cliente("Gonçalo Feliciano")

biblioteca = Biblioteca([], [cliente1, cliente2, cliente3, cliente4])

biblioteca.adicionar_livro("League of Legends para NABOS", "Tiago Pinto")
biblioteca.adicionar_livro("Counter Strike para NOOBS", "Beatriz Charrua")
biblioteca.adicionar_livro("Como fotografar - Modulo para Totos", "Margarida Almeida")
biblioteca.adicionar_livro("Como fazer paezinhos de queijo", "Goncalo Feliciano")

biblioteca.consultar_livros()

biblioteca.editar_livro("Counter Strike para NOOBS", Estado.indisponivel)
biblioteca.consultar_livro("Counter Strike para NOOBS")

biblioteca.consultar_livro("Este livro e uma ilusao")

biblioteca.remover_livro("Counter Strike para NOOBS")
biblioteca.consultar_livros()

biblioteca.requisitar_livro("League of Legends para NABOS", cliente1)
biblioteca.mostrar_requisicoes_livro("League of Legends para NABOS")

biblioteca.consultar_livros()

biblioteca.fazer_pedido("Python para iniciantes", cliente4)
biblioteca.mostrar_pedidos_pendentes("Python para iniciantes")


