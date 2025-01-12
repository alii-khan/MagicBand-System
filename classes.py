class Ride:
    def __init__(self, ride_name:str, height_requirement:int, capacity:int):
        self.ride_name = ride_name # The name of the ride.
        self.height_requirement = height_requirement # The height requirement for the ride.
        self.capacity = capacity # The number of guests the ride can accommodate at a time.
        self.queue = [] # A list of Magic Bands waiting to enter the ride.
        self.total_visitors = 0 # Counts how many visitors visited this ride.

    def __str__(self):
        return self.ride_name

    def add_to_queue(self, band): # Adds a guest’s Magic Band to the ride queue.
        self.queue.append(band)
       
        self.total_visitors += 1 # Increases the counter by 1

    def complete_ride(self, band): # Removes a guest's Magic Band to the ride queue.
        self.queue.remove(band)
   
    def get_ride_info(self): # Returns details about the ride.
        return f"""
*** RIDE INFO ***
Ride name: {self.ride_name}
Height Requirement: {self.height_requirement}
Capacity: {self.capacity}
Queue Length: {len(self.queue)}
"""

class Restaurant:
    def __init__(self, name: str):
        self.name = name
        self.dishes = []

        # Used for get_restaurant_info function (same for the shop class)
        self.list1 = []
        self.list2 = []

    def __str__(self):
        return self.name

    def add_dish(self, name_of_dish: str, price_of_dish: float):
        self.dishes.append((name_of_dish, price_of_dish)) # Adds as a tuple.

    def get_restaurant_info(self):

        # Adds the length of names and prices to a list separately
        for x in self.dishes:
            self.list1.append(len(x[0]))
            self.list2.append(len(str(x[1])))

        # Finds the greatest length in each list (num1 is item and num2 is price)
        self.num1 = max(self.list1)
        self.num2 = max(self.list2)

        # Centers the restaurant name according to the greatest length for item and price (same for the shop class)
        # The other numbers account for "Dish name: ", "Price: $", etc.
        restaurant_info = "\n" + f"*** {self.name} ***".center(self.num1 + self.num2 + 8 + 11 + 5) + "\n\n" + "*** MENU ***".center(self.num1 + self.num2 + 8 + 11 + 5) + "\n"

        for x in self.dishes:
            restaurant_info += "\nDish name: " + str(x[0]).ljust(self.num1 + 5) + "Price: $" + str(x[1])

        return restaurant_info

class Shop:
    def __init__(self, name: str):
        self.name = name
        self.items = []

        self.list1 = []
        self.list2 = []

    def __str__(self):
        return self.name

    def add_item(self, name_of_item: str, price_of_item: float):
        self.items.append((name_of_item, price_of_item)) # Adds as a tuple.

    def get_shop_info(self):
        for x in self.items:
            self.list1.append(len(x[0]))
            self.list2.append(len(str(x[1])))

        self.num1 = max(self.list1)

        self.num2 = max(self.list2)

        shop_info = "\n" + f"*** {self.name} ***".center(self.num1 + self.num2 + 8 + 11 + 5) + "\n\n" + "*** ITEMS ***".center(self.num1 + self.num2 + 8 + 11 + 5) + "\n"

        for x in self.items:
            shop_info += "\nItem name: " + str(x[0]).ljust(self.num1 + 5) + "Price: $" + str(x[1])

        return shop_info

class Element:

    current_element_id = 1000

    def __init__(self, name_of_element:str, type:str):

        Element.current_element_id += 1
        self.element_id = "Park Element " + str(Element.current_element_id) #A unique identifier for the element.
        self.name = name_of_element # The name of the element.
        self.interaction_type = type # The type of interaction supported (e.g., scan, touch, proximity).
        self.interaction_log = "Magic Band Interaction Log:\n"# A log of interactions with Magic Bands.

    def __str__(self):
        return self.element_id

    def interact(self, band_id):
        # Logs an interaction with a Magic Band.
        # From https://www.geeksforgeeks.org/get-current-date-and-time-using-python/
        import datetime
        self.interaction_log += str(datetime.datetime.now()) + "   Band: " + str(band_id) +"\n"

    def get_interaction_summary(self):
        # Provides a summary of all interactions.
        return self.interaction_log

class Park:

    def __init__(self, name_of_park:str):
       
       self.park_name = name_of_park
       self.rides = []
       self.elements = []
       self.shops = []
       self.restaurants = []

    def __str__(self):
        return self.park_name

    def add_ride(self,ride):
        #adds a ride to the park
        self.rides.append(ride)

    def add_elements(self,element):
        #adds an element to the park
        self.elements.append(element)

    def add_shops(self, shops_in_park):
        #adds a shop to the park
        self.shops.append(shops_in_park)

    def add_restaurant(self,restaurant):
        #adds restaurant to the park
        self.restaurants.append(restaurant)

    def get_overview(self):
        #gives the summary of the park

        print(f"""
The park has different types of rides which include: {*self.rides,}
It has has different elements which include: {*self.elements,}
              """)

class Transaction:
    
    unique_id=1000

    def __init__(self, amount:float, item_description:str, location:str, bought_in_restaurant:bool, bought_in_shop:bool ):
       Transaction.unique_id+=1
       self.transaction_id = Transaction.unique_id
       self.amount = amount
       self.item_description = item_description
       self.location = location
       self.bought_in_restaurant = bought_in_restaurant
       self.bought_in_shop = bought_in_shop
       
    def record_transaction(self):
       
        transaction_record = [
            self.transaction_id,
            self.amount,
            self.item_description,
            self.location,
        ]

        MagicBand.purchase_history.append(transaction_record)
       
        if self.bought_in_restaurant== True:
            MagicBand.use_band_in_restaurant(self.amount)

        elif self.bought_in_shop==True:
            MagicBand.use_band_in_shop(self.amount)
        else:
            return "Unknown transaction"
       
        return transaction_record

    def get_transaction_details(self):
        return [
            "Your transaction id:",self.transaction_id,
            "Price of the item purchased:",self.amount,
            "Item description:",self.item_description,
            "Location of purchase:",self.location,
        ]

