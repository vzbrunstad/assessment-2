import unittest
from classes.inventory import Inventory
from classes.customers import Customers
from classes.interface import Interface

class video_store_test(unittest.TestCase):
    
    '''Tests that the classmethods for the Customers and Inventory Classes return lists'''
    def test_customer_returns_list(self):
        self.assertIsInstance(Customers.all_customers(), list)
    def test_inventory_returns_list(self):
        self.assertIsInstance(Inventory.all_inventory(), list)
    def test_interface_returns_str(self):
        all_inventory = Inventory.all_inventory()
        self.assertIsInstance(Interface.check_valid_rental(self,all_inventory), str)
    def test_inventory_displayed(self):
        self.assertTrue(Interface.view_invantory(self))



if __name__ == '__main__':
    unittest.main()