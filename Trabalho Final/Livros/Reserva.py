from dataclasses import dataclass
from datetime import datetime

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Livros.Livro import Livro  
    from Usuarios.iUsuario import iUsuario
    
class Reserva:
    
    def __init__(self, livro: 'Livro', usuario: 'iUsuario') -> None:
        self.livro: 'Livro' = livro  
        self.usuario: 'iUsuario' = usuario
        self.dataReserva = datetime.now().date()
    
    @property
    def titulo_livro(self) -> str:
        return self.livro.titulo
    
    @property
    def nome_usuario(self) -> str:
        return self.usuario.nome
    
    @property
    def codigo_identificador_livro(self) -> str:
        return self.livro.codigoIdentificador
    
    def get_informacoes_reserva(self) -> dict[str, str]:
        return {'titulo': self.titulo_livro, 'dataReserva': self.dataReserva}