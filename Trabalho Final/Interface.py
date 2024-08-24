from comando.iComando import iComando
from comando.parametro.Parametro import Parametro
from comando.EmprestarLivroComando import EmprestarLivroComando
from comando.DevolverLivroComando import DevolverLivroComando
from comando.ReservarLivroComando import ReservarLivroComando
from comando.ObservarLivroComando import ObservarLivroComando
from comando.ConsultarLivroComando import ConsultarLivroComando
from comando.ConsultarUsuarioComando import ConsultarUsuarioComando
from comando.ConsultarNotificacaoComando import ConsultarNotificacaoComando
from comando.SaiDoSistemaComando import SaiDoSistemaComando

class Interface:

    def __init__(self) -> None:
        self.comandos: dict[str, dict[str, iComando|int ]] = {}
        self.iniciar_Comandos()


    def iniciar_Comandos(self):
        self.comandos['emp'] = {"comando": EmprestarLivroComando(), "parametros": 2, "responseHandler": self.mensagem_emprestimo_realizado}
        self.comandos['dev'] = {"comando": DevolverLivroComando(), "parametros": 2, "responseHandler": self.mensagem_devolucao_realizada}
        self.comandos['res'] = {"comando": ReservarLivroComando(), "parametros": 2, "responseHandler": self.mensagem_reserva_realizada}
        self.comandos['obs'] = {"comando": ObservarLivroComando(), "parametros": 2, "responseHandler": self.mensagem_inscricao_realizada}
        self.comandos['liv'] = {"comando": ConsultarLivroComando(), "parametros": 1, "responseHandler": self.mensagem_consuta_de_livro}
        self.comandos['usu'] = {"comando": ConsultarUsuarioComando(), "parametros": 1, "responseHandler": self.mensagem_consulta_de_usuario}
        self.comandos['ntf'] = {"comando": ConsultarNotificacaoComando(), "parametros": 1, "responseHandler": self.mensagem_consulta_de_notificacao}
        self.comandos['sai'] = {"comando": SaiDoSistemaComando(), "parametros": 0, "responseHandler": self.mensagem_sai_do_sistema}


    def recebe_entrada(self) -> str:
        entrada = input("Digite o comando: ")
        return self.trata_entrada(entrada)
    
    def trata_entrada(self, entrada: str)-> list[str]:
        listaDeEntrada = entrada.split(" ")
        listaDeEntrada = [parametro.strip() for parametro in listaDeEntrada]
        return listaDeEntrada
    
    def criar_parametros(self, listaDeEntrada: list[str]) -> Parametro:
        if len(listaDeEntrada) == 1:
            return Parametro(None, None)
        elif len(listaDeEntrada) == 2:
            return Parametro(listaDeEntrada[1], None)
        else:
            return Parametro(listaDeEntrada[1], listaDeEntrada[2])
    
    
    def comando_valido(self, comando: list[str]) -> bool:
        if comando[0] in self.comandos:
            if len(comando) -1 == self.comandos[comando[0]]["parametros"]:

                return True

            raise ValueError(f"Quantidade de parametros inválida para o comando {comando[0]}, esperado {self.comandos[comando[0]]['parametros']} parametros, recebido {len(comando) -1} parametros")
        
        raise ValueError(f"Comando {comando[0]} não encontrado")
    
    def executar_comando(self, comando: list[str]):
        try:
            
            if self.comando_valido(comando):
                
                parametro :Parametro = self.criar_parametros(comando)
                responseHandler = self.comandos[comando[0]]["responseHandler"]
                comando   :iComando  = self.comandos[comando[0]]["comando"]
            
        
                retorno = comando.executar(parametro)
                responseHandler(**retorno)
        except Exception as e:
                print(f"Operação não concluída. {e}\n")

    def iniciar_sistema(self):
        while True:
            entrada = self.recebe_entrada()
            self.executar_comando(entrada)
            
    #dicionário padrão de retorno de sucesso de operação
    #dict = {nomeUsuario: None, nomeLivro: None, dataDeDevolucaoEsperada: None, dataDevolucao: None}
    def mensagem_emprestimo_realizado(self, nomeUsuario, nomeLivro, dataDeDevolucaoEsperada, **kwargs):
        print(f"Emprestimo do livro '{nomeLivro}' realizada com sucesso pelo usuário {nomeUsuario}, data de devolução esperada: {dataDeDevolucaoEsperada}\n")

    def mensagem_devolucao_realizada(self, nomeUsuario, nomeLivro, dataDevolucao, **kwargs):
        print(f"Devolução do livro '{nomeLivro}' realizada com sucesso pelo usuário {nomeUsuario} em {dataDevolucao} \n")

    def mensagem_reserva_realizada(self, nomeUsuario, nomeLivro, **kwargs):
        print(f"Reserva do livro '{nomeLivro}' realizada com sucesso pelo usuário{nomeUsuario}\n")

    def mensagem_inscricao_realizada(self, nomeUsuario, nomeLivro, **kwargs):
        print(f"Inscrição do usuário {nomeUsuario} no livro '{nomeLivro}' realizada com sucesso. O mesmo será notificado quando o limite de reservas for passado\n")
        
    def mensagem_sai_do_sistema(self):
        print("Sistema encerrado")

    #formato dicionário padrão de retorno consulta de livro
    #dict = {titulo: None, numero_de_reservas: None, nome_dos_reservantes: None, dados_exemplares: dict[str, dict[str:str]]}
    #dados_exemplares = {codigoExemplar: {disponivel: None, emprestimo: None}}
    #emprestimo = {nomeUsuario: None, dataEmprestimo: None, dataDeDevolucaoEsperada: None}
    def mensagem_consuta_de_livro(self, titulo, numero_de_reservas, dados_exemplares: dict[str, dict[str:str]], nome_dos_reservantes):

        print("Titulo: ", titulo)
        
        print(f"Quantidade de reservas: {numero_de_reservas}")

        if numero_de_reservas > 0:
            for nome in nome_dos_reservantes:
                print(f"\t-{nome}")

        print("Exemplares")
        existem_exemplares = len(dados_exemplares) > 0
        if existem_exemplares:
            for codigoExemplar, dadosExemplar in dados_exemplares.items():

                if dadosExemplar["disponivel"]:
                    print(f"\t-Codigo Exemplar: {codigoExemplar}\n\tStatus: Disponivel\n\t")
                else:
                    emprestimo = dadosExemplar["emprestimo"]
                    if emprestimo:
                        print(f"\t-Codigo Exemplar: {codigoExemplar}\n\tStatus: Emprestado")
                        print(f"\tUsuario: {emprestimo["nomeUsuario"]}\n\tData de Emprestimo: {emprestimo["dataEmprestimo"]} | Data de Devolução Esperada: {emprestimo["dataDeDevolucaoEsperada"]}\n")

    #formato dicionário padrão de retorno consulta de usuario
    #dict = {nome: str, em_debito: bool, reservas: List[reservas], emprestimos:List[emprestimos], numero_notificacoes:int}
    #reservas = {titulo: str, data: str}
    #emprestimos = {titulo: str, dataEmprestimo: str, dataDeDevolucaoEsperada: str, dataDevolucao: str, status: str}
    def mensagem_consulta_de_usuario(self, nome, em_debito, reservas, emprestimos, **kwargs):
        emprestimosEmCurso = []
        emprestimosAtrasados = []
        emprestimosConcluidos = []
        for emprestimo in emprestimos:
            if emprestimo["status"] == "Em Curso":
                emprestimosEmCurso.append(emprestimo)
            elif emprestimo["status"] == "Em Atraso":    
                emprestimosAtrasados.append(emprestimo)
            elif emprestimo["status"] == "Finalizado":
                emprestimosConcluidos.append(emprestimo)
        
        print("Nome: ", nome)
        print("Está em débito: ", em_debito)
        
        numero_notificacoes = kwargs.get("numero_notificacoes")
        if numero_notificacoes != None:
            print(f"Numero de notificações: {numero_notificacoes}")

        if reservas:
            print("Reservas: ")
            for reserva in reservas:
                print(f"Livro: {reserva['titulo']} Data: {reserva['dataReserva']}")
        else:
            print("Sem reservas\n")

        if emprestimosEmCurso:
            print("Empréstimos em curso: ")
            for emprestimo in emprestimosEmCurso:
                print(f"\t-Livro: {emprestimo['titulo']} \n\tData de Emprestimo: {emprestimo['dataEmprestimo']} Data de Devolução Esperada: {emprestimo['dataDeDevolucaoEsperada']}\n\tStatus: {emprestimo['status']}\n")
        
        if emprestimosAtrasados:
            print("Empréstimos atrasados: ")
            for emprestimo in emprestimosAtrasados:
                print(f"\t-Livro: {emprestimo['titulo']} \n\tData de Emprestimo: {emprestimo['dataEmprestimo']} Data de Devolução Esperada: {emprestimo['dataDeDevolucaoEsperada']}\n\tStatus: {emprestimo['status']}\n")
        else:
            print("Sem empréstimos atrasados\n")
        
        if emprestimosConcluidos:
            print("Empréstimos concluidos: ")
            for emprestimo in emprestimosConcluidos:
                print(f"\t-Livro: {emprestimo['titulo']} \n\tData de Emprestimo: {emprestimo['dataEmprestimo']} Data de Devolução Esperada: {emprestimo['dataDeDevolucaoEsperada']}\n\tStatus: {emprestimo['status']}\n")
    
    def mensagem_consulta_de_notificacao(self, nome, numero_notificacoes):
        print(f"Numero de notificações para o usuário {nome}: {numero_notificacoes}\n")    