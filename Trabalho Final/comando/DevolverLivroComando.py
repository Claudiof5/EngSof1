from comando.iComando import iComando
from comando.parametro.Parametro import Parametro
from Biblioteca import Biblioteca

class DevolverLivroComando(iComando):
        
        def executar(self, parametro: Parametro):
            biblioteca: Biblioteca = Biblioteca.get_instance()
            codigoUsuario = parametro.getParametroUm()
            codigoLivro = parametro.getParametroDois()

            usuario = biblioteca.find_user(codigoUsuario)
            livro = biblioteca.find_book(codigoLivro)
            if not usuario:
                raise ValueError(f'Usuário correspondente ao codigo {codigoUsuario} não encontrado')
            
            if not livro:
                raise ValueError(f'Livro correspondente ao codigo {codigoLivro} não encontrado')
                
            
            emprestimo = usuario.find_emprestimo(livro)
            if not emprestimo:
                raise ValueError(f'Usuário não possui emprestimo do livro correspondente ao codigo {codigoLivro}')
            
            emprestimo.emCurso = False
            emprestimo.dataDeDevolucao = biblioteca._datetime.now().date()
            retorno = {"nomeUsuario": usuario.nome, "nomeLivro": livro.titulo, "dataDeDevolucaoEsperada": emprestimo.dataDeDevolucaoEsperada, "dataDevolucao": emprestimo.dataDeDevolucao}
            return retorno