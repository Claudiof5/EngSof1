from dataclasses import dataclass
#from Livro import Livro


class Exemplar:

    def __init__(self, livro, codigoExemplar) -> None:
        self.livro = livro
        self.codigoExemplar: int = codigoExemplar
        self.disponivel: bool = True

    
    def get_livro(self) -> str:
        return self.livro
    
    def get_codigo_exemplar(self) -> int:
        return self.codigoExemplar

    def get_informacoes_exemplar(self) -> dict[str, str]:
        return {'disponivel': self.disponivel}