
public class BancoDados implements IRegistrador {
	public void save(int ano, int mes, double valor) {
		System.out.println("Simulando o registro em banco de dados: " + ano + "/" + mes + " " + valor);
	}
}
