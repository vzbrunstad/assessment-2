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
                self.add_customer()
            elif user_input == 2:
                self.login()
            elif user_input == 3:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nThank you, Come again\n\n\n\n\n\n")
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

                    

    def add_customer(self):# adds a customer by asking for user inputs, soring in customer_data, appending all_customers then saving to the csv file.

        customer_data = {'first_name': 'customer'}

        customer_data['id'] = input('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWhat would you like your id number to be: \n')
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


    def save_to_csv(self, all_customers):#can be called by other methods to save add_customers to the csv file.
        with open(customer_info_path, 'w') as csvfile:
            customer_csv = csv.writer(csvfile, delimiter=',')
            customer_csv.writerow(["id", "first_name", "last_name", "current_video_rentals"])
            for customer in all_customers:
                customer_csv.writerow([customer.id, customer.first_name, customer.last_name, customer.current_video_rentals])

        print(f"\n\n\n\nWelcome {customer.first_name}. You have been entered into our detabase(customers.csv)")
        self.current_customer = customer
        self.all_inventory =Inventory.all_inventory()
        self.all_Customers = Customers.all_customers()
        return self.main_menu()

    def login(self):#called by existing users to identify who will be renting/returning videos.
        customer_id = input('Please enter your Customer ID Number: \n')
        for customer in Customers.all_customers():
            if customer.id == customer_id:
                self.current_customer = customer
                self.all_inventory =Inventory.all_inventory()
                self.all_Customers = Customers.all_customers()
                if customer.first_name == 'Ankur':
                    print(f"\n\n\n\nWelcome {customer.first_name}, have a doughnut")
                else:
                    print(f"\n\n\n\nWelcome {customer.first_name}")
                return self.main_menu()
        print(f"\n\nUser with drivers license number {customer_id} not found.\n\nPlease try again.")        
        self.customer_checkin_menu

    

    def view_invantory(self): #displays the current invantory of movies.
        all_invantory = Inventory.all_inventory()
        print("Blockbusters Current Invantory Includes")
        for movie in all_invantory:
            print(f"{movie.copies_available} copies of {movie.title} rated {movie.rating}")
    
    def view_my_rentals(self):
        Customers.all_customers()
        print(f"""
        
        Customer ID:         {self.current_customer.id}
        Name:                {self.current_customer.first_name} {self.current_customer.last_name} 
        Movies Checked Out:  {self.current_customer.current_video_rentals}
        
        """)

    def rent_video(self):
        all_invantory = Inventory.all_inventory()
        all_customers= Customers.all_customers()
        print("What movie would you like to rent?. Below is a list of available movies:\n")
        for movie_title in all_invantory:
            if movie_title.copies_available != 0:
                print(movie_title.title)

        rental = input("")
        
        with open(customer_info_path, 'w') as csvfile:
            customer_csv = csv.writer(csvfile, delimiter=',')
            customer_csv.writerow(["id", "first_name", "last_name", "current_video_rentals"])
            for customer in all_customers:
                if customer.id == self.current_customer.id:
                    if self.current_customer.current_video_rentals == "":
                        customer_csv.writerow([customer.id, customer.first_name, customer.last_name, self.current_customer.current_video_rentals+rental])
                    else:
                        customer_csv.writerow([customer.id, customer.first_name, customer.last_name, self.current_customer.current_video_rentals+"/"+rental])
                else:
                    customer_csv.writerow([customer.id, customer.first_name, customer.last_name,customer.current_video_rentals])

        print(f"\n\n\n\nWelcome {customer.first_name}. You have been entered into our detabase(customers.csv)")
        self.current_customer = customer
        self.all_inventory =Inventory.all_inventory()
        # self.logged_in = True
        self.all_Customers = Customers.all_customers()
        return self.main_menu()


    def return_video(self):
        print('Return a Video')





