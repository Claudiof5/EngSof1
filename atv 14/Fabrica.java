import java.util.ArrayList;
import java.util.List;

public class Fabrica {
    
    public static IGerenciadorTributario criarGerenciadorTributario(){
        return new GerenciadorTributario();
    }
    public static IVenda criarVenda(String data, double valor){
        return new Venda( data, valor);
    }
    public static IRegistrador criarBancoDados(){
        return new BancoDados();
    }
    public static List<IVenda> criaListaIVenda(){
        return new ArrayList<IVenda>();
    }
}

//Criado tendo em mente o principio de responsabilidade unica