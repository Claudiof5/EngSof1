from comando.iComando import iComando
from comando.parametro.Parametro import Parametro
from Biblioteca import Biblioteca

class ConsultarLivroComando(iComando):
        
        def executar(self, parametro: Parametro):
            
            biblioteca = Biblioteca.get_instance()
            codigoLivro = parametro.getParametroUm()
            livro = biblioteca.find_book(codigoLivro)

            if not livro:
                raise ValueError(f'Livro correspondente ao codigo {codigoLivro} não encontrado')
            return livro.retorna_informacoes()