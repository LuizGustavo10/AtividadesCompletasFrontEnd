// Exemplo de classe
class Carro {
    String modelo;   // atributo
    int ano;         // atributo

    void buzinar() { // método
        System.out.println("Buzinando!");
    }
}

class Carro {
    private String modelo; // privado, não acessível direto

    // métodos para acessar e alterar (getters e setters)
    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }
}




class Veiculo {
    int ano;
    void ligar() {
        System.out.println("Ligando o veículo...");
    }
}

class Carro extends Veiculo { // Carro herda Veiculo
    String modelo;
}

public class Main {
    public static void main(String[] args) {
        Carro c = new Carro();
        c.ano = 2020; // atributo herdado
        c.modelo = "Civic";
        c.ligar();     // método herdado
    }
}