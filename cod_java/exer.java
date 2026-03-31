import java.util.Scanner;

public class exer {
    public static void main(String[] args) {
        //String nome = "Johnny";
        //String sobrenome = "Cortez";
        //System.out.println("Olá " + nome + " " + sobrenome);
        
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite seu nome: ");
        String nome = scanner.nextLine();

        System.out.println("Digite o seu sobrenome: ");
        String sobrenome = scanner.nextLine();
        
        System.out.println("Digite a sua idade: ");
        int idade = scanner.nextInt();
        
        System.out.println("Olá " + nome + " " + sobrenome);
        
        if (idade >=18) {
            System.out.println("Você é maior de idade!");
        } else {
            System.out.println("Você é menor de idade!");
        }

        System.out.println("Você tem " + idade + " anos! " );

        scanner.close();
    }
}