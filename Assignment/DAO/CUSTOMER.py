from Assignment.UTIL.DBCONNECTION import DBConnection
from Assignment.EXCEPTIONS.CUSTOMERIDNOTFOUND import customer_id_not_found_exception


class Customer(DBConnection):
    def __init__(self, cust_id=None, first_name=None, last_name=None, email=None, phone_num=None, address=None):
        self.cust_id = cust_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_num = phone_num
        self.address = address

    def create_table(self):
        create_query = '''create table if not exists Customer(
           cust_id int,
           first_name varchar(30),
           last_name varchar(30),
           email varchar(30),
           phone_num varchar(10),
           address varchar(30)
           )'''
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(create_query)
        print("Table created successfully")

    def insert_into(self):
        self.cust_id = int(input("Enter the customer id: "))
        self.first_name = input("Enter the first name: ")
        self.last_name = input("Enter the last name: ")
        self.email = input("Enter the email: ")
        self.phone_num = input("Enter the phone number: ")
        self.address = input("Enter the address: ")

        insert_query = '''insert into Customer(cust_id, first_name, last_name, email, phone_num, address) values(%s,%s,%s,%s,%s,%s)'''
        data = [(self.cust_id, self.first_name, self.last_name, self.email, self.phone_num, self.address)]
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.executemany(insert_query, data)
        DBConnection.connection.commit()
        print("Inserted Successfully")
        return 'Values inserted successfully'

    def update_table(self):
        try:
            self.cust_id = int(input("Enter the doctor id: "))
            self.first_name = input("Enter the first name: ")
            self.last_name = input("Enter the last name: ")
            self.email = input("Enter the email: ")
            self.phone_num = input("Enter the phone number: ")
            self.address = input("Enter the address: ")
            if not self.customer_exists(self.cust_id):
                raise customer_id_not_found_exception("customer id not found")

            update_query = f'update Customer set first_name=%s, last_name=%s, email=%s, phone_num=%s, address=%s where cust_id=%s'
            data = [(self.first_name, self.last_name, self.email, self.phone_num, self.address, self.cust_id)]
            DBConnection.getConnection()
            stmt = DBConnection.connection.cursor()
            stmt.executemany(update_query, data)
            DBConnection.connection.commit()
            print("Updated Successfully")

        except customer_id_not_found_exception as e:
            print(e)

        except Exception as e:
            print(e)

    def delete_table(self):
        try:
            self.cust_id = int(input("Enter the customer id to delete record: "))
            if not self.customer_exists(self.cust_id):
                raise customer_id_not_found_exception("customer id not found")
            delete_query = f'delete from Customer where cust_id={self.cust_id}'
            DBConnection.getConnection()
            stmt = DBConnection.connection.cursor()
            stmt.execute(delete_query)
            DBConnection.connection.commit()
            print("Deleted Successfully")
            return 'Deleted customer successfully'

        except customer_id_not_found_exception as e:
            print(e)

        except Exception as e:
            print(e)

    def select_table(self):
        select_query = 'select * from Customer'
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(select_query)
        data = stmt.fetchall()
        for i in data:
            print(i)
        print("Values successfully displayed")

    def customer_exists(self, cust_id):
        try:
            DBConnection.getConnection()
            stmt = DBConnection.connection.cursor()
            select_query = f'SELECT COUNT(*) FROM Customer WHERE cust_id = {cust_id}'
            stmt.execute(select_query)
            result = stmt.fetchone()
            if result and result[0] > 0:
                return True
            else:
                return False

        except Exception as e:
            print(f"Error checking patient existence: {e}")
            return False

    def getvalues(self):
        print(self.cust_id)
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.phone_num)
        print(self.address)

    def set_customer_id(self, cust_id):
        self.cust_id = cust_id

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_email(self, email):
        self.email = email

    def set_phone_number(self, phone_num):
        self.phone_num = phone_num

    def set_address(self, address):
        self.address = address

# obj = Customer()
# obj.create_table()
# obj.insert_into()
# obj.select_table()

