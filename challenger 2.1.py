#program to create an instance of the Bank Account and test the deposite and withdrawal functionality
class bankaccount:
  def __init__(self,account_number,account_holder_name,initial_balance=0.0):
    self.__account_number=account_number
    self.__account_holder_name=account_holder_name
    self.__account_balance=initial_balance
  def deposite(self,amount):
    if amount >0:
      self.__account_balance +=amount
      print("Deposited rupees{}. New balance: rupees{}".format(amount,self.__account_balance))
    else:
      print("Invalid deposite amount. Please deposite a positive amount.")
  def withdraw(self,amount):
    if amount >100 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print("withdraw rupees{}.New balance: rupees{}".format(amount,self.__account_balance))
    else:
      print("Invalid withdrawl amount or Insufficient balance.")
  def display_balance(self):
    print("Account balance for {} (Account #{}): rupees{}".format(self.__account_holder_name,self.__account_number,self.__account_balance))
#creating class for bankaccount
account=bankaccount(account_number="987654321",account_holder_name="bala",initial_balance=500)
account.display_balance()
account.deposite(1000)
account.withdraw(200)
#Entering larger amount than account balance
account.withdraw(2000)
#Entering lower amount than withdrawl limit
account.withdraw(50)
account.display_balance()