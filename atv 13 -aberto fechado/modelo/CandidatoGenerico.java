package modelo;

public class CandidatoGenerico implements ICandidato {

	private String nome;
	private String sobrenome;
	private TipoCandidato tipoCandidato = TipoCandidato.GENERICO;

	public CandidatoGenerico(String nome, String sobrenome) {
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
	public CriadorContasGenerico obterCriador(){
		return new CriadorContasGenerico();
	}
}
