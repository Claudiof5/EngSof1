from Usuarios.regrasReserva.iRegrasReserva import *

#from Interface import Interface

class RegrasReservaPadrao(iRegrasReserva):
    
    def apto_a_reserva(self, livro, user) -> bool:
        
        possui_reserva_ativa_mesmo_livro = user.find_reserva(livro) != None
        possui_exemplar_emprestado_do_mesmo_livro = user.find_emprestimo(livro) != None
        condicionais = [ 
            { "condicao": user.limite_de_reservas_atingido(), "erro": AssertionError(f"O usuário {user.nome} atingiu o limite de reservas") },
            { "condicao": possui_reserva_ativa_mesmo_livro, "erro": AssertionError(f"O usuário {user.nome} já possui reserva ativa para o livro {livro.titulo}") },
            { "condicao": possui_exemplar_emprestado_do_mesmo_livro, "erro": AssertionError(f"O usuário {user.nome} já possui exemplar emprestado deste livro {livro.titulo}") },
                        ]
        
        for condicional in condicionais:
            if condicional["condicao"]:
                raise condicional["erro"]
        return True