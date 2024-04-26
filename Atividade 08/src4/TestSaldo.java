import java.util.Scanner;

public class TestSaldo {
    double saldoInicial = 1000;

    public TestSaldo() {
        ContaBancaria conta = new ContaBancaria(saldoInicial);
        Scanner sc = new Scanner(System.in);

        System.out.println("\nBem-vindo à sua conta!");
        System.out.println(String.format("Seu saldo atual é: R$ %s\n\n", conta.getSaldo()));

        System.out.println("Faça um depósito!");
        System.out.print("Digite o valor a ser depositado: R$");
        conta.depositar(sc.nextDouble());
        System.out.println(String.format("Seu novo saldo é: R$ %s\n\n", conta.getSaldo()));

        System.out.println("Faça um saque!");
        System.out.print("Digite o valor da retirada: R$");

        try {
            conta.sacar(sc.nextDouble());
            System.out.println(String.format("Seu novo saldo é: R$ %s\n\n", conta.getSaldo()));
        } catch (SaldoInsuficienteException e) {
            System.out.println("\nOperação não permitida - Saldo insuficiente");
        }
    }
}
