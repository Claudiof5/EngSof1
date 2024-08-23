from dataclasses import dataclass

from datetime import datetime
#from iUsuario import iUsuario
#from Livro import Livro

class Reserva:
    
    def __init__(self, livro , usuario) -> None:
        self.livro = livro
        self.usuario = usuario
        self.dataReserva = datetime.now().date()
        
    def get_nome_usuario(self) -> str:
        return self.usuario.nome
    
    def get_codigoIdentificador_livro(self) -> str:
        return self.livro.codigoIdentificador
    
    def print_reserva(self) -> None:
        print(f"Livro: {self.livro.titulo} Data: {self.dataReserva}")