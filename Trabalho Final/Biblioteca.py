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
        self._reservas: List[Reserva] = []
        self._emprestados: List[Emprestimo] = []


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


#Retorna Informações Usuario, Livro e Notificações professor

    def retorna_informacoes_usuarios(self, codigoUsuario: int):
        usuario = self.find_user(codigoUsuario)
        if usuario:
            return usuario.retorna_informacoes()
        else:
            print(self._usuarios[0].codigoIdentificador)
            raise ValueError(f'Usuário correspondente ao codigo {codigoUsuario} não encontrado')
    
    def retorna_informacoes_livro(self, codigoLivro: int):
        livro = self.find_book(codigoLivro)
        if livro:
            return livro.retorna_informacoes()
        else:
            raise ValueError(f'Livro correspondente ao codigo {codigoLivro} não encontrado')

    def retorna_informacoes_notificacoes_professor(self, codigoUsuario: int):
        usuario: None | Professor = self.find_user(codigoUsuario)
        if usuario:
            return usuario.retorna_numero_de_notificacoes()
        else:
            raise ValueError(f'Usuário correspondente ao codigo {codigoUsuario} não encontrado')

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
    

#Emprestimo, Devolução, Reserva e Inscreve professor à livro

    def emprestar_livro(self, codigoUsuario: str, codigoLivro: str) -> dict:
        usuario = self.find_user(codigoUsuario)
        livro = self.find_book(codigoLivro)

        if not usuario:
            raise ValueError(f'Usuário correspondente ao codigo {codigoUsuario} não encontrado')
            return False
        
        if not livro:
            raise ValueError(f'Livro correspondente ao codigo {codigoLivro} não encontrado')
            return False
        
        if not usuario.apto_a_emprestimo(livro):
            #usuario não apto a emprestimo
            return False
        
        exemplar = livro.retorna_exemplar_disponivel_para_emprestimo()
        emprestimo :Emprestimo = Emprestimo( exemplar, usuario)
    
        reserva: Reserva = usuario.find_reserva(livro)
        if reserva:
            usuario.retira_reserva(reserva)
            livro.remove_reserva(reserva)

        usuario.adiciona_emprestimo(emprestimo)
        livro.adiciona_emprestimo(emprestimo)
        self._emprestados.append(emprestimo)

        
        #Interface.emprestimo_realizado(emprestimo.dataDeDevolucaoEsperada)
        retorno = {"nomeUsuario": usuario.nome, "nomeLivro": livro.titulo, "dataDeDevolucaoEsperada": emprestimo.dataDeDevolucaoEsperada, "dataDevolucao": None}
        return retorno

    def devolver_livro(self, codigoUsuario, codigoLivro):
        usuario = self.find_user(codigoUsuario)
        livro = self.find_book(codigoLivro)
        if not usuario:
            raise ValueError(f'Usuário correspondente ao codigo {codigoUsuario} não encontrado')
            
        
        if not livro:
            raise ValueError(f'Livro correspondente ao codigo {codigoLivro} não encontrado')
            
        
        emprestimo = usuario.find_emprestimo(livro)
        if not emprestimo:
            raise ValueError(f'Usuário não possui emprestimo do livro correspondente ao codigo {codigoLivro}')
            
        
        emprestimo.emCurso = False
        emprestimo.dataDeDevolucao = datetime.now().date()
        retorno = {"nomeUsuario": usuario.nome, "nomeLivro": livro.titulo, "dataDeDevolucaoEsperada": emprestimo.dataDeDevolucaoEsperada, "dataDevolucao": emprestimo.dataDeDevolucao}
        return retorno
    
    def reservar_livro(self, codigoUsuario, codigoLivro):
        usuario = self.find_user(codigoUsuario)
        livro = self.find_book(codigoLivro)

        if not usuario:
            raise ValueError(f'Usuário correspondente ao codigo {codigoUsuario} não encontrado')
            
        
        if not livro:
            raise ValueError(f'Livro correspondente ao codigo {codigoLivro} não encontrado')
        
        if not usuario.apto_a_reserva(livro):
            return False
        
        reserva = Reserva(livro, usuario)
        usuario.adiciona_reserva(reserva)
        livro.adiciona_reserva(reserva)
        self._reservas.append(reserva)
        retorno = {"nomeUsuario": usuario.nome, "nomeLivro": livro.titulo, "dataDeDevolucaoEsperada": None, "dataDevolucao": None}
        return retorno
    
    def inscreve_professor_a_livro(self, codigoUsuario, codigoLivro):
        usuario: None | Professor = self.find_user(codigoUsuario)
        livro:   None | Livro     = self.find_book(codigoLivro)

        if not usuario:
            raise ValueError(f'Usuário correspondente ao codigo {codigoUsuario} não encontrado')
        
        if not livro:
            
            raise ValueError(f'Livro correspondente ao codigo {codigoLivro} não encontrado')
        
        observador = usuario._observerProfessor
        livro.inscreve_observador_a_livro(observador)
        retorno = {"nomeUsuario": usuario.nome, "nomeLivro": livro.titulo, "dataDeDevolucaoEsperada": None, "dataDevolucao": None}
        return retorno
    
