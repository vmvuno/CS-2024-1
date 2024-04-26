import java.util.Scanner;

public class LoginTeste {
    public LoginTeste() {
        String usuario;
        String senha;
        Scanner sc = new Scanner(System.in);
        System.out.print("Usuário: ");
        usuario = sc.next();
        System.out.print("Senha:   ");
        senha = sc.next();

        try {
            Login.fazer_login(usuario, senha);
            System.out.println("\nLogin efetuado com sucesso");
        } catch (LoginInvalidoException e) {
            System.out.println("\nLogin não efetuado - Usuário ou senha incorreto");
        }
    }
}
