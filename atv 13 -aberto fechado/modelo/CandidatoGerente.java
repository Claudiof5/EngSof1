package modelo;

public class CandidatoGerente implements ICandidato {

	private String nome;
	private String sobrenome;
	private TipoCandidato tipoCandidato = TipoCandidato.GERENTE;

	public CandidatoGerente(String nome, String sobrenome) {
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

	public CriadorContasGerente obterCriador(){
		return new CriadorContasGerente();
	}
	
}
