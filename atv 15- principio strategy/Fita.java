
public class Fita {

  private String titulo;
  private TipoFita codigoDePreco;

  public Fita(String titulo, TipoFita codigoDePreco) {
    this.titulo = titulo;
    this.codigoDePreco = codigoDePreco;
  }

  public String getTitulo() {
    return titulo;
  }

  public TipoFita getCodigoDePreco() {
    return codigoDePreco;
  }

  public void setCodigoDePreco(TipoFita codigoDePreco) {
    this.codigoDePreco = codigoDePreco;
  }
  
  public double calcularValorAluguel(int diasAlugada) {
      return codigoDePreco.calcularValorAluguel(diasAlugada);
  }
}

