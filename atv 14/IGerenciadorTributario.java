import java.util.List;

public interface IGerenciadorTributario {
    public void registraTotalImpostoMes(int ano, int mes, List<IVenda> vendasMes);
}

//criada a interface IGerenciadorTributario 