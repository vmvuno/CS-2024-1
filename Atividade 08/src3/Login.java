import java.util.Objects;

public class Login {
    static String usuario = "admin";
    static String senha = "admin";

    public static boolean fazer_login(String usuario, String senha) throws LoginInvalidoException {
        if (!Objects.equals(usuario, Login.usuario) |  !Objects.equals(senha, Login.senha)) {
            throw new LoginInvalidoException();
        }
        return true;
    }
}
