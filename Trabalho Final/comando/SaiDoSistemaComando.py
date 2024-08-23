from comando.iComando import iComando
from comando.parametro.Parametro import Parametro
from sys import exit

class SaiDoSistemaComando(iComando):
        
        def executar(self, parametro: Parametro):
            exit()