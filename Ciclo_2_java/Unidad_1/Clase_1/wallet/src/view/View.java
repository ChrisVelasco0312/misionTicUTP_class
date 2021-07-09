package view;

import model.Wallet;

public class View {
    public static void main(String[] args) {
        // Create 2 different objects wallet
        Wallet wallet1 = new Wallet(true);
        Wallet wallet2 = new Wallet(false);

        wallet1.getBalance();
        wallet2.getBalance();
    }
}
