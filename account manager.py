import json

file_name = "accounts.json"


def load_accounts():
    try:
        with open(file_name , "r") as file:
            return json.load(file)
    except:
        return{"accounts":[]}

def create_account(account):
    acc_name = input("Enter account name:")
    if acc_name:
        account["accounts"].append(acc_name)
        with open(file_name , "w") as file:
            json.dump(account, file)
    else:
        print("Invalid choice")

def view_accounts(account):
    acc_list = account["accounts"]
    if len(acc_list) == 0:
        print("No accounts found")
    else:
        for acc in acc_list:
            print(acc)

def delete_account(account):
    acc_name = input("Enter account name to be removed:")
    if acc_name:
        account["accounts"].remove(acc_name)
    else:
        print("Invalid choice")

def main():
    account = load_accounts()
    while True:

       print("1. View accounts")
       print("2. Create account")
       print("3. Delete account")
       print("4. Exit")

       choice = input("Enter your choice:")
       if choice == "1":
           view_accounts(account)
       elif choice == "2":
           create_account(account)
       elif choice == "3":
           delete_account(account)
       elif choice == "4":
           print("Thank you for using this program")
           break
       else:
           print("Invalid choice")
           continue
main()

