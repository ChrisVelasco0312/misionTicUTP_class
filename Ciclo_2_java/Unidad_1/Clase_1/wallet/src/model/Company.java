package model;

public class Company extends User {
    private Wallet wallet;

    public Company(String name) {
        super();
        wallet = new Wallet(false);
        setName(name);
    }

    public Wallet getWallet() {
        return wallet;
    }
}
