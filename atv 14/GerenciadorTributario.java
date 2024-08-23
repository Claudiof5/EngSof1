import java.util.List;

public class GerenciadorTributario implements IGerenciadorTributario{

	public void registraTotalImpostoMes(int ano, int mes, List<IVenda> vendasMes) {
		
		double imposto = 0;
		for (IVenda venda : vendasMes)
		{	
			if (venda.getValor() < 1000)
				imposto += 0.05 * venda.getValor();
			else
				imposto += 0.07 * venda.getValor();
		}
		
		//registra valor do imposto total
		IRegistrador banco = Fabrica.criarBancoDados();
		banco.save(ano, mes, imposto);
		
	}

}
