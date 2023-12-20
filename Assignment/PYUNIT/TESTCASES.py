import unittest
from Assignment.DAO.CUSTOMER import Customer


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.custObj = Customer()

    def test_customer_insertion(self):
        print("create a new customer with customer id = 4")
        res = self.custObj.insert_into()
        self.assertEqual('Values inserted successfully', res)

    def test_customer_deletion(self):
        print("Delete a customer with customer id = 4")
        res = self.custObj.delete_table()
        self.assertEqual('Deleted customer successfully', res)


if __name__ == '__main__':
    unittest.main()
