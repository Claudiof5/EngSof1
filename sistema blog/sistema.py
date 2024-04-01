from user import User
from blog import Blog
from nota import Nota
from comentario import Comentario
from typing import List

class Sistema:
    users :List[User] = []
    blogs :List[Blog] = []

    @staticmethod
    def createBlog( donoId: User, titulo: str)-> Blog:
        novoBlog = Blog(titulo, donoId, len(Sistema.blogs))
        Sistema.blogs.append( novoBlog)
        return novoBlog.blogId
    
    @staticmethod
    def createUser( email:str )-> User:
        if Sistema.emailDisponivel:
            novoUser = User(email, str(len(Sistema.users)))
            Sistema.users.append( novoUser)
            return novoUser.userId
        
    
    @staticmethod
    def emailDisponivel( email: str) -> bool:
        for user in Sistema.users:
            if user.email == email:
                return False
        return True
    
    @staticmethod
    def getBlogById( blogId:str) -> Blog:
        for blog in Sistema.blogs:
            if blog.blogId == blogId:
                return blog
            
    @staticmethod
    def getUserById( userId:str) -> User:
        for user in Sistema.users:
            if user.userId == userId:
                return user

if __name__ =="__main__":
    Sistema.createBlog("1", "macaco")
     