package br.ufba.idp;

public class Programa {

	public static void main(String[] args) {
        IFuncionario funcionario = Fabrica.criarFuncionario();
        funcionario.setNome("Carlos");
        funcionario.setSobreNome("Silva");
        funcionario.setTelefone("(71) 988888888");
        funcionario.setEmail("carloss@ufba.br");

        ITarefa tarefa = Fabrica.criarTarefa();
        tarefa.setNome("Preparar o relat�rio");
        tarefa.setResponsavel(funcionario);

        tarefa.realizarTrabalho(3);
        tarefa.realizarTrabalho(1.5);
        tarefa.completarTarefa();
	}

}
