package modelo;

public class CandidatoDiretor implements ICandidato {

	private String nome;
	private String sobrenome;
	private TipoCandidato tipoCandidato = TipoCandidato.DIRETOR;

	public CandidatoDiretor(String nome, String sobrenome) {
		this.nome = nome;
		this.sobrenome = sobrenome;
	}

	public String getNome() {
		return nome;
	}
	
	public String getSobrenome() {
		return sobrenome;
	}
	public TipoCandidato getTipoCandidato(){
		return tipoCandidato;
	}
	public CriadorContasDiretor obterCriador(){
		return new CriadorContasDiretor();
	}
}
