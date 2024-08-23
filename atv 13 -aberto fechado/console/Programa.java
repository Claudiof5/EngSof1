package console;

import java.util.*;
import modelo.*;

public class Programa {

	public static void main(String[] args) {
		List<ICandidato> candidatos = new ArrayList<ICandidato>();
	    candidatos.add(new CandidatoGenerico("Carlos", "Silva"));
	    candidatos.add(new CandidatoGerente("Maria", "Souza"));
	    candidatos.add(new CandidatoDiretor("Ana", "Lopes"));

	    List<Empregado> empregados = new ArrayList<Empregado>();

	    for (ICandidato candidato: candidatos)
	    {
	        empregados.add(candidato.obterCriador().criar(candidato));
	    }

	    for (Empregado empregado: empregados)
	    {
	        System.out.println(empregado.getNome() + " " + empregado.getSobrenome() + " " + empregado.getEmail() + "Gerente: " + empregado.isGerente() + "Diretor: " + empregado.isDiretor());
	    }

	}

}
