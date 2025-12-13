class BankAccount {
  constructor(balance) {
    this.balance = balance;
  }
  
  deposit(amount) {
    this.balance += amount; // משנה את המצב
    return this.balance;
  }
}

const account = new BankAccount(100);
account.deposit(50); // 150



const deposit = (balance, amount) => balance + amount;

const balance = 100;
const newBalance = deposit(balance, 50); // 150
// balance עדיין 100 - לא השתנה