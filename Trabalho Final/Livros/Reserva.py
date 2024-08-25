from dataclasses import dataclass

from datetime import datetime
#from iUsuario import iUsuario
#from Livro import Livro

class Reserva:
    
    def __init__(self, livro , usuario) -> None:
        self.livro = livro
        self.usuario = usuario
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