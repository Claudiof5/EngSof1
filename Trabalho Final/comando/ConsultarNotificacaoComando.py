from comando.iComando import iComando
from comando.parametro.Parametro import Parametro
from Biblioteca import Biblioteca

class ConsultarNotificacaoComando(iComando):
        
        def executar(self, parametro: Parametro):
            biblioteca = Biblioteca.get_instance()
            return biblioteca.retorna_informacoes_notificacoes_professor(parametro.getParametroUm())
            