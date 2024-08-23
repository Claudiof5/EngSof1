import java.util.List;

public class Repositorio {
	private static Repositorio instancia;	
	private List<Usuario> usuarios;
	private List<Livro> livros;
	
	private Repositorio() {};
	
	public static Repositorio getInstancia() {
		if (instancia == null)
			instancia = new Repositorio();
		return instancia;
	}
	
	public Usuario buscarUsuarioPorCodigo(String codigoUsuario) {
		return null;
	}
	
	public Livro buscarLivroPorCodigo(String codigoLivro) {
		return null;
	}

}
