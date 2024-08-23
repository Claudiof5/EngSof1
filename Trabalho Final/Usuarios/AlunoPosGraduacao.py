from Usuarios.iAluno import *
from Usuarios.regrasEmprestimo.RegrasEmprestimoAlunoPosGraduacao import RegrasEmprestimoAlunoPosGraduacao
from Usuarios.regrasReserva.RegrasReservaPadrao import RegrasReservaPadrao

class AlunoPosGraduacao(iAluno):

    limiteDeLivrosMaximo = 4
    diasDeEmprestimoMaximo = 5
    
    def __init__(self, nome :str, codigoIdentificador:int) -> None:
        super().__init__(nome, codigoIdentificador)
        self._regrasDeEmprestimo = RegrasEmprestimoAlunoPosGraduacao()
        self._regrasDeReserva = RegrasReservaPadrao()
    


