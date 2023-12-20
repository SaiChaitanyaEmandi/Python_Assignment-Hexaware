from Assignment.UTIL.DBCONNECTION import DBConnection


class Account(DBConnection):

    def __init__(self, acc_num=None, acc_type=None, acc_bal=0.0, cust_id=None,):
        self.acc_num = acc_num
        self.acc_type = acc_type
        self.acc_bal = acc_bal
        self.cust_id = cust_id

    def create_table(self):
        create_query = '''create table if not exists Account(
           acc_num int primary key,
           acc_type varchar(30),
           acc_bal float(2),
           cust_id int
           )'''
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(create_query)
        print("Table created successfully")

    def insert_into(self):
        self.acc_num = int(input("Enter the account number: "))
        self.acc_type = input("Enter the account type: ")
        self.acc_bal = float(input("Enter the account balance: "))
        self.cust_id = int(input("Enter the customer id: "))

        insert_query = '''insert into Account(acc_num, acc_type, acc_bal, cust_id) values(%s,%s,%s,%s)'''
        data = [(self.acc_num, self.acc_type, self.acc_bal, self.cust_id)]
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.executemany(insert_query, data)
        DBConnection.connection.commit()
        print("Inserted Successfully")

    def update_table(self):
        self.acc_num = int(input("Enter the account number: "))
        self.acc_type = input("Enter the account type: ")
        self.acc_bal = float(input("Enter the account balance: "))
        self.cust_id = int(input("Enter the customer id: "))

        update_query = f'update Account set acc_type=%s, acc_bal=%s, cust_id=%s where acc_num=%s'
        data = [(self.acc_type, self.acc_bal, self.cust_id, self.acc_num)]
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.executemany(update_query, data)
        DBConnection.connection.commit()
        print("Updated Successfully")

    def delete_table(self):
        self.acc_num = int(input("Enter the account number to delete record: "))
        delete_query = f'delete from Account where acc_num={self.acc_num}'
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(delete_query)
        DBConnection.connection.commit()
        print("Deleted Successfully")

    def select_table(self):
        select_query = 'select * from Account'
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(select_query)
        data = stmt.fetchall()
        for i in data:
            print(i)
        print("Values successfully displayed")

    def account_exists(self, acc_num):
        try:
            DBConnection.getConnection()
            stmt = DBConnection.connection.cursor()
            select_query = f'SELECT COUNT(*) FROM Account WHERE acc_num = {acc_num}'
            stmt.execute(select_query)
            result = stmt.fetchone()
            if result and result[0] > 0:
                return True
            else:
                return False

        except Exception as e:
            print(f"Error checking account existence: {e}")
            return False

    def fetch(self, acc_num):
        query = f'select acc_bal from Account where acc_num={acc_num}'
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(query)
        res = stmt.fetchone()
        if res:
            return res[0]
        else:
            return None

    def update_balance(self, bal, acc_num):
        query = f'update Account set acc_bal=%s where acc_num=%s'
        data = [(bal, acc_num)]
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.executemany(query, data)
        DBConnection.connection.commit()
        print('Balance updated into the account')

    def get_account_balance(self):
        return self.acc_bal

    def calc_interest(self, interest):
        interest_amount = self.acc_bal * (interest / 100)
        print(f'Interest = {interest_amount}')

