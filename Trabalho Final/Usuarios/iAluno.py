from Usuarios.iUsuario import *
from Usuarios.regrasEmprestimo.RegrasEmprestimoAluno import RegrasEmprestimoAluno
from Usuarios.regrasReserva.RegrasReservaPadrao import RegrasReservaPadrao

class iAluno(iUsuario):

    limiteDeLivrosMaximo: int
    diasDeEmprestimoMaximo: int
    
    def __init__(self, nome: str, codigoIdentificador: int) -> None:
        super().__init__(nome, codigoIdentificador)
        self._regrasDeEmprestimo = RegrasEmprestimoAluno()
        self._regrasDeReserva = RegrasReservaPadrao()
        
    def limite_de_livros_alcancado(self) -> bool:
        return self.numero_emprestimos() >= self.limiteDeLivrosMaximo
    