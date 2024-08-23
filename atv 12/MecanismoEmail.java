package br.ufba.idp;

public class MecanismoEmail implements IMecanismoMensagem{
    @Override
	public void enviarMensagem(IFuncionario funcionario, String mensagem){
		System.out.println("Simulando o envio de email para " + funcionario.getNome());
	}
}
