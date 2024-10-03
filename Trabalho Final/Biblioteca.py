from typing import List
from Livros.Livro import Livro
from Usuarios.iUsuario import iUsuario
from Usuarios.Professor import Professor
from Usuarios.enumUsuarios import enumUsuarios

from Livros.Reserva import Reserva 
from Livros.Emprestimo import Emprestimo

from datetime import datetime

class Biblioteca:
    
    instancia = None
    def __init__(self):
        self._livros: List[Livro] = []
        self._usuarios: List[iUsuario] = []
        self._datetime: datetime = datetime

    def get_instance() -> 'Biblioteca':
        if not Biblioteca.instancia:
            Biblioteca.instancia = Biblioteca()
        return Biblioteca.instancia
    
#Encontra Usuários e Livros

    def find_user(self, codigoIdentificador: str) -> iUsuario:
        
        for usuario in self._usuarios:
            if usuario.codigoIdentificador == codigoIdentificador:
                return usuario
        return None
    
    def find_book(self, codigoIdentificador: str) -> Livro:
        for livro in self._livros:
            if livro.codigoIdentificador == codigoIdentificador:
                return livro
        return None
    
#Cadastros livro, exemplar e usuario

    def cadastrar_livro(self, codigoIdentificador: str, titulo: str, autores: str, editora: str, edicao: str, ano: str):
        livro = Livro(codigoIdentificador, titulo, autores, editora, edicao, ano)
        self._livros.append(livro)

    def cadastrar_exemplar(self, codigoLivro: str, codigoExemplar: str) -> bool:
        livro = self.find_book(codigoLivro)
        if livro:
            livro.cadastrar_exemplar(codigoExemplar)
            return True
        return False

    def cadastrar_usuario(self, codigoIdentificador: str, nome: str, classe:str) -> bool:
        for tipoUsuario in enumUsuarios:
            if tipoUsuario.name == classe:
                usuario:iUsuario = tipoUsuario.value(nome, codigoIdentificador)
                self._usuarios.append(usuario)
                return True
        return False
    