class Guest():
   
    current_guest_id = 1000
   
    # --------------- Constructor ---------------
   
    def __init__(self, name:str, age:int):
       
        Guest.current_guest_id += 1
        self.guest_id = "G00" + str(Guest.current_guest_id) # Unique Identifier for the Guest
        self.name = name # Name of the Guest
        self.age = age # Age of the Guest
        self.magic_band = None # A reference to the guest's Magic Band
        self.preferences = [] # A List of Preferences (i.e. Favourite, Restrictions...)
       
       # ---------------- METHODS ----------------
   
    # 1. String Representation Method
   
    def __str__(self):
        return ("This is guest:" + self.guest_id + "-->" + self.name)

    # -----------------------------------------
   
    # 2. Link's MagicBand to Guest

    def link_magic_band(self, band):
       
        self.magic_band = band
        return f"\nMagicBand {band.band_id} has been linked to guest ( {self.name} | {self.guest_id} )!"
   
    # -----------------------------------------
   
    # 3. Updates the Guest's Preferences
   
    def update_preferences(self, preferences):
       
        self.preferences.append(preferences)
       
        return f"\n({self.name} | {self.guest_id})'s preferences have been updated!\nPREFERENCES:\n{self.preferences}"

    # -----------------------------------------

    # 3. Returns the Guest's Profile and Linked Band Details
   
    def get_profile_summary(self):
       
        # If Test MagicBand Class / Objects ARE Created:
        return (f"\nGuest ID: {self.guest_id}\nName: {self.name}\nAge: {self.age}\nBand ID: {self.magic_band.band_id}\nPreferences: {self.preferences}")

class MagicBand():
   
    band_id = 0

    def __init__(self, guest:Guest):
        self.guest = guest
        import random

        #Create unique band id
        MagicBand.band_id += 1
        self.band_id = MagicBand.band_id

        self.current_location = None
        self.linked_tickets = []
        self.useage_history = []
        self.bought_item = 0 #start this at 0 instead of 1000

        #Set color of band
        colors = ["red", "green", "blue", "purple"]
        MagicBand.band_color = random.choice(colors)
        self.current_color = MagicBand.band_color
       
        self.light_up = False

    def use_band_for_Park_entry(self, Park: object):
        if Park.park_name in self.linked_tickets:
            print(f"Welcome to {Park.park_name}")
            self.light_up = True
            print(f"Your band has lit up a bright {self.current_color}")
            self.linked_tickets.remove(Park.park_name)
            self.current_location = Park.park_name
        else:
            return "You do not have a ticket for this park"

    def use_band_for_ride(self, ride: object):
        self.useage_history.append("Ride : "+ ride.ride_name)
        self.current_color = ride.ride_name
        ride.add_to_queue(self)

    def use_band_in_restaurant(self, restaurant:Restaurant, price_of_dish: float, name_of_dish:str):
        self.most_recent_order = Transaction(price_of_dish, name_of_dish, restaurant.name, True, False)
        self.useage_history.append("Food order:" + restaurant.name + "> "+ name_of_dish)
        self.current_location = restaurant.name
        self.bought_item += 1

    def use_band_in_shop(self, shop: Shop, price_of_item:float, name_of_item:str):
        self.most_recent_item = Transaction(price_of_item, name_of_item, shop.name, False, True)
        self.useage_history.append("Bought item:" + shop.name + ">" + name_of_item)
        self.current_location = shop.name
        self.bought_item += 1

    def light_up(self, color):
        self.light_up = True
        self.current_color = color
    
    def use_band_in_element(self, element:object):
        self.useage_history.append("Interact with element : "+ element.name)
        self.current_location = element.name
        element.interact(self)

    def purchase_park_ticket(self, Park: object):
        self.useage_history.append("Purchase Park Ticket : " + Park.park_name)
        self.current_location = "Ticket Store"
        self.linked_tickets.append(Park.park_name)

    def __str__(self):
        return f"{self.band_id}: Band_id for magic band class"

class MagicBandSystem:
    def __init__(self, list_of_disney_parks: list):
        self.registered_bands = []            # List of all bands that have been registered
        self.parks = list_of_disney_parks     # List of all parks

    def register_band(self,band):
        # Registers a band
        self.registered_bands.append(band)

    def get_band_info(self,band_id: int):
        # Returns information about a band if it is registered

        band_found = False

        # Checks through registered bands to find band and returns information when found
        for band in self.registered_bands:
            if band.band_id == band_id:
                band_found = True
                return "Name: " + band.guest.name + " \nCurrent Location: " + str(band.current_location)

        # If band is not found then that is returned
        if band_found == False:
            return "Band not Found"
       
    def generate_usage_report(self):
        # Returns overall usage report of all bands used and all existing parks
        return "Total Bands Used: " + str(len(self.registered_bands)) + "\nTotal Parks Visited: " + str(len(self.parks))

    def purchase_park_tickets(self, band : MagicBand, park: Park):
        # Magic band purchases park ticket
        band.purchase_park_ticket(park)

    def get_ride_interaction_count(self, ride:Ride):
        return ride.ride_name +" total visitors: " + str(ride.total_visitors)
   
    def __str__ (self):
        return "This is the Disney Magic Band System"
