#from sistema import Sistema
from typing import List, Dict

class User:
    
    def __init__(self, email: str, userId : str) -> None:
        self.email              : str = email
        self.userId             : str = userId
        self.comentariosCriados : List[str] = []
        self.notasCriadas       : List[str] = []
        self.blogsCriados       : List[str] = []

    def createBlog(self, titulo):
        blogId = Sistema.createBlog(self.userId, titulo)
        self.blogsCriados.append(blogId)

    def createNota(self, blogId, titulo, texto):
        notaId = Sistema.createNota(self.userId, blogId, titulo, texto)
        self.notasCriadas.append(notaId)

    def createComentario(self, noteId, texto):
        comentarioId = Sistema.createComentario(self.userId, noteId, texto)
        self.comentariosCriados.append(comentarioId)

    def deleteNota(self, noteId):
        Sistema.deleteNota(self.userId, noteId)
        self.notasCriadas.delete(noteId)

    def printAllBlogsCriados(self):
        for blog in self.blogsCriados:
            blg = Sistema.getBlogById(blog)
            print(f"id: {blog:<20}titulo: {blg.titulo}")