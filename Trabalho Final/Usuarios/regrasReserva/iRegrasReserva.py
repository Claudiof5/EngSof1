from abc import ABC, abstractmethod
from Livros.Livro import Livro


class iRegrasReserva(ABC):
    
    @abstractmethod
    def apto_a_reserva(self, livro :Livro, user ) -> bool:
        pass


