from Assignment.UTIL.DBCONNECTION import DBConnection


class Transaction(DBConnection):
    def __init__(self, transaction_id=None, acc_num=None, description=None, transaction_date=None, transaction_type=None, transaction_amount=0.0):
        self.transaction_id = transaction_id
        self.acc_num = acc_num
        self.description = description
        self.transaction_date = transaction_date
        self.transaction_type = transaction_type
        self.transaction_amount = transaction_amount

    def create_table(self):
        create_query = '''create table if not exists Transaction(
           transaction_id int primary key AUTO_INCREMENT,
           acc_num int,
           description varchar(150),
           transaction_date date,
           transaction_type varchar(30),
           transaction_amount float(2)
           )'''
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(create_query)
        print("Table created successfully")

    def insert_into(self):
        self.transaction_id = int(input("Enter the transaction id: "))
        self.acc_num = int(input("Enter the account number: "))
        self.description = input("Enter the description: ")
        self.transaction_date = input("Enter the transaction date: ")
        self.transaction_type = input("Enter the transaction type: ")
        self.transaction_amount = float(input("Enter the transaction amount: "))

        insert_query = '''insert into Transaction(transaction_id, acc_num, description, transaction_date, transaction_type, transaction_amount) values(%s,%s,%s,%s,%s,%s)'''
        data = [(self.transaction_id, self.acc_num, self.description, self.transaction_date, self.transaction_type, self.transaction_amount)]
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.executemany(insert_query, data)
        DBConnection.connection.commit()
        print("Inserted Successfully")

    def update_table(self):
        self.transaction_id = int(input("Enter the transaction id: "))
        self.acc_num = int(input("Enter the account number: "))
        self.description = input("Enter the description: ")
        self.transaction_date = input("Enter the transaction date: ")
        self.transaction_type = input("Enter the transaction type: ")
        self.transaction_amount = float(input("Enter the transaction amount: "))

        update_query = f'update Transaction set acc_num=%s, description=%s, transaction_date=%s, transaction_type=%s, transaction_amount=%s where transaction_id=%s'
        data = [(self.acc_num, self.description, self.transaction_date, self.transaction_type, self.transaction_amount, self.transaction_id)]
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.executemany(update_query, data)
        DBConnection.connection.commit()
        print("Updated Successfully")

    def delete_table(self):
        self.transaction_id = int(input("Enter the transaction id to delete record: "))
        delete_query = f'delete from Transaction where transaction_id={self.transaction_id}'
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(delete_query)
        DBConnection.connection.commit()
        print("Deleted Successfully")

    def select_table(self):
        select_query = 'select * from Transaction'
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(select_query)
        data = stmt.fetchall()
        for i in data:
            print(i)
        print("Values successfully displayed")


# obj = Transaction()
# obj.create_table()
# obj.select_table()
