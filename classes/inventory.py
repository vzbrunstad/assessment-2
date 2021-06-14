import csv 
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
inventory_info_path = os.path.join(my_path, "../data/inventory.csv") # Sets the file path to the inventory.csv file.


class Inventory: # Declares the Inventory Class.
    def __init__(self, id, title, rating, copies_available): # Initiates the Inventory Class.
        self.id = id
        self.title = title
        self.rating = rating
        self.copies_available = copies_available

    @classmethod
    def all_inventory(cls): # reads the inventory.csv when called.
        with open(inventory_info_path, 'r') as inventory_file:
            inventory = csv.DictReader(inventory_file)
            inventory_list = []
            for movie in inventory:
                # print(movie)
                this_movie = Inventory(movie['id'], movie['title'], movie['rating'], movie['copies_available'])
                inventory_list.append(this_movie)
 
            return inventory_list

# id,title,rating,copies_available
# 1,Guardians of the Galaxy,PG-13,5
# 2,Prometheus,R,2
# 3,Split,PG-13,8
# 4,Sing,PG,10
# 5,La La Land,PG-13,0
# 6,WALL-E,G,3
# 7,The Prestige,PG-13,1
# 8,The Dark Knight,PG-13,5
# 9,Inception,PG-13,2
# 10,Interstellar,PG-13,0

#Final