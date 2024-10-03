from dataclasses import dataclass
from datetime import datetime, timedelta

from Livros.Exemplar import Exemplar
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Usuarios.iUsuario import iUsuario
    from Livros.Livro import Livro
class Emprestimo:

    def __init__(self, exemplar: Exemplar, usuario: 'iUsuario') -> None:
        self.exemplar: Exemplar = exemplar
        self.usuario: 'iUsuario' = usuario
        self.dataEmprestimo = datetime.now().date()
        self.dataDeDevolucaoEsperada = self.dataEmprestimo + timedelta(usuario.diasDeEmprestimoMaximo )
        self.dataDeDevolucao = None
        self.emCurso = True

    @property
    def livro(self) -> 'Livro':
        return self.exemplar.get_livro()
    @property
    def nomeUsuario(self) -> str:
        return self.usuario.nome
    @property
    def codigoExemplar(self) -> int:
        return self.exemplar.codigoExemplar
    @property
    def titulo(self) -> str:
        return self.exemplar.get_livro().titulo
    
    def get_informacoes_emprestimo(self) -> dict[str, str]:

        status = self.get_status()
        return {'nomeUsuario':self.nomeUsuario, 'titulo': self.titulo, 'dataEmprestimo': self.dataEmprestimo, 
                'dataDeDevolucaoEsperada': self.dataDeDevolucaoEsperada,'dataDeDevolucao': self.dataDeDevolucao, 'status': status}
    
    def get_status(self) -> str:
        if self.emCurso:
            if datetime.now().date() > self.dataDeDevolucaoEsperada:
                return "Em Atraso"
            else:
                return "Em Curso"
        else:
            return "Finalizado"