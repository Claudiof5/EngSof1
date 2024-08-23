from Usuarios.regrasReserva.iRegrasReserva import *

#from Interface import Interface

class RegrasReservaPadrao(iRegrasReserva):
    
    def apto_a_reserva(self, livro, user) -> bool:
        
        possui_reserva_ativa_mesmo_livro = user.find_reserva(livro) != None
        possui_exemplar_emprestado_do_mesmo_livro = user.find_emprestimo(livro) != None
        condicionais = [ 
            { "condicao": user.limite_de_reservas_atingido(), "mensagem": Interface.Erro_reservas_maximas_atingidas},
            { "condicao": possui_reserva_ativa_mesmo_livro, "mensagem": Interface.Erro_livro_ja_reservado},
            { "condicao": possui_exemplar_emprestado_do_mesmo_livro, "mensagem": Interface.Erro_livro_ja_emprestado},
                        ]
        
        for condicional in condicionais:
            if condicional["condicao"]:
                condicional["mensagem"]()
                return False
        return True