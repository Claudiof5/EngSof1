from datetime import datetime 
from comentario import Comentario
from sistema import Sistema

class Nota:
    def __init__(self, titulo:str, texto: str, noteId: str) -> None:
        self.titulo = self.titulo
        self.texto = self.texto
        self.noteId = noteId
        self.dataCriacao = datetime.now().strftime("%x")
        self.comentarios = []

    def comentar(self, userId:str, texto:str):
        novoComentario = Comentario(userId, texto, str(len(self.comentarios)))
        self.comentarios.append(novoComentario)