package model;

public class Wallet {

    // Create the constant for the wallet limit
    public static final int WALLET_LIMIT = 5000000;
    /**
     * wallet balance
     */

    private int balance;
    private boolean hasLimit;

    public Wallet(boolean limit) {
        super();
        // initialize balance attr
        balance = 0;
        hasLimit = limit;
    }

    public int getBalance() {
        return balance;
    }

    public String setBalance(int value) {
        if (balance + value > WALLET_LIMIT && hasLimit) {
            return "cannot exceed the limit";
        }
        balance += value;
        return "Operation succeed! your new balance is " + balance;

    }
}
