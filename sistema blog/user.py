from sistema import Sistema

class User:
    
    def __init__(self, email: str, userId : str) -> None:
        self.email = email
        self.userId = userId
        self.comentariosCriados = []
        self.notasCriadas = []
        self.blogsCriados = []

    def criaBlog(self, titulo):
        blogId = Sistema.createBlog(self.userId, titulo)
        self.blogsCriados.append(blogId)

    def comentar(self, )
