from dataclasses import dataclass
from Livros.Exemplar import Exemplar
#from iUsuario import iUsuario
from datetime import datetime, timedelta

class Emprestimo:

    def __init__(self, exemplar: Exemplar, usuario) -> None:
        self.exemplar = exemplar
        self.usuario = usuario
        self.dataEmprestimo = datetime.now().date()
        self.dataDeDevolucaoEsperada = self.dataEmprestimo + timedelta(usuario.diasDeEmprestimoMaximo )
        self.dataDeDevolucao = None
        self.emCurso = True

    @property
    def livro(self) -> str:
        return self.exemplar.get_livro()
    @property
    def nomeUsuario(self) -> str:
        return self.usuario.nome
    @property
    def codigoExemplar(self) -> int:
        return self.exemplar.codigoExemplar

    def print_emprestimo(self) -> None:
        if self.emCurso:
            if datetime.now().date() > self.dataDeDevolucaoEsperada:
                status = "Em Atraso"
            else:
                status = "Em Curso"
            print(f"\t-Livro: {self.exemplar.get_livro().titulo} \n\tData de Emprestimo: {self.dataEmprestimo} Data de Devolução Esperada: {self.dataDeDevolucaoEsperada}\n\tStatus: {status}\n")
        else:
            print(f"\t-Livro: {self.exemplar.get_livro().titulo} \n\tData de Emprestimo: {self.dataEmprestimo} Data de Devolução: {self.dataDeDevolucao}\n\tStatus: Finalizado")