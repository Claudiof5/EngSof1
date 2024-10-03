from dataclasses import dataclass
#from Livro import Livro

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Livros.Livro import Livro

class Exemplar:

    def __init__(self, livro: 'Livro', codigoExemplar: int) -> None:
        self.livro: 'Livro' = livro
        self.codigoExemplar: int = codigoExemplar
        self.disponivel: bool = True

    
    def get_livro(self) -> 'Livro':
        return self.livro
    
    def get_codigo_exemplar(self) -> int:
        return self.codigoExemplar

    def get_informacoes_exemplar(self) -> dict[str, str]:
        return {'disponivel': self.disponivel}