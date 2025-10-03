import java.util.ArrayList;
import java.util.Scanner;

/*
 * ============================
 * CLASSE BASE (SUPERCLASSE)
 * ============================
 * Representa uma Pessoa genérica.
 * Demonstra ENCAPSULAMENTO, pois os atributos são privados
 * e só podem ser acessados por métodos (getters).
 */
class Pessoa {
    private String nome;   // Encapsulado: só acessível via métodos
    private int idade;     // Encapsulado: protege integridade dos dados

    public Pessoa(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    // Getters (métodos de acesso controlado)
    public String getNome() { return nome; }
    public int getIdade() { return idade; }

    // Método genérico (será sobrescrito nas subclasses → POLIMORFISMO)
    public void apresentar() {
        System.out.println("Olá, sou " + nome + ", tenho " + idade + " anos.");
    }
}

/*
 * ============================
 * SUBCLASSE ALUNO
 * ============================
 * Usa HERANÇA (extends Pessoa), herdando atributos e métodos.
 * Mostra POLIMORFISMO sobrescrevendo o método apresentar().
 */
class Aluno extends Pessoa {
    private String curso;

    public Aluno(String nome, int idade, String curso) {
        super(nome, idade); // chama o construtor da superclasse
        this.curso = curso;
    }

    // POLIMORFISMO: sobrescreve o método da superclasse
    @Override
    public void apresentar() {
        System.out.println("Olá, sou o aluno " + getNome() + ", do curso de " + curso);
    }
}

/*
 * ============================
 * SUBCLASSE PROFESSOR
 * ============================
 * Também herda de Pessoa (HERANÇA).
 * Também altera o comportamento do método apresentar() (POLIMORFISMO).
 */
class Professor extends Pessoa {
    private String disciplina;

    public Professor(String nome, int idade, String disciplina) {
        super(nome, idade);
        this.disciplina = disciplina;
    }

    // POLIMORFISMO: comportamento diferente para Professor
    @Override
    public void apresentar() {
        System.out.println("Olá, sou o professor " + getNome() + ", ensino " + disciplina);
    }
}

/*
 * ============================
 * CLASSE PRINCIPAL
 * ============================
 * Contém o método main() para rodar o programa.
 * Aqui vemos o POLIMORFISMO acontecendo de fato:
 * - Uma lista de Pessoas armazena Alunos e Professores
 * - O método apresentar() se adapta ao tipo real do objeto
 */
public class EscolaApp {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Pessoa> pessoas = new ArrayList<>();

        int opcao;
        do {
            System.out.println("\n--- MENU ---");
            System.out.println("1 - Cadastrar Aluno");
            System.out.println("2 - Cadastrar Professor");
            System.out.println("3 - Listar Pessoas");
            System.out.println("0 - Sair");
            System.out.print("Escolha: ");
            opcao = sc.nextInt();
            sc.nextLine(); // consumir quebra de linha

            switch (opcao) {
                case 1:
                    System.out.print("Nome do aluno: ");
                    String nomeAluno = sc.nextLine();
                    System.out.print("Idade: ");
                    int idadeAluno = sc.nextInt();
                    sc.nextLine();
                    System.out.print("Curso: ");
                    String curso = sc.nextLine();

                    // HERANÇA: Aluno é uma Pessoa
                    pessoas.add(new Aluno(nomeAluno, idadeAluno, curso));
                    System.out.println("Aluno cadastrado com sucesso!");
                    break;

                case 2:
                    System.out.print("Nome do professor: ");
                    String nomeProf = sc.nextLine();
                    System.out.print("Idade: ");
                    int idadeProf = sc.nextInt();
                    sc.nextLine();
                    System.out.print("Disciplina: ");
                    String disciplina = sc.nextLine();

                    // HERANÇA: Professor também é uma Pessoa
                    pessoas.add(new Professor(nomeProf, idadeProf, disciplina));
                    System.out.println("Professor cadastrado com sucesso!");
                    break;

                case 3:
                    System.out.println("\n--- LISTA DE PESSOAS ---");
                    // POLIMORFISMO: cada objeto executa sua versão de apresentar()
                    for (Pessoa p : pessoas) {
                        p.apresentar();
                    }
                    break;

                case 0:
                    System.out.println("Saindo...");
                    break;

                default:
                    System.out.println("Opção inválida!");
            }

        } while (opcao != 0);

        sc.close();
    }
}