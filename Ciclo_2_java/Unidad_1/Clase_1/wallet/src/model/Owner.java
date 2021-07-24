package model;

public class Owner extends User {
    private Wallet wallet;

    public Owner() {
        super();
        wallet = new Wallet(false);
        setName("Hello");
    }

    public Wallet getWallet() {
        return wallet;
    }
}
