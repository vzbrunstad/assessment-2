import csv
import os

from classes.inventory import Inventory
from classes.customers import Customers

class Movies(Inventory): # Declares the Movies class
    def __init__(self, id, title, rating, copies_available): #Initializes the movies class.
        super().__init__(id, title, rating, copies_available)
        self.checked_out = 'y'

    def __str__(self):
        return f"""
        ID: {self.id}
        Title:  {self.title}
        Rating: {self.rating}
        Copies Avaliable: {self.copies_available}
        Checked out: {self.checked_out}
        """

#Final