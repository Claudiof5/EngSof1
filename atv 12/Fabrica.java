package br.ufba.idp;

public class Fabrica {
        public static IFuncionario criarFuncionario(){
                return new Funcionario();
        }
        public static IMecanismoMensagem criarMecanismoIMecanismoMensagem(){
                return new MecanismoEmail();
        }
        public static IMecanismoLog criarMecanismoLog(){
                return new MecanismoLog();
        }
        public static ITarefa criarTarefa(){
                return new Tarefa();
        }

}

//Fabrica criado pelo principio de responsabilidade unica