public class SaldoInsuficienteException extends Exception{
    public SaldoInsuficienteException() {
        super("Vocâ não tem saldo suficiente para realizar essa transação");
    }
}
