from datetime import datetime 
from typing import List
from .nota import Nota
from .sistema import Sistema

class Blog:
    def __init__(self, titulo: str, donoId:str, blogId: str) -> None:
        self.titulo          : str        = titulo
        self.dataCriacao     : str        = datetime.now().strftime("%x")
        self.notes           : List[Nota] = []
        self.numNotasCriadas : int        = 0
        self.blogId          : str        = blogId


    def createNota(self, userId : str, titulo : str, texto : str ) -> str:
        if self.checaPermissao(userId):
            novaNota = Nota(titulo, texto, self.blogId + "-" + str(self.numNotasCriadas))
            self.numNotasCriadas += 1
            self.notes.append(novaNota)
            return novaNota.noteId
        
    def deletaNota(self, userId : str, noteId : str):
        if self.checaPermissao(userId):        
            nota = self.getNotaById(noteId)
            self.notes.remove(nota)


    def checaPermissao(self, userId : str ) -> bool:
        if userId == self.blogId.split("-")[0]:
            return True
        else:
            return False
        
    def getNotaById( self, noteId : str ) -> Nota:

        for note in self.notes:
            if note.noteId == noteId:
                return note
            