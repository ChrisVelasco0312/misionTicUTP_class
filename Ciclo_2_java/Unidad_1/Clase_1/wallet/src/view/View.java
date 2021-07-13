package view;

import java.util.Scanner;

import model.Wallet;

public class View {
    public static void main(String[] args) {
        // Create 2 different objects wallet
        Wallet wallet1 = new Wallet(true);
        Wallet wallet2 = new Wallet(false);

        String balance1 = wallet1.setBalance(600000);
        System.out.println(balance1 + "\n" + wallet1.getBalance());
        String balance2 = wallet2.setBalance(600000);
        System.out.println(balance2 + "\n" + wallet2.getBalance());

        Scanner sc = new Scanner(System.in);
        System.out.println("New withdraw for wallet 2: ");
        System.out.println("How much would you like to withdraw?: ");
        int withdraw2 = sc.nextInt();

        System.out.println(wallet2.withdrawBalance(withdraw2));
        sc.close();
    }
}
