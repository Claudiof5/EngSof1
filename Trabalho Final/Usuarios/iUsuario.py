from abc import ABC, abstractmethod
from typing import List
from Livros.Emprestimo import Emprestimo
from Livros.Reserva import Reserva
from Livros.Livro import Livro
from Usuarios.regrasEmprestimo.iRegrasEmprestimo import iRegrasEmprestimo   
from Usuarios.regrasReserva.iRegrasReserva import iRegrasReserva   
from datetime import datetime, timedelta

class iUsuario(ABC):
    
    numeroReservasMaximo:int = 3
    diasDeEmprestimoMaximo: int
    def __init__(self, nome :str, codigoIdentificador:int) -> None:
        self._nome = nome
        self._codigoIdentificador = codigoIdentificador
        self._emprestimos :List[Emprestimo] = []
        self._reservas :List[Reserva] = []
        self._regrasDeEmprestimo:iRegrasEmprestimo
        self._regrasDeReserva: iRegrasReserva
    
    def reservar_livro(self, livro) -> None:
        pass
    

    def apto_a_emprestimo(self, livro :Livro ) -> bool:
        return self._regrasDeEmprestimo.apto_a_emprestimo( livro, self)

    def apto_a_reserva(self, livro :Livro) -> bool:
        return self._regrasDeReserva.apto_a_reserva(livro, self)
    
    def devolver_livro(self, livro) -> None:
        pass

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, value: str) -> None:
        self._nome = value

    @property
    def codigoIdentificador(self) -> int:
        return self._codigoIdentificador

    @property
    def emprestimos(self) -> List[Emprestimo]:
        return self._emprestimos
    
    def adiciona_emprestimo(self, emprestimo: Emprestimo) -> None:
        self._emprestimos.append(emprestimo)

    def find_emprestimo(self, livro: Livro) -> Emprestimo:
        for emprestimo in self._emprestimos:
            if emprestimo.livro == livro:
                return emprestimo
        return None
    @property
    def reservas(self) -> List[Reserva]:
        return self._reservas
    
    def adiciona_reserva(self, reserva: Reserva) -> None:
        self._reservas.append(reserva)
    
    def find_reserva(self, livro: Livro) -> Reserva:
        for reserva in self._reservas:
            if reserva.livro == livro:
                return reserva
        return None

    def esta_em_debito(self) -> bool:
        for emprestimo in self._emprestimos:
            if emprestimo.emCurso and datetime.now().date() > emprestimo.dataDeDevolucaoEsperada :
                return True
        return False

    def retira_reserva(self, reserva: Reserva) -> None:
        self._reservas.remove(reserva)

    def limite_de_reservas_atingido(self) -> bool:
        return self.numero_reservas() >= self.numeroReservasMaximo
    
    def numero_reservas(self) -> int:
        return len(self._reservas)
    
    def numero_emprestimos(self) -> int:
        return len(self._emprestimos)
    
    def emprestimos_ativos(self) -> List[Emprestimo]:
        return [ emprestimo for emprestimo in self._emprestimos if emprestimo.emCurso]
    
    def emprestimos_atrasados(self) -> List[Emprestimo]:
        return [ emprestimo for emprestimo in self._emprestimos if emprestimo.emCurso and datetime.now().date() > emprestimo.dataDeDevolucaoEsperada ]
    
    def emprestimos_concluidos(self) -> List[Emprestimo]:
        return [ emprestimo for emprestimo in self._emprestimos if not emprestimo.emCurso]

    #formato dicionário padrão de retorno consulta de usuario
    #dict = {nome: str, em_debito: bool, reservas: List[reservas], emprestimos:List[emprestimos], notificacoes:int}
    #reservas = {titulo: str, data: str}
    #emprestimos = {titulo: str, dataEmprestimo: str, dataDeDevolucaoEsperada: str, dataDevolucao: str, status: str}
    def retorna_informacoes(self) ->dict:
        nome = self._nome
        em_debito = self.esta_em_debito()
        reservas = self.retorna_informacoes_reservas()
        emprestimos = self.retorna_informacoes_emprestimos()
        
        retorno = {"nome": nome, "em_debito": em_debito, "reservas": reservas, "emprestimos": emprestimos}
        return retorno
        
    def retorna_informacoes_reservas(self) -> List[dict]:
        return {reserva.codigo_identificador_livro: reserva.get_informacoes_reserva() for reserva in self._reservas}
    
    def retorna_informacoes_emprestimos(self) -> List[dict]:
        return {emprestimo.codigoExemplar:emprestimo.get_informacoes_emprestimo() for emprestimo in self._emprestimos}