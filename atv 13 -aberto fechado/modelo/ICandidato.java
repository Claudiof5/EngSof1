package modelo;


public interface ICandidato {

    public String getNome();
    public String getSobrenome();

    public ICriadorContas obterCriador();
}