package br.ufba.idp;

public interface IFuncionario {

    String getNome();
    void setNome(String nome);

    String getSobreNome();
    void setSobreNome(String sobreNome);

    String getTelefone();
    void setTelefone(String telefone);

    String getEmail();
    void setEmail(String email);
}