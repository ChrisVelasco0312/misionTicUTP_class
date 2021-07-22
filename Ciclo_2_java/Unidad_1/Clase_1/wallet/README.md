## Getting Started

Welcome to the VS Code Java world. Here is a guideline to help you get started to write Java code in Visual Studio Code.

## Folder Structure

The workspace contains two folders by default, where:

- `src`: the folder to maintain sources
- `lib`: the folder to maintain dependencies

## Dependency Management

The `JAVA PROJECTS` view allows you to manage your dependencies. More details can be found [here](https://github.com/microsoft/vscode-java-dependency#manage-dependencies).

## Challenges

1. Create the following methods, and verify if it works
    - Now the Wallet has an attribute called transactionLimit, if the wallet has a limit(hasLimit == true), cannot allow deposit or withdraw money for a value greather than 200000, this value it's assigned in a constant called TRANSACTION_LIMIT
    - **Transfer Money** : for this functionality an instance of the Wallet class is received, as a parameter and a value, with which the money must be withdrawn from the wallet that calls the method and deposited in the instance that arrives by parameter
    - For transfers consider a rate of 0.2 %, which will be assigned to a constant called TRANSFER_RATE.