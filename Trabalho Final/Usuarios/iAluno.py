from Usuarios.iUsuario import *


class iAluno(iUsuario):

    limiteDeLivrosMaximo: int
    diasDeEmprestimoMaximo: int
    
    def __init__(self, nome: str, codigoIdentificador: int) -> None:
        super().__init__(nome, codigoIdentificador)
        
    def limite_de_livros_alcancado(self) -> bool:
        return self.numero_emprestimos() >= self.limiteDeLivrosMaximo
    