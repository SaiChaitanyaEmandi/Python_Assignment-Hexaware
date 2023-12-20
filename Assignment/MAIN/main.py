from Assignment.UTIL.DBCONNECTION import DBConnection
from Assignment.DAO.CUSTOMER import Customer
from Assignment.DAO.ACCOUNT import Account
from Assignment.DAO.TRANSACTION import Transaction
from Assignment.DAO.CUSTSERVICEPROVIDERIMPL import cust_service_provider_impl


try:
    connObj = DBConnection()
    con = connObj.getConnection()

    while True:
        customerObj = Customer()
        accountObj = Account()
        transactionObj = Transaction()
        customerServiceObj = cust_service_provider_impl()

        print("Select table to use functionalities")
        print("1.Customer\n2.Account\n3.Transaction\n4.Customer Service Implementation\n5.exit")
        ch = int(input("enter your choice:"))

        if ch == 1:
            while True:
                print(
                    "1.create Customer\t2.insert Customer\t3.update Customer\n4.delete Customer\t5.select Customer\n6.Exit")
                choice = int(input("enter your choice:"))
                if choice == 1:
                    customerObj.create_table()
                elif choice == 2:
                    customerObj.insert_into()
                elif choice == 3:
                    customerObj.update_table()
                elif choice == 4:
                    customerObj.delete_table()
                elif choice == 5:
                    customerObj.select_table()
                elif choice == 6:
                    print("exited successfully")
                    break
                else:
                    print("Wrong choice")

        elif ch == 2:
            while True:
                print(
                    "1.create Account\t2.insert Account\t3.update Account\n4.delete Account\t5.select Account\n6.Exit")
                choice = int(input("enter your choice:"))
                if choice == 1:
                    accountObj.create_table()
                elif choice == 2:
                    accountObj.insert_into()
                elif choice == 3:
                    accountObj.update_table()
                elif choice == 4:
                    accountObj.delete_table()
                elif choice == 5:
                    accountObj.select_table()
                elif choice == 6:
                    print("Exited successfully")
                    break
                else:
                    print("Wrong choice")

        elif ch == 3:
            while True:
                print(
                    "1.create transaction\t2.insert transaction\t3.update transaction\n4.delete transaction\t5.select transaction\n6.Exit")
                choice = int(input("enter your choice:"))
                if choice == 1:
                    transactionObj.create_table()
                elif choice == 2:
                    transactionObj.insert_into()
                elif choice == 3:
                    transactionObj.update_table()
                elif choice == 4:
                    transactionObj.delete_table()
                elif choice == 5:
                    transactionObj.select_table()
                elif choice == 6:
                    print("Exited successfully")
                    break
                else:
                    print("Wrong choice")

        elif ch == 4:
            while True:
                print("1.get account balance\t2.get account details\t3.deposit\n4.withdraw\t5.transfer\n6.Exit")
                choice = int(input("enter your choice:"))
                if choice == 1:
                    customerServiceObj.get_account_balance()
                elif choice == 2:
                    customerServiceObj.get_account_details()
                elif choice == 3:
                    customerServiceObj.deposit()
                elif choice == 4:
                    customerServiceObj.withdraw()
                elif choice == 5:
                    customerServiceObj.transfer()
                elif choice == 6:
                    print("Exited successfully")
                    break
                else:
                    print("Wrong choice")

        elif ch == 5:
            print("Exited successfully")
            break

        else:
            print("Wrong choice")

except Exception as e:
    print(f"Unhandled error: {e}")

finally:
    DBConnection.connection.close()
    print("Connection closed")