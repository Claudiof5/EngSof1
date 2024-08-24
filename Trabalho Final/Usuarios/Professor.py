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

    
    def retorna_informacoes(self) -> None:
        
        retorno = super().retorna_informacoes()
        retorno["numero_notificacoes"] = self.numero_de_notificacoes
        return retorno

    def retorna_numero_de_notificacoes(self) -> None:
        retorno = {"numero_notificacoes": self.numero_de_notificacoes, "nome": self.nome}
        return retorno
