import java.util.InputMismatchException;
import java.util.Scanner;

public class Divisao {
    public Divisao() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite o primeiro número (numerador): ");
        String input1 = sc.nextLine();
        System.out.println("Digite o segundo número (denominador): ");
        String input2 = sc.nextLine();

        try {
            int n1 = Integer.parseInt(input1);
            int n2 = Integer.parseInt(input2);
            System.out.println("A parte inteira da divisão é: " + n1 / n2);
        } catch (NumberFormatException e) {
            System.out.println("Um dos valores informados não é numérico");
        } catch (ArithmeticException e) {
            System.out.print("O denominador não pode ter valor 0");
        }
    }
};