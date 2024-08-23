package modelo;

public class CriadorContasDiretor implements ICriadorContas{
    public Empregado criar(ICandidato candidato) 
    {
        Empregado empregado = new Empregado();

        empregado.setNome(candidato.getNome());
        empregado.setSobrenome(candidato.getSobrenome());

        empregado.setEmail(candidato.getNome() + candidato.getSobrenome() + "@xptodiretoria.com");
        empregado.setDiretor(true);
        
        return empregado;
    }
}
