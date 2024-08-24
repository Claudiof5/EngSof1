from comando.iComando import iComando
from comando.parametro.Parametro import Parametro
from Biblioteca import Biblioteca

class ReservarLivroComando(iComando):
        
        def executar(self, parametro: Parametro):
            biblioteca = Biblioteca.get_instance()
            retorno = biblioteca.reservar_livro(parametro.getParametroUm(), parametro.getParametroDois())
            return retorno