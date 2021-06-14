import csv 
import os.path

from classes.customers import Customers
from classes.inventory  import Inventory

my_path = os.path.abspath(os.path.dirname(__file__))
customer_info_path = os.path.join(my_path, "../data/customers.csv")
inventory_info_path = os.path.join(my_path, "../data/inventory.csv")

class Interface(): # Declare the Interface Class

    #----------------------------------------
    def __init__(self):#Initialize the Interface Class
        self.inventory = Inventory.all_inventory() # read the inventory.csv and set to self.inventory
        self.customers = Customers.all_customers() # read the customer.csv and set to self.customer
        self.customer_checkin_menu() #Initiates the Customer checkin menu 

    #----------------------------------------
    def customer_checkin_menu(self): # Creates a new customer account or checks in a current customer

        while True:
            #This is the desplay menu
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

    #----------------------------------------
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

    #----------------------------------------
    def add_customer(self):# adds a customer by asking for user inputs, soring in customer_data, appending all_customers then saving to the csv file.

        # User Inputs saves to the customer_data dict
        customer_data = {'first_name': 'customer'}
        customer_data['id'] = input('\n\n\n\n\n\n\n\n\n\n\nWhat would you like your id number to be: \n')
        customer_data['first_name'] = input('What is your first name: \n')
        customer_data["last_name"] = input('what is your last name: \n')
        customer_data['current_video_rentals'] = ''

        # customers csv read
        all_customers= Customers.all_customers()
        
        # checks for a user with the requested id and appends user inputs to the local all_customers list
        for customer in all_customers:
            if str(customer.id) == str(customer_data['id']):
                print("\n\n\n\nA customer already exists with that id number. Try again.")
                return self.add_customer()
        all_customers.append(Customers(**dict(customer_data)))
        


        print(f"\n\n\n\nWelcome {customer.first_name}. You have been entered into our detabase(customers.csv)")
        #calles the method to save the customers.csv
        self.save_customer_csv(all_customers)

        for customer in Customers.all_customers():
            if str(customer.id) == str(customer_data['id']):
                self.current_customer = customer
        self.main_menu()


    #----------------------------------------
    def save_customer_csv(self, all_customers):#can be called by other methods to save all_customers to the csv file.
        with open(customer_info_path, 'w') as csvfile:
            customer_csv = csv.writer(csvfile, delimiter=',')
            customer_csv.writerow(["id", "first_name", "last_name", "current_video_rentals"])
            for customer in all_customers:
                customer_csv.writerow([customer.id, customer.first_name, customer.last_name, customer.current_video_rentals])

        # self.current_customer = customer
        self.all_inventory =Inventory.all_inventory()
        self.all_Customers = Customers.all_customers()
        


    #----------------------------------------
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

    
    #----------------------------------------
    def view_invantory(self): #displays the current invantory of movies.
        all_invantory = Inventory.all_inventory()
        print("Blockbusters Current Invantory Includes")
        for movie in all_invantory:
            print(f"{movie.copies_available} copies of {movie.title} rated {movie.rating}")
        return True


    #----------------------------------------   
    def view_my_rentals(self): # Displays the current customers information to include checked out movies.
        Customers.all_customers()
        print(f"""
        
        Customer ID:         {self.current_customer.id}
        Name:                {self.current_customer.first_name} {self.current_customer.last_name} 
        Movies Checked Out:  {self.current_customer.current_video_rentals}
        
        """)
        return True


    #----------------------------------------
    def rent_video(self): #adds the requested movie to the current customers checked ot movies list and decrements -1 from the available movies in the inventory.
        all_inventory = Inventory.all_inventory() # Reads the current Inventory from the csv
        all_customers= Customers.all_customers() # Reads the current customers from the csv
        print("What movie would you like to rent?. Below is a list of available movies:\n")

        for movie_title in all_inventory:#Displays a list of movies in stock
            if movie_title.copies_available != 0:
                print(movie_title.title)

        rental = self.check_valid_rental(all_inventory)

        for customer in all_customers:
            if customer.id == self.current_customer.id:
                self.current_customer = customer
                if customer.current_video_rentals == '':
                    customer.current_video_rentals += rental
                else:
                    customer.current_video_rentals += '/'+rental
        self.save_customer_csv(all_customers)

        for movie in all_inventory:
            if movie.title == rental:
                movie.copies_available = int(movie.copies_available) - 1

        print(f"\n\n\n\n{self.current_customer.first_name} enjoy your movie")
        self.save_invantory_csv(all_inventory)

        print (self.current_customer.first_name)


    #----------------------------------------
    def return_video(self):
        all_inventory = Inventory.all_inventory() # Reads the current Inventory from the csv
        all_customers= Customers.all_customers() # Reads the current customers from the csv
        print("What movie would you like to rent?. Below is a list of available movies:\n")

        (returned,rented_movies) = self.check_valid_return()

        updated_rented_movies = []
        for movie in rented_movies: # Removes all copies of the returned movie and appends current customer.
            if movie == returned:
                pass
            else:
                updated_rented_movies.append(movie)

        slash = '/'
        updated_rented_movies_str = slash.join(updated_rented_movies)
        print(updated_rented_movies_str)
 
        for movie in all_inventory: # Add the returned movie to the invantory
            if movie.title == returned:
                movie.copies_available = int(movie.copies_available) + 1 # I am assuming nobody would rent more than one of a movie.
                self.save_invantory_csv(all_inventory)

        for customer in all_customers:
            
            if customer.id == self.current_customer.id:
                self.current_customer = customer
                customer.current_video_rentals = updated_rented_movies_str
                print(f"Current Videos: {customer.current_video_rentals}")
                self.save_customer_csv(all_customers)

        print(f"\n\n\n\n{self.current_customer.first_name} Thank you for returning {returned}. Check out our new releases while your here")

        return True


    #----------------------------------------
    def save_invantory_csv(self,all_inventory): # writes all_invantory to the invantory csv
        print('saving inventory')
        with open(inventory_info_path, 'w') as csvfile:
            inventory_csv = csv.writer(csvfile, delimiter=',')
            inventory_csv.writerow(["id", "title", "rating", "copies_available"])
            for inventory in all_inventory:
                inventory_csv.writerow([inventory.id, inventory.title, inventory.rating, inventory.copies_available])


    #----------------------------------------
    def check_valid_rental(self,all_inventory): #checks if the inputed movie is valid and in stock.

        valid_movie = False
        while valid_movie == False: # Only allows movies in stock to be rented.
            rental = input("\n\nMovie:")

            for movie in all_inventory: # Check if the requested movie is in the inventory (punctuation matters)

                    if str(movie.title) == str(rental) and int(movie.copies_available) >= 1:
                        valid_movie = True
                        return rental
                    
            print('Thats is not a valid movie please try again with proper punctuation.')

        



    #----------------------------------------
    def check_valid_return(self):

        valid_rental = False
        while valid_rental == False:
            rented_movies = self.current_customer.current_video_rentals.split("/")
            if len(rented_movies) == 0:
                print ('You havnt rented any movies, do you intend to donate that movie?')
            else:
                print(f"Which movie would you like to return?")
                for movies in rented_movies:
                    print (movies)
                returned = input('Movie:')
                if returned in rented_movies:
                    return (returned,rented_movies)
                


        
#Final