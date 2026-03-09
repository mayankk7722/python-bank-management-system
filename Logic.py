import hashlib
import os 

class Bank:
   def __init__(self):
      self.accounts =[]
      self.details = "Detail.txt"
      self.load_from_file()

   def intro(self):
      print("\n" + "="*50)
      print("      ██████╗ ██╗   ██╗██████╗  █████╗ ███╗   ██╗")
      print("      ██╔══██╗██║   ██║██╔══██╗██╔══██╗████╗  ██║")
      print("      ██████╔╝██║   ██║██████╔╝███████║██╔██╗ ██║")
      print("      ██╔═══╝ ██║   ██║██╔══██╗██╔══██║██║╚██╗██║")
      print("      ██║     ╚██████╔╝██████╔╝██║  ██║██║ ╚████║")
      print("      ╚═╝      ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝")
      print("        💳 WELCOME TO PYTHON BANK SYSTEM 💳")
      print("="*50)
      print("Secure | Fast | Reliable")
      print("Manage your account with confidence.")
      print("="*50 + "\n")

   def exit_message(self):
      print("\n" + "="*50)
      print("Thank you for using Python Bank System.")
      print("Your trust is our priority.")
      print("Have a great day! 👋")
      print("="*50 + "\n")


class Account(Bank):
    def create_account(self):
        name = input("Enter Your name: ")
        
        try:
          age = int(input("Enter Your age: "))
          if age >= 18:
            pass
          else:
             print("Sorry You are nor Eligible")
             print("User age should be 18 or above")
             return
          
        except ValueError:
           print("age should be in Numbers")
           return
        
        dob = input("Enter your dob in number(01/01/2005): ")
        account_number = name[0:4].upper() + dob.replace("/","")
        
        password = input("Genrate the password: ")
        conform_password = input("Conform  the password: ")

        while True:
          if password == conform_password: 
            convert_hash = hashlib.sha256(conform_password.encode()).hexdigest()         
            self.accounts.append({"Name":name,
                                  "Account Number":account_number,
                                  "Total Balance":0,
                                  "Password":convert_hash,
                                  "Transactions": [] }
                                  )
            print("\nUser Created Successfuly")
            break
          else:
                print("\nThe password not Match")
                print("Try Again! to Regenrate the password")
                password = input("\nGenrate the password: ")
                conform_password = input("Conform  the password: ")

        print(f"Your Account Number is: {account_number}")


    def save_to_file(self):
     try:
        with open(self.details, "w") as file:
            for user in self.accounts:
                file.write(f"{user['Name']}|{user['Account Number']}|{user['Total Balance']}|{user['Password']}\n")

        print("💾 Data saved successfully!")

     except Exception as e:
        print("Error saving file:", e)


    def load_from_file(self):
     if not os.path.exists(self.details):
        return

     try:
        with open(self.details, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                name, acc_no, balance, password = line.split("|")

                self.accounts.append({
                    "Name": name,
                    "Account Number": acc_no,
                    "Total Balance": int(balance),
                    "Password": password,
                    "Transactions": []
                })

        print("📂 Data loaded successfully!")

     except Exception as e:
        print("Error loading file:", e)
          
class User(Account):
   
   def transaction_history(self):
      Id = input("Enter the Account Number: ")
      found = False

      for acc in self.accounts:
        if acc["Account Number"] == Id:
            found = True

            password = input("Enter the password: ")
            convert_hash = hashlib.sha256(password.encode()).hexdigest()

            if acc["Password"] == convert_hash:
               
               if not acc["Transactions"]:
                 print("No transactions found")
               
               else:
                print("\n------ Transaction History ------")

                for i, record in enumerate(acc["Transactions"], 1):
                 print(f"{i}. {record}")

                 print("---------------------------------\n")
            else:
               print("password is inccorect")
            
            break

      if not found:
           print("account is not found")
               


   def check_balance(self):
      Id = input("Enter the Account Number: ")
      found = False

      for acc in self.accounts:
        if acc["Account Number"] == Id:
            found = True

            password = input("Enter the password: ")
            convert_hash = hashlib.sha256(password.encode()).hexdigest()

            if acc["Password"] == convert_hash:
               print("Total Balance: ", acc["Total Balance"])

            else:
               print("password is inccorect")
            
            break

      if not found:
           print("account is not found")


   def deposit(self):
      Id = input("Enter the Account Number: ")
      found = False

      for acc in self.accounts:
        if acc["Account Number"] == Id:
            found = True
            
            password = input("Enter the password: ")
            convert_hash = hashlib.sha256(password.encode()).hexdigest()

            if acc["Password"] == convert_hash:
               
               while True:
                  try:
                     amount = int(input("Enter the amount you want to deposit: "))
                     break
                  except ValueError:
                     print("Amount should be in Numbers")

               acc["Total Balance"] += amount 
               record =f"Deposit amount {amount} :- {acc['Total Balance']}"
               acc["Transactions"].append(record)
               print("Deposit Successful")
               print("Updated Balance:", acc["Total Balance"])
              
            else:
               print("password is inccorect")
            
            break

      if not found:
           print("account is not found")

   def withdraw(self):
      Id = input("Enter the Account Number: ")
      found = False

      for acc in self.accounts:
        if acc["Account Number"] == Id:
            found = True
            
            password = input("Enter the password: ")
            convert_hash = hashlib.sha256(password.encode()).hexdigest()

            if acc["Password"] == convert_hash:
               
               while True:
                  try:
                     amount = int(input("Enter the amount you want to Withdraw: "))
                     break
                  except ValueError:
                     print("Amount should be in Numbers")
            
               if acc["Total Balance"] >= amount:
                  acc["Total Balance"] -= amount
                  record =f"Withdraw amount {amount} :- {acc['Total Balance']}"
                  acc["Transactions"].append(record) 
                  print("Withdrawl Successful")
                  print("Updated Balance:", acc["Total Balance"])

               else:
                print("Insufficient balance")
                print("Your Balance is ", acc["Total Balance"])

            else:
               print("password is inccorect")
            
            break

      if not found:
           print("account is not found")
                  
   def Transfer(self): 
      Id = input("Enter the Account Number: ")
      found = False

      for acc in self.accounts:
        if acc["Account Number"] == Id:
            found = True
            
            password = input("Enter the password: ")
            convert_hash = hashlib.sha256(password.encode()).hexdigest()

            if acc["Password"] == convert_hash:
                
                while True:
                     try:
                        amount = int(input("Enter the amount you want to transfer: "))
                        break
                     except ValueError:
                      print("Amount should be in Numbers")

                if acc["Total Balance"] >= amount:
                    Transfer_Id = input("Enter the Account Number: ")
                    T_found = False
               
                    for accc in self.accounts:
                        if accc["Account Number"] == Transfer_Id:
                          T_found = True
                         
                          acc["Total Balance"] -= amount
                          record_transfer =f"Transfer to {accc['Account Number']} {amount} :- {acc['Total Balance']}"
                          acc["Transactions"].append(record_transfer)
                         
                          accc["Total Balance"] += amount
                          record_reciver =f"Recevied from {acc['Account Number']} {amount} :- {accc['Total Balance']}"
                          accc["Transactions"].append(record_reciver)
                         
                          print("Amount Transfer Successful")
                          print("Updated Balance:", acc["Total Balance"])
                          break

                    if not T_found:
                        print("account is not found")

                else:
                    print("Insufficient balance")
                    print("Your Balance is ", acc["Total Balance"])

            else:
               print("password is inccorect")
            
            break

      if not found:
           print("account is not found")


x = User()
x.intro()

while True:
   print("1.Create Account")
   print("2.Check Balance")
   print("3.Transaction History")
   print("4.Deposit Money")
   print("5.Withdraw Money")
   print("6.Transfer Money")
   print("7.Exit")

   choice = input("Enter choice: ")

   if choice == "1":
        x.create_account()
        x.save_to_file()
   elif choice == "2":
        x.check_balance()
   elif choice == "3":
        x.transaction_history()
   elif choice == "4":
        x.deposit()
        x.save_to_file()
   elif choice == "5":
        x.withdraw()
        x.save_to_file()
   elif choice == "6":
        x.Transfer()
        x.save_to_file()
   elif choice == "7":
        x.save_to_file()
        x.exit_message()
        break 
   else:
        print("Invalid choice")   


e = input("Press enter for exist: ")
                           
                   
               

