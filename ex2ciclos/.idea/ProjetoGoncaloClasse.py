from dataclasses import dataclass
from enum import Enum

class Estado(Enum):
    disponivel = 1
    requisitado = 2
    indisponivel = 3
    def __str__(self):
        return self.name

@dataclass
class Livro:
    titulo: str
    autor: str
    estado: Estado

@dataclass
class Cliente:
    nome: str

@dataclass
class Requisicao:
    nome_cliente: str
    titulo_livro: str

class Biblioteca:
    def __init__(self, livros, clientes):
        self.livros = livros
        self.clientes = clientes
        self.historico_requisicoes = []
        self.requisicoes_pendentes = []

    def adicionar_livro(self, titulo, autor):
        livro = Livro(titulo, autor, Estado.disponivel)
        self.livros.append(livro)

    def consultar_livros(self):
        for livro in self.livros:
            self.print_livro(livro)

    def consultar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                self.print_livro(livro)
                return
        print('Livro Indisponível\n')

    def editar_livro(self, titulo, novo_estado):
        for livro in self.livros:
            if livro.titulo == titulo:
                livro.estado = novo_estado
                break

    def remover_livro(self, titulo):
        self.livros = [livro for livro in self.livros if livro.titulo != titulo]

    def requisitar_livro(self, titulo, cliente):
        for livro in self.livros:
            if livro.titulo == titulo and livro.estado == Estado.disponivel:
                livro.estado = Estado.requisitado
                self.historico_requisicoes.append(Requisicao(cliente.nome, titulo))
                break

    def mostrar_requisicoes_livro(self, titulo):
        print(f'Clientes que requisitaram o livro "{titulo}" :\n')
        for historico_livro in self.historico_requisicoes:
            print(historico_livro.nome_cliente, '\n')

    def fazer_pedido(self, titulo, cliente):
        livros_existentes = [livro.titulo for livro in self.livros]
        if titulo in livros_existentes:
            self.requisitar_livro(titulo, cliente)
        else:
            self.requisicoes_pendentes.append(Requisicao(cliente.nome, titulo))

    def mostrar_pedidos_pendentes(self, titulo):
        print(f'Clientes que querem requisitar o livro "{titulo}" :\n')
        for requisicao in self.requisicoes_pendentes:
            if requisicao.titulo_livro == titulo:
                print(requisicao.nome_cliente)

    def print_livro(self, livro):
        print(f'Titulo: {livro.titulo} - Autor: {livro.autor} - Estado: {livro.estado}\n')