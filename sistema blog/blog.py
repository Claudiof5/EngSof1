from datetime import datetime 
from user import User

class Blog:
    def __init__(self, titulo: str, donoId:str, blogId: str) -> None:
        self.titulo = titulo
        self.dataCriacao = datetime.now().strftime("%x")
        self.notes = []
        self.blogId = blogId