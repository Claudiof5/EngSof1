public interface IRegistrador {
    public void save(int ano, int mes, double valor);
}

//criado a interface IRegistrador pois o metodo de registro pode mudar futuramente. seguindo principio aberto/fechado