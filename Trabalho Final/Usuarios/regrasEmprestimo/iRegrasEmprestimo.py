from abc import ABC, abstractmethod 
from Livros.Livro import Livro


class iRegrasEmprestimo(ABC):
    
    @abstractmethod
    def apto_a_emprestimo(self, livro :Livro, user ) -> bool:
        pass




