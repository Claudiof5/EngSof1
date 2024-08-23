
public class Venda implements IVenda{
	private String data;
	private double valor;
	
	public Venda(String data, double valor) {
		this.data = data;
		this.valor = valor;
	}
	
	public String getData() {
		return data;
	}
	
	public double getValor() {
		return valor;
	}
}

