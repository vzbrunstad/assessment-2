import csv 
import os.path

from classes.customers import Customers
from classes.inventory  import Inventory

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/user_info.csv")
customer_info_path = os.path.join(my_path, "../data/customers.csv")

class Interface():
    def __init__(self):
        self.inventory = Inventory.all_inventory()
        self.customers = Customers.all_customers()
        self.customer_checkin_menu() #Initiates the Customer checkin menu 


    def customer_checkin_menu(self): # Creates a new customer account or checks in a current customer

        while True:
            user_input = int(input("""
            
            \n\n\n\n\n\n\n\n\nWelcome to Blockbuster Video, please take a moment to checkin.
            1. New Customer Checkin
            2. Existing Customer Checkin
            3. Quit
            \n\n\n
            """))
            print(user_input)
            if user_input == 1:
                print('hello')
                self.add_customer()
            elif user_input == 2:
                self.login()
            elif user_input == 3:
                break


    def main_menu(self): # once checked in this menu allows the customer to chose options

        while True:
                user_input = int(input("""

                Welcome to Code Platoon Video!
                1. View video inventory
                2. View customer's rented videos
                3. Rent Video
                4. Return Video
                5. Exit Application
                
                """))
            
                if user_input == 1:
                    self.view_invantory()
                elif user_input == 2:
                    self.view_my_rentals()
                elif user_input == 3:
                    self.rent_video()
                elif user_input == 4:
                    self.return_video()
                elif user_input == 5:
                    self.logged_in_user = None
                    self.loggedIn = False
                    break

                    

    def add_customer(self):

        customer_data = {'first_name': 'customer'}

        customer_data['id'] = input('What would you like your id number to be: \n')
        customer_data['first_name'] = input('What is your first name: \n')
        customer_data["last_name"] = input('what is your last name: \n')
        customer_data['current_video_rentals'] = ''
    
        all_customers= Customers.all_customers()
        
        for customer in all_customers:
            if str(customer.id) == str(customer_data['id']):
                print("A customer already exists with that id number. Try again.")
                return self.add_customer()
        all_customers.append(Customers(**dict(customer_data)))
        self.save_to_csv(all_customers)


    def save_to_csv(self, all_customers):
        for customer in all_customers:
                print(customer)
        with open(customer_info_path, 'w') as csvfile:
            customer_csv = csv.writer(csvfile, delimiter=',')
            customer_csv.writerow(["id", "first_name", "last_name", "current_video_rentals"])
        
            # customer_csv.writeheader()
            for customer in all_customers:
                print(customer)
                customer_csv.writerow([customer.id, customer.first_name, customer.last_name, customer.current_video_rentals])

                # id=customer.id
                # first_name=customer.first_name
                # last_name=customer.last_name
                # current_video_rentals = customer.current_video_rentals
                # writer.writerow({'id': id,'first_name': first_name, 'last_name': last_name,'current_video_rentals': current_video_rentals})

    # #     print(f"congradulations {user_data['name']} you have successfully created an account!")
        print(f"\n\n\n\nWelcome {customer.first_name}. You have been entered into our detabase(customers.csv)")
        return self.main_menu()

    def login(self):
        customer_id = input('Please enter your Customer ID Number: \n')
        for customer in Customers.all_customers():
            # print (customer.id)
            if customer.id == customer_id:
                self.current_customer = customer
                self.all_inventory =Inventory.all_inventory()
                # self.logged_in = True
                self.all_inventory = Inventory.all_inventory()
                if customer.first_name == 'Ankur':
                    print(f"\n\n\n\nWelcome {customer.first_name}, have a doughnut")
                else:
                    print(f"\n\n\n\nWelcome {customer.first_name}")
                return self.main_menu()
    #     print(f"\n\nUser with drivers license number {drivers_license} not found.\n\nPlease try again.")        
    #     self.login_menu

    

    def view_invantory(self):
        all_invantory = Inventory.all_inventory()
        print("Blockbusters Current Invantory Includes")
        for movie in all_invantory:
            print(f"{movie.copies_available} copies of {movie.title} rated {movie.rating}")
    
    def view_my_rentals(self):
        Customers.all_customers()
        print(f"""
        
        Customer ID: {self.current_customer.id}
        Name: {self.current_customer.first_name} {self.current_customer.last_name} 
        Movies Checked Out:{self.current_customer.current_video_rentals}
        
        """)

    def rent_video(self):
        print('Rent a Video')

    def return_video(self):
        print('Return a Video')

    # def add_customer(self):
    #     print('Add a Customer')






        # with open(customer_info_path, 'w', newline='') as csv_file:
        #     customer_csv = csv.DictWriter(csv_file, fieldnames = ["id", "first_name", "last_name", "current_video_rentals"])
        #     customer_csv.writeheader()
        #     for customer in all_customers:
        #         print(customer)
        #         customer_csv.writerow([customer.id, customer.first_name, customer.last_name, customer.current_video_rentals])

        #         # id=customer.id
        #         # first_name=customer.first_name
        #         # last_name=customer.last_name
        #         # current_video_rentals = customer.current_video_rentals
        #         # writer.writerow({'id': id,'first_name': first_name, 'last_name': last_name,'current_video_rentals': current_video_rentals})