from park_features import *

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
        return (f"\nGuest ID: {self.guest_id}\nName: {self.name}\nAge: {self.age}\nBand ID: {self.magic_band.band_id if self.magic_band else 'None'}\nPreferences: {self.preferences}")

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

    def use_band_for_park_entry(self, Park: object):
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
