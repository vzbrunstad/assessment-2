import unittest
from classes.inventory import Inventory
from classes.customers import Customers

class video_store_test(unittest.TestCase):
    
    '''Tests the correct output if insufficient funds are paid'''
    def test_customer_returns_list(self):
        self.assertIsInstance(Customers.all_customers(), list)
    def test_inventory_returns_list(self):
        self.assertIsInstance(Inventory.all_inventory(), list)


if __name__ == '__main__':
    unittest.main()