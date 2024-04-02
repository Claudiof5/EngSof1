from .user import User
from .blog import Blog
from typing import List

class Sistema:
    users :List[User] = []
    blogs :List[Blog] = []

    @classmethod    
    def createBlog( cls, donoId : str, titulo : str ) -> Blog:

        novoBlog = Blog(titulo, donoId, donoId + "-" + str(len(cls.blogs)))
        cls.blogs.append( novoBlog)
        return novoBlog.blogId
    
    @classmethod    
    def createNota( cls, userId : str, blogId : str, titulo : str, texto : str ) -> Nota:
        
        blog = cls.getBlogById(blogId)
        notaId = blog.createNota( userId, titulo, texto)
        return notaId

    @classmethod    
    def deleteNota( cls, userId : str, noteId : str):
        listId = noteId.split("-")
        blogId = listId[0] + "-" + listId[1]
        blog = cls.getBlogById(blogId)
        blog.deletaNota(userId, noteId)



    @classmethod    
    def createComentario( cls, userId : str, noteId : str, texto : str ) -> Comentario:
        
        nota = cls.getNoteById(noteId)
        notaId = nota.createComentario( userId, texto)
        return notaId
    
    
    @classmethod    
    def createUser( cls, email : str ) -> User:
        if cls.emailDisponivel:
            novoUser = User(email, str(len(cls.users)))
            cls.users.append( novoUser)
            return novoUser.userId
        
    
    @classmethod    
    def emailDisponivel( cls, email : str ) -> bool:
        for user in cls.users:
            if user.email == email:
                return False
        return True
    
    @classmethod    
    def getBlogById( cls, blogId : str ) -> Blog:
        for blog in cls.blogs:
            if blog.blogId == blogId:
                return blog
            
    @classmethod    
    def getUserById( cls, userId : str ) -> User:
        for user in cls.users:
            if user.userId == userId:
                return user
    
    @classmethod    
    def getNoteById( cls, noteId : str ) -> Nota:
        idList = noteId.split("-")
        blogId = idList[0] + "-" + idList[1]

        blog = cls.getBlogById(blogId)
        nota = blog.getNotaById(noteId)
        return nota

    @classmethod    
    def getComentarioById( cls, comentarioId : str ) -> Nota:
        idList = comentarioId.split("-")
        blogId = idList[0] + "-" + idList[1]
        noteId = blogId + "-" + idList[2]

        blog = cls.getBlogById(blogId)
        nota = blog.getNotaById(noteId)
        comentario = nota.getComentarioById(comentarioId)
        return comentario
        
    @classmethod    
    def getUserByEmail( cls, userEmail : str) -> User:
        for user in cls.users:
            if user.email == userEmail:
                return user
    @classmethod    
    def printAllBlogs( cls ) -> None:
        for blog in cls.blogs:
            print(f"id: {blog.blogId:<20}titulo: {blog.titulo}")

if __name__ =="__main__":
    Sistema.createBlog("1", "macaco")

    blog = Sistema.getBlogById('1-0')
    print(blog.titulo)