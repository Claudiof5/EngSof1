from Usuarios.iAluno import *
from Usuarios.regrasEmprestimo.RegrasEmprestimoAlunoGraduacao import RegrasEmprestimoAlunoGraduacao
from Usuarios.regrasReserva.RegrasReservaPadrao import RegrasReservaPadrao

class AlunoGraduacao(iAluno):

    limiteDeLivrosMaximo = 3
    diasDeEmprestimoMaximo = 3
    
    def __init__(self, nome :str, codigoIdentificador:int) -> None:
        super().__init__(nome, codigoIdentificador)
        self._regrasDeEmprestimo = RegrasEmprestimoAlunoGraduacao()
        self._regrasDeReserva = RegrasReservaPadrao()
    


