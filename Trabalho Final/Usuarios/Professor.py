from Usuarios.iUsuario import *
from Usuarios.regrasEmprestimo.RegrasEmprestimoProfessor import RegrasEmprestimoProfessor
from Usuarios.regrasReserva.RegrasReservaPadrao import RegrasReservaPadrao
from Usuarios.observer.ObserverProfessor import ObserverProfessor

class Professor(iUsuario):

    diasDeEmprestimoMaximo = 7
    
    def __init__(self, nome: str, codigoIdentificador: int) -> None:
        super().__init__(nome, codigoIdentificador)
        self._regrasDeEmprestimo = RegrasEmprestimoProfessor()
        self._regrasDeReserva = RegrasReservaPadrao()
        self._observerProfessor = ObserverProfessor()

    @property
    def notificacoes(self):
        return self._observerProfessor._notificacoes
    
    @property
    def numero_de_notificacoes(self):
        return self._observerProfessor.numero_notificacoes

    
    def print_informacoes(self) -> None:
        
        self.print_numero_de_notificacoes()
        super().print_informacoes()

    def print_numero_de_notificacoes(self) -> None:
        print(f"Numero de notificações: {self.numero_de_notificacoes}")
