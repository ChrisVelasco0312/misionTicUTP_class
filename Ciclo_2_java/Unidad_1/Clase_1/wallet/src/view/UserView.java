package view;

import model.Company;
import model.Owner;

public class UserView {

    public static void main(String[] args) {
        Owner owner1 = new Owner("Rodrain");
        System.out.println(owner1.getName());
        Owner owner2 = new Owner("Palahniuk");
        System.out.println(owner2.getName());
        System.out.println(owner1.getWallet().setBalance(200000));

        Company robbleSolutions = new Company("Robble Solutions STDA");
        System.out.println(robbleSolutions.getName());
    }

}
