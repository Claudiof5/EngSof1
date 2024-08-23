from Usuarios.regrasEmprestimo.iRegrasEmprestimo import *
#from Interface import Interface

class RegrasEmprestimoAlunoGraduacao(iRegrasEmprestimo):

    def apto_a_emprestimo(self, livro :Livro, user  ) -> bool:
        numeroExemplaresDisponiveis = livro.get_numero_exemplares_disponiveis()
        semExemplaresDisponiveis = numeroExemplaresDisponiveis == 0
        existeReserva = user.find_reserva(livro)
        numeroReservas = livro.get_numero_reservas()
        semExemplaresSuficientesParaReservas = numeroReservas >= numeroExemplaresDisponiveis and (not existeReserva)
        existeEmprestimoAtivoDoLivro = user.find_emprestimo(livro) != None


        condicionais = [ 
            { "condicao": semExemplaresDisponiveis,             "mensagem":Interface.Erro_livro_indisponivel},
            { "condicao": user.esta_em_debito(),                "mensagem":Interface.Erro_usuario_em_debito},
            { "condicao": user.limite_de_livros_alcancado(),    "mensagem":Interface.Erro_limite_de_livros_alcancado},
            { "condicao": semExemplaresSuficientesParaReservas, "mensagem":Interface.Erro_reserva_excedida},
            { "condicao": existeEmprestimoAtivoDoLivro,         "mensagem":Interface.Erro_emprestimo_ativo}
                        ]
        
        for condicional in condicionais:
            if condicional["condicao"]:
                condicional["mensagem"]()
                return False
        return True