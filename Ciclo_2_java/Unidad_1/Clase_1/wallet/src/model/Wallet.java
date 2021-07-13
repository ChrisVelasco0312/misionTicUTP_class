package model;

import java.util.Scanner;

public class Wallet {

    // Create the constant for the wallet limit
    public static final int WALLET_LIMIT = 500000;
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

    // My solution
    public String withdrawBalance(int withdraw) {
        // Validate if have balance
        if (balance == 0) {
            return "Sorry, you have insufficient funds";
        } else if (withdraw <= balance && withdraw >= 10000) {
            // Validate if withdraw is grater than balance and meets the minimun of 10000
            balance -= withdraw;// Subtract the witdraw from the balance
            return "Operation succeed!, \n you have made a withdrawal for: " + withdraw + "\n Your balance now is: "
                    + balance; // return the succed message
        }

        return "Sorry, you are only allowed to withdraw a minimum of 10000 , please try again.";
    }

    // The lesson solution
    public String getMoney(int value){
        if(value > balance){
            int tempBalance = balance;
            
            return "Sorry, you have insufficient funds";
        }
        balance -= value;
        return "Succesful balance withdrawal "
    }
}
