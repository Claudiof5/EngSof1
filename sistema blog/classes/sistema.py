from user import User
from blog import *
from typing import List

class Sistema:
    users :List[User] = []
    blogs :List[Blog] = []

    @staticmethod
    def createBlog( donoId : str, titulo : str ) -> Blog:

        novoBlog = Blog(titulo, donoId, donoId + "-" + str(len(Sistema.blogs)))
        Sistema.blogs.append( novoBlog)
        return novoBlog.blogId
    
    @staticmethod
    def createNota( userId : str, blogId : str, titulo : str, texto : str ) -> Nota:
        
        blog = Sistema.getBlogById(blogId)
        notaId = blog.createNota( userId, titulo, texto)
        return notaId

    @staticmethod
    def deleteNota( userId : str, noteId : str):
        listId = noteId.split("-")
        blogId = listId[0] + "-" + listId[1]
        blog = Sistema.getBlogById(blogId)
        blog.deletaNota(userId, noteId)



    @staticmethod
    def createComentario( userId : str, noteId : str, texto : str ) -> Comentario:
        
        nota = Sistema.getNoteById(noteId)
        notaId = nota.createComentario( userId, texto)
        return notaId
    
    
    @staticmethod
    def createUser( email : str ) -> User:
        if Sistema.emailDisponivel:
            novoUser = User(email, str(len(Sistema.users)))
            Sistema.users.append( novoUser)
            return novoUser.userId
        
    
    @staticmethod
    def emailDisponivel( email : str ) -> bool:
        for user in Sistema.users:
            if user.email == email:
                return False
        return True
    
    @staticmethod
    def getBlogById( blogId : str ) -> Blog:
        for blog in Sistema.blogs:
            if blog.blogId == blogId:
                return blog
            
    @staticmethod
    def getUserById( userId : str ) -> User:
        for user in Sistema.users:
            if user.userId == userId:
                return user
    
    @staticmethod
    def getNoteById( noteId : str ) -> Nota:
        idList = noteId.split("-")
        blogId = idList[0] + "-" + idList[1]

        blog = Sistema.getBlogById(blogId)
        nota = blog.getNotaById(noteId)
        return nota

    @staticmethod
    def getComentarioById( comentarioId : str ) -> Nota:
        idList = comentarioId.split("-")
        blogId = idList[0] + "-" + idList[1]
        noteId = blogId + "-" + idList[2]

        blog = Sistema.getBlogById(blogId)
        nota = blog.getNotaById(noteId)
        comentario = nota.getComentarioById(comentarioId)
        return comentario
        
    @staticmethod
    def getUserByEmail( userEmail : str) -> User:
        for user in Sistema.users:
            if user.email == userEmail:
                return user

    def printAllBlogs() -> None:
        for blog in Sistema.blogs:
            print(f"id: {blog.blogId:<20}titulo: {blog.titulo}")
if __name__ =="__main__":
    Sistema.createBlog("1", "macaco")

    blog = Sistema.getBlogById('1-0')
    print(blog.titulo)