package br.ufba.idp;

public class Funcionario implements IFuncionario{

	private String nome;
	private String sobreNome;
	private String telefone;
	private String email;
	
	@Override
	public String getNome() {
		return nome;
	}
	@Override
	public void setNome(String nome) {
		this.nome = nome;
	}
	@Override
	public String getSobreNome() {
		return sobreNome;
	}
	@Override
	public void setSobreNome(String sobreNome) {
		this.sobreNome = sobreNome;
	}
	@Override
	public String getTelefone() {
		return telefone;
	}
	@Override
	public void setTelefone(String telefone) {
		this.telefone = telefone;
	}
	@Override
	public String getEmail() {
		return email;
	}
	@Override
	public void setEmail(String email) {
		this.email = email;
	}
	
	
}
