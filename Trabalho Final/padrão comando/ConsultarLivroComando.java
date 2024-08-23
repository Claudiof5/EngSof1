
public class ConsultarLivroComando implements Comando {

	@Override
	public void executar(Parametros parametros) {
		String codigoLivro = parametros.getCodigoUm();
		Repositorio repositorio = Repositorio.getInstancia();
		Livro livro = repositorio.buscarLivroPorCodigo(codigoLivro);
		
	}

}
