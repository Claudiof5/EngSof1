from datetime import datetime 
from .comentario import Comentario
#from sistema import Sistema
from typing import List

class Nota:
    def __init__(self, titulo:str, texto: str, noteId: str) -> None:
        self.titulo      : str              = titulo
        self.texto       : str              = texto
        self.noteId      : str              = noteId
        self.dataCriacao : str              = datetime.now().strftime("%x")
        self.comentarios : List[Comentario] = []

    def createComentario(self, userId:str, texto:str):
        
        novoComentario = Comentario(userId, texto, self.noteId + "-" + str(len(self.comentarios)))
        self.comentarios.append(novoComentario)


    def getComentarioById(self, comentarioId : str) -> Comentario:
        for comentario in self.comentarios:
            if comentario.comentarioId == comentarioId:
                return comentario
            
    def printNota(self):
        print(f"id da nota: {self.noteId}".center(80))
        print(f"~~-=-{self.titulo}-=-~~".center(80))
        print(f" {self.texto}".center(80))
    
    def checaNotaAFundo(self):
        self.printNota()    
        for comentario in self.comentarios:
            comentario.printaComentario()