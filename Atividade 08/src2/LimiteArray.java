import java.util.Arrays;
import java.util.InputMismatchException;
import java.util.Scanner;

import static java.lang.Integer.parseInt;

public class LimiteArray {
    public LimiteArray() {
        Scanner sc = new Scanner(System.in);
        int[] lista = new int[10];
        int nLido;
        int indice = 0;

        System.out.println("Digite uma sequência de números:");
        System.out.println("(Digite o número e enter em seguida)");
        try {
            do {
                nLido = sc.nextInt();
                lista[indice] = nLido;
                indice++;
            } while (nLido != 0);
            System.out.print("Array: ");
        } catch (InputMismatchException e) {
            System.out.println("Você digitou um valor suportado (não numérico)");
            System.out.print("Array até o momento: ");
        }
        catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Você digitou mais números que o Array comporta");
            System.out.print("Array até o momento: ");
        } finally {
            System.out.print(String.format("%s", lista[0]));
            if(lista[1] != 0) {
                for(indice=1; indice<10; indice++) {
                    if (lista[indice] == 0) break;
                    System.out.print(String.format(", %s", lista[indice]));
                }
            }
        }
    }
}
