import java.util.List;

public class Programa {

	public static void main(String[] args) {
		//mudança de Classe para interface caso varios tipos de venda sejam criadas de acordo com o principio Inversão de Dependencias
		//uso de Fabrica para diminuir acoplamento da classe e garantir principio da responsabilidade unica
		List<IVenda> vendas = Fabrica.criaListaIVenda();
		vendas.add( Fabrica.criarVenda("10/05/2023", 11.5   ) );
		vendas.add( Fabrica.criarVenda("12/05/2023", 8.5    ) );
		vendas.add( Fabrica.criarVenda("12/05/2023", 1000.0 ) );
		
		//criado interface IGerenciadorTributario para o principio Inversão de Dependencias
		IGerenciadorTributario impostos = Fabrica.criarGerenciadorTributario();
		impostos.registraTotalImpostoMes(2023, 5, vendas);
		
	}

}
