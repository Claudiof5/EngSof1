from comando.iComando import iComando
from comando.parametro.Parametro import Parametro
from Biblioteca import Biblioteca

class EmprestarLivroComando(iComando):
        
        def executar(self, parametro: Parametro):
            biblioteca = Biblioteca.get_instance()
            retorno = biblioteca.emprestar_livro(parametro.getParametroUm(), parametro.getParametroDois())
            return retorno
            