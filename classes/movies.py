import csv
import os

from classes.invantory import Invantory
from classes.customers import Customers

class Movies(Invantory): # Not sure if this shoudlbe Customers or Invantory as the parent
    def __init__(self, id, title, rating, copies_available):
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