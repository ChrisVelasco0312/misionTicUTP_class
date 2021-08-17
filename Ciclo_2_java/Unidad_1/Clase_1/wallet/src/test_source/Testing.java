package test_source;

import model.Owner;
import model.Wallet;

public class Testing {

    public Testing() {
        super();
    }

    public void scenarioOwner() {
        // Creamos 2 objetos owner
        Owner owner1 = new Owner("Juan");
        // Owner owner2 = new Owner("Pedro");

        boolean r1 = assertTrue("Juan", owner1.getName());
        System.out.println("Prueba nombre " + (r1 ? "Pasó" : "No pasó"));

        owner1.getWallet().setBalance(200000);
        boolean r2 = assertTrue(200000, owner1.getWallet().getBalance());
        System.out.println("Prueba carga de saldo " + (r2 ? "Pasó" : "No pasó"));

        owner1.getWallet().setGoal(500000);
        boolean r3 = assertTrue(500000, owner1.getWallet().getGoal());
        System.out.println("Prueba de méta " + (r3 ? "Pasó" : "No pasó"));

        owner1.getWallet().getMoney(150000);
        boolean r4 = assertFalse(200000, owner1.getWallet().getBalance());
        System.out.println("Prueba de sacar dinero " + (r4 ? "Pasó" : "No pasó"));
    }

    public void scenarioWallet() {
        Wallet wallet1 = new Wallet(false);

        int walletOneBalance = 550000;
        wallet1.setBalance(walletOneBalance);
        boolean r1 = assertTrue(walletOneBalance, wallet1.getBalance());
        System.out.println("Prueba Wallet carga de saldo " + (r1 ? "Pasó" : "No pasó"));

        int walletOneWithdrawal = 250000;
        wallet1.getMoney(walletOneWithdrawal);
        boolean r2 = assertTrue((walletOneBalance - walletOneWithdrawal), wallet1.getBalance());
        System.out.println("Prueba Wallet retiro de saldo " + (r2 ? "Pasó" : "No pasó"));

        int walletOneGoal = 2000000;
        int walletOneNewBallance = 1720000;
        wallet1.setGoal(walletOneGoal);
        wallet1.setBalance(walletOneNewBallance);
        boolean r3 = assertTrue(true, wallet1.verifyGoal());
        System.out.println("Prueba Wallet méta superada " + (r3 ? "Pasó" : "No pasó"));
    }

    // Comparar 2 strings y devuelve si son iguales o no.
    public boolean assertTrue(String expected, String received) {
        if (expected.equalsIgnoreCase(received)) {
            return true;
        }
        return false;
    }

    public boolean assertTrue(boolean expected, boolean received) {
        if (expected == received) {
            return true;
        }
        return false;
    }

    // Comparación de enteros
    public boolean assertTrue(int expected, int received) {
        if (expected == received) {
            return true;
        }
        return false;
    }

    // Evaluar una condicion negativa de cadenas
    public boolean assertFalse(String expected, String received) {
        if (expected.equalsIgnoreCase(received)) {
            return false;
        }
        return true;
    }

    // Evaluar una condicion negativa de enteros
    public boolean assertFalse(int expected, int received) {
        if (expected == received) {
            return false;
        }
        return true;
    }

}
