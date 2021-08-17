package model;

public class Owner extends User {
    private Wallet wallet;

    public Owner(String name) {
        super();
        wallet = new Wallet(false);
        setName(name);
    }

    public Wallet getWallet() {
        return wallet;
    }
}
