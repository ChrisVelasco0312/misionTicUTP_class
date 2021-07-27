package model;

import java.util.Scanner;

public class Wallet {

    // Create the constant for the wallet limit
    public static final int WALLET_LIMIT = 500000;
    public static final int TRANSACTION_LIMIT = 200000;
    /**
     * wallet balance
     */

    private int balance;
    private boolean hasLimit;
    private int goal;

    public Wallet(boolean limit) {
        super();
        // initialize balance attr
        balance = 0;
        goal = 0;
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
        if (verifyGoal()) {
            System.out.println("You have surpassed the goal!");
        }
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
    public String getMoney(int value) {
        if (value > balance) {
            int tempBalance = balance;

            return "Sorry, you have insufficient funds";
        }
        balance -= value;
        return "Succesful balance withdrawal ";
    }

    // set and verify goal --- My solution

    // public String setGoal(int value) {
    // goal = value;
    // return "Congrats!, your new goal was set to: " + goal;
    // }

    // public String verifyGoal() {
    // if (goal == 0) {
    // return "Sorry the goal has not been set yet.";
    // } else if (goal > 0 && balance == goal) {
    // return "Congratulations, you have reached the goal!";
    // } else if (balance > goal) {
    // return "You just have surpassed the goal! by: " + (balance - goal);
    // }
    // return "You're still " + (goal - balance) + " short to the goal of: " + goal;
    // }

    // Lesson Solution

    public String setGoal(int value) {
        if (value > WALLET_LIMIT && hasLimit) {
            return "You can't set a goal higher than the limit";
        }
        if (value <= 0) {
            return "The value is not valid";
        }
        if (value <= balance) {
            return "You have already surpassed this goal!";
        }
        goal = value;
        return "New goal added";
    }

    public int getGoal() {
        return goal;
    }

    public boolean verifyGoal() {
        if (balance >= goal && goal > 0) {
            return true;
        }
        return false;
    }

}
