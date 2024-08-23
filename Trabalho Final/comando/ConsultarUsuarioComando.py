from comando.iComando import iComando
from comando.parametro.Parametro import Parametro
from Biblioteca import Biblioteca

class ConsultarUsuarioComando(iComando):
        
        def executar(self, parametro: Parametro):
            biblioteca = Biblioteca.get_instance()
            biblioteca.retorna_informacoes_usuarios(parametro.getParametroUm())
            