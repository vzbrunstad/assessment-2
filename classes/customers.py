import csv 
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
customer_info_path = os.path.join(my_path, "../data/customers.csv")


class Customers:
    # users = []
    def __init__(self, id, first_name, last_name,current_video_rentals):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.current_video_rentals = current_video_rentals


    @classmethod
    def all_customers(cls):
        with open(customer_info_path, 'r') as customers_file:
            customers = csv.DictReader(customers_file)
            customers_list = []
            for customer in customers:
                print(customer)
                this_customer = Customers(customer['id'], customer['first_name'], customer['last_name'], customer['current_video_rentals'])
                customers_list.append(this_customer)
             
 
            return customers_list

# id,first_name,last_name,current_video_rentals
# 1,Jon,Young,Guardians Of The Galaxy/La La Land
# 2,Tom,Prete,Prometheus/Split/Sing
# 3,Rod,Levy,The Dark Knight/Guardians Of The Galaxy/Split
# 4,Ankur,Shah,The Prestige
# 5,Chris,Howell,
