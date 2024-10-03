from Usuarios.regrasEmprestimo.iRegrasEmprestimo import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Usuarios.iAluno import iAluno

class RegrasEmprestimoAluno(iRegrasEmprestimo):

    def apto_a_emprestimo(self, livro: Livro, user: 'iAluno'  ) -> bool:
        numeroExemplaresDisponiveis = livro.get_numero_exemplares_disponiveis()
        semExemplaresDisponiveis = numeroExemplaresDisponiveis == 0
        existeReserva = user.find_reserva(livro)
        numeroReservas = livro.get_numero_reservas()
        semExemplaresSuficientesParaReservas = numeroReservas >= numeroExemplaresDisponiveis and (not existeReserva)
        existeEmprestimoAtivoDoLivro = user.find_emprestimo(livro) != None


        condicionais = [ 
            { "condicao": semExemplaresDisponiveis,             "erro": AssertionError(f"O livro {livro.titulo} não possui exemplares disponíveis") },
            { "condicao": user.esta_em_debito(),                "erro": AssertionError(f"O usuário {user.nome} está em débito") },
            { "condicao": user.limite_de_livros_alcancado(),    "erro": AssertionError(f"O usuário {user.nome} atingiu o limite de emprestimos") },
            { "condicao": semExemplaresSuficientesParaReservas, "erro": AssertionError(f"O livro {livro.titulo} não possui exemplares suficientes para suprir as reservas e o usuário {user.nome} não possui reserva") },
            { "condicao": existeEmprestimoAtivoDoLivro,         "erro": AssertionError(f"O usuário {user.nome} já possui exemplar emprestado deste livro") },
                        ]
        
        for condicional in condicionais:
            if condicional["condicao"]:
                raise condicional["erro"]
        return True