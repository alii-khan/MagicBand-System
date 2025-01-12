# -----------------------------------------------
# Created By: Ali Khan (& Mr. Alexander's Class)
# Date: January 9-16, 2025
# DisneyWorld MagicBandSystem Culminating 
# -----------------------------------------------

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

# USE CASE:
# ------------------------------------
# Part 1 - Creation of Disney World Environment

# Create Parks
animal_kingdom_park = Park("Animal Kingdom")
magic_kingdom_park = Park("Magic Kingdom")
epcot_park = Park("Epcot")
hollywood_studios_park = Park("Hollywood Studios")

# Animal Kingdom Rides
ride_ak1 = Ride("Bug's Life", 48, 250)
animal_kingdom_park.add_ride(ride_ak1)

ride_ak2 = Ride("Expedition Everest", 44, 100)
animal_kingdom_park.add_ride(ride_ak2)

ride_ak3 = Ride("Kilimanjaro Safaris", 40, 300)
animal_kingdom_park.add_ride(ride_ak3)

# Animal Kingdom Restaurants
restaurant_ak1 = Restaurant("Pizzafari")
restaurant_ak1.add_dish("Noodles", 3.99)
restaurant_ak1.add_dish("Pizza Slice", 5.49)
animal_kingdom_park.add_restaurant(restaurant_ak1)

restaurant_ak2 = Restaurant("Rainforest Cafe")
restaurant_ak2.add_dish("Burgers", 9.99)
restaurant_ak2.add_dish("Chicken Wings", 7.99)
animal_kingdom_park.add_restaurant(restaurant_ak2)

restaurant_ak3 = Restaurant("Tiffins")
restaurant_ak3.add_dish("Grilled Salmon", 14.99)
restaurant_ak3.add_dish("Mac and Cheese", 8.99)
animal_kingdom_park.add_restaurant(restaurant_ak3)

# Animal Kingdom Shops
shop_ak1 = Shop("Trader Sam's")
shop_ak1.add_item("Stitch Plushie", 24.99)
shop_ak1.add_item("Animal Kingdom Mug", 14.99)
animal_kingdom_park.add_shops(shop_ak1)

shop_ak2 = Shop("Island Mercantile")
shop_ak2.add_item("Safari Hat", 19.99)
shop_ak2.add_item("Water Bottle", 12.99)
animal_kingdom_park.add_shops(shop_ak2)

shop_ak3 = Shop("Zuri's Sweets Shop")
shop_ak3.add_item("Candy Apple", 5.99)
shop_ak3.add_item("Chocolate Bar", 3.99)
animal_kingdom_park.add_shops(shop_ak3)

# Animal Kingdom Elements
element_ak1 = Element("Timon and Pumba Statue", "Golden Statue")
animal_kingdom_park.add_elements(element_ak1)

element_ak2 = Element("Tree of Life", "Iconic Structure")
animal_kingdom_park.add_elements(element_ak2)

element_ak3 = Element("Pandora Floating Rocks", "Proximity Attraction")
animal_kingdom_park.add_elements(element_ak3)

# Magic Kingdom Rides
ride_mk1 = Ride("Space Mountain", 48, 200)
magic_kingdom_park.add_ride(ride_mk1)

ride_mk2 = Ride("It's a Small World", 0, 300)
magic_kingdom_park.add_ride(ride_mk2)

ride_mk3 = Ride("Big Thunder Mountain Railroad", 42, 180)
magic_kingdom_park.add_ride(ride_mk3)

# Magic Kingdom Restaurants
restaurant_mk1 = Restaurant("Cinderella's Royal Table")
restaurant_mk1.add_dish("Roast Chicken", 16.99)
restaurant_mk1.add_dish("Mashed Potatoes", 4.99)
magic_kingdom_park.add_restaurant(restaurant_mk1)

restaurant_mk2 = Restaurant("Be Our Guest")
restaurant_mk2.add_dish("Steak", 19.99)
restaurant_mk2.add_dish("Pasta Alfredo", 11.99)
magic_kingdom_park.add_restaurant(restaurant_mk2)

restaurant_mk3 = Restaurant("Liberty Tree Tavern")
restaurant_mk3.add_dish("Turkey Leg", 14.99)
restaurant_mk3.add_dish("Apple Pie", 6.99)
magic_kingdom_park.add_restaurant(restaurant_mk3)

# Magic Kingdom Shops
shop_mk1 = Shop("Emporium")
shop_mk1.add_item("Mickey Ears", 19.99)
shop_mk1.add_item("Cinderella Figurine", 29.99)
magic_kingdom_park.add_shops(shop_mk1)

shop_mk2 = Shop("Big Top Souvenirs")
shop_mk2.add_item("Popcorn Bucket", 12.99)
shop_mk2.add_item("Plush Minnie Mouse", 24.99)
magic_kingdom_park.add_shops(shop_mk2)

shop_mk3 = Shop("Star Traders")
shop_mk3.add_item("Star Wars Mug", 16.99)
shop_mk3.add_item("Galaxy T-Shirt", 19.99)
magic_kingdom_park.add_shops(shop_mk3)

# Magic Kingdom Elements
element_mk1 = Element("Cinderella's Castle", "Iconic Structure")
magic_kingdom_park.add_elements(element_mk1)

element_mk2 = Element("Partners Statue", "Golden Statue")
magic_kingdom_park.add_elements(element_mk2)

element_mk3 = Element("Seven Dwarfs Mine Entrance", "Interactive Exhibit")
magic_kingdom_park.add_elements(element_mk3)

# Epcot Rides
ride_ep1 = Ride("Soarin'", 40, 200)
epcot_park.add_ride(ride_ep1)

ride_ep2 = Ride("Test Track", 40, 150)
epcot_park.add_ride(ride_ep2)

ride_ep3 = Ride("Spaceship Earth", 0, 300)
epcot_park.add_ride(ride_ep3)

# Epcot Restaurants
restaurant_ep1 = Restaurant("Coral Reef Restaurant")
restaurant_ep1.add_dish("Lobster Tail", 24.99)
restaurant_ep1.add_dish("Caesar Salad", 12.99)
epcot_park.add_restaurant(restaurant_ep1)

restaurant_ep2 = Restaurant("Le Cellier Steakhouse")
restaurant_ep2.add_dish("Filet Mignon", 36.99)
restaurant_ep2.add_dish("Poutine", 10.99)
epcot_park.add_restaurant(restaurant_ep2)

restaurant_ep3 = Restaurant("Garden Grill Restaurant")
restaurant_ep3.add_dish("BBQ Ribs", 19.99)
restaurant_ep3.add_dish("Grilled Vegetables", 14.99)
epcot_park.add_restaurant(restaurant_ep3)

# Epcot Shops
shop_ep1 = Shop("Mouse Gear")
shop_ep1.add_item("Epcot Globe Figurine", 29.99)
shop_ep1.add_item("Disney Pins", 9.99)
epcot_park.add_shops(shop_ep1)

shop_ep2 = Shop("World Traveler")
shop_ep2.add_item("Epcot T-Shirt", 19.99)
shop_ep2.add_item("Minnie Ears", 24.99)
epcot_park.add_shops(shop_ep2)

shop_ep3 = Shop("The Art of Disney")
shop_ep3.add_item("Disney Artwork", 99.99)
shop_ep3.add_item("Sketchbook Journal", 14.99)
epcot_park.add_shops(shop_ep3)

# Epcot Elements
element_ep1 = Element("Spaceship Earth Structure", "Iconic Structure")
epcot_park.add_elements(element_ep1)

element_ep2 = Element("Fountain of Nations", "Proximity Attraction")
epcot_park.add_elements(element_ep2)

element_ep3 = Element("Living with the Land Exhibit", "Interactive Exhibit")
epcot_park.add_elements(element_ep3)

# Hollywood Studios Rides
ride_hs1 = Ride("Tower of Terror", 40, 150)
hollywood_studios_park.add_ride(ride_hs1)

ride_hs2 = Ride("Rock 'n' Roller Coaster", 48, 120)
hollywood_studios_park.add_ride(ride_hs2)

ride_hs3 = Ride("Star Tours", 40, 180)
hollywood_studios_park.add_ride(ride_hs3)

# Hollywood Studios Restaurants
restaurant_hs1 = Restaurant("50's Prime Time Café")
restaurant_hs1.add_dish("Fried Chicken", 16.99)
restaurant_hs1.add_dish("Pot Roast", 18.99)
hollywood_studios_park.add_restaurant(restaurant_hs1)

restaurant_hs2 = Restaurant("Hollywood & Vine")
restaurant_hs2.add_dish("Seafood Platter", 29.99)
restaurant_hs2.add_dish("Spaghetti & Meatballs", 19.99)
hollywood_studios_park.add_restaurant(restaurant_hs2)

restaurant_hs3 = Restaurant("Woody's Lunch Box")
restaurant_hs3.add_dish("Grilled Cheese", 8.99)
restaurant_hs3.add_dish("Tachos", 9.99)
hollywood_studios_park.add_restaurant(restaurant_hs3)

# Hollywood Studios Shops
shop_hs1 = Shop("Tatooine Traders")
shop_hs1.add_item("Lightsaber", 49.99)
shop_hs1.add_item("Star Wars T-Shirt", 24.99)
hollywood_studios_park.add_shops(shop_hs1)

shop_hs2 = Shop("Mickey's of Hollywood")
shop_hs2.add_item("Hollywood Studios Mug", 14.99)
shop_hs2.add_item("Disney Collectible Keychain", 7.99)
hollywood_studios_park.add_shops(shop_hs2)

shop_hs3 = Shop("Keystone Clothiers")
shop_hs3.add_item("Disney Sweatshirt", 34.99)
shop_hs3.add_item("Mickey Mouse Watch", 44.99)
hollywood_studios_park.add_shops(shop_hs3)

# Hollywood Studios Elements
element_hs1 = Element("Hollywood Tower Hotel Sign", "Golden Statue")
hollywood_studios_park.add_elements(element_hs1)

element_hs2 = Element("Millennium Falcon", "Iconic Structure")
hollywood_studios_park.add_elements(element_hs2)

element_hs3 = Element("Toy Story Land Entrance", "Interactive Exhibit")
hollywood_studios_park.add_elements(element_hs3)

# Initialize Magic Band System

disney_parks = [animal_kingdom_park, magic_kingdom_park, epcot_park, hollywood_studios_park]

magic_band_system = MagicBandSystem(disney_parks)
print(magic_band_system)

# Part 2 - SIMULATION

# Guests deciding to go to Disney world (Create six guests.)
guest_1_ca = Guest("Christopher Alexander", 47)
guest_2_ra = Guest("Ruby Alexander", 9)
guest_3_aa = Guest("Annie Alexander", 6)
guest_4_jt = Guest("Joey Tribiani", 35)
guest_5_mb = Guest("Monica Bing", 28)
guest_6_rg = Guest("Ross Geller", 32)

# Three Guests purchase their own Magic Band"
magic_band_1 = MagicBand(guest_1_ca)
magic_band_2 = MagicBand(guest_2_ra)
magic_band_3 = MagicBand(guest_3_aa)

# Magic bands are registered in the disney system
magic_band_system.register_band(magic_band_1)
magic_band_system.register_band(magic_band_2)
magic_band_system.register_band(magic_band_3)

# Guests purchase tickets for parks
magic_band_system.purchase_park_tickets(magic_band_1, animal_kingdom_park)
magic_band_system.purchase_park_tickets(magic_band_2, animal_kingdom_park)
magic_band_system.purchase_park_tickets(magic_band_3, animal_kingdom_park)
magic_band_system.purchase_park_tickets(magic_band_1, epcot_park)
magic_band_system.purchase_park_tickets(magic_band_2, epcot_park)
magic_band_system.purchase_park_tickets(magic_band_3, epcot_park)

# Guests enter the Animal Kingdom Park
magic_band_1.use_band_for_Park_entry(animal_kingdom_park)
magic_band_2.use_band_for_Park_entry(animal_kingdom_park)
magic_band_3.use_band_for_Park_entry(animal_kingdom_park)

# Guests get in line for and complete rides
magic_band_1.use_band_for_ride(ride_ak1)  # Christopher on Bug's Life
ride_ak1.complete_ride(magic_band_1)

magic_band_2.use_band_for_ride(ride_ak2)  # Ruby on Expedition Everest
ride_ak2.complete_ride(magic_band_2)

magic_band_3.use_band_for_ride(ride_ak3)  # Annie on Kilimanjaro Safaris
ride_ak3.complete_ride(magic_band_3)

magic_band_2.use_band_for_ride(ride_ak3)  # Ruby on Kilimanjaro
ride_ak3.complete_ride(magic_band_2)

magic_band_1.use_band_for_ride(ride_ak3)  # Christopher on Kilimanjaro
ride_ak3.complete_ride(magic_band_1)

# Guests purchase food at restaurants
magic_band_1.use_band_in_restaurant(restaurant_ak1, 10.99, "Noodles")  # Christopher at Pizzafari
magic_band_2.use_band_in_restaurant(restaurant_ak2, 14.99, "Burgers")  # Ruby at Rainforest Cafe
magic_band_3.use_band_in_restaurant(restaurant_ak3, 15.99, "Grilled Salmon")  # Annie at Tiffins

# Guests purchase merchandise at shops
magic_band_1.use_band_in_shop(shop_ak1, 29.99, "Stitch Plushie")  # Christopher at Trader Sam's
magic_band_2.use_band_in_shop(shop_ak2, 19.99, "Safari Hat")  # Ruby at Island Mercantile
magic_band_3.use_band_in_shop(shop_ak3, 5.99, "Candy Apple")  # Annie at Zuri's Sweets Shop

# Guests interact with park elements
magic_band_1.use_band_in_element(element_ak1)  # Christopher interacts with Timon and Pumba Statue
magic_band_2.use_band_in_element(element_ak2)  # Ruby interacts with Tree of Life
magic_band_3.use_band_in_element(element_ak3)  # Annie interacts with Pandora Floating Rocks

# ------------------------------------------------------------------------------------------------

import tkinter as tk
from tkinter import ttk # This is just the themed window set

# Main Application Window
def main_screen():
    root = tk.Tk()
    root.title("Disney System Interface")
    root.geometry("800x600")

    def open_employee_interface():
        password_window = tk.Toplevel(root)
        password_window.title("Employee Login")
        password_window.geometry("300x200")

        tk.Label(password_window, text="Enter Password").pack(pady=10)
        password_entry = tk.Entry(password_window, show="*")
        password_entry.pack()

        def validate_password():
            if password_entry.get() == "DisneyEmployee123":
                password_window.destroy() # This is just going to collapse the widgets!
                employee_interface()
            else:
                tk.Label(password_window, text="Incorrect Password", fg="red").pack()

        tk.Button(password_window, text="Login", command=validate_password).pack(pady=10)

    # Buttons for the main screen
    tk.Label(root, text="Welcome to the Disney System", font=("Helvetica", 18)).pack(pady=20)
    tk.Button(root, text="Employee Login", command=open_employee_interface, height=2, width=20).pack(pady=10)
    tk.Button(root, text="Guest Login", height=2, width=20).pack(pady=10)  # Placeholder (, command=lambda: pass)

    root.mainloop()

# Employee Interface
def employee_interface():
    emp_root = tk.Tk()
    emp_root.title("Disney Employee Interface")
    emp_root.geometry("1000x700")

    def show_park_overview():
        park_window = tk.Toplevel(emp_root)
        park_window.title("Park Overview")
        park_window.geometry("800x600")

        tk.Label(park_window, text="Select a Park to View Details", font=("Helvetica", 14)).pack(pady=10)

        def show_park_details(park):
            detail_window = tk.Toplevel(park_window)
            detail_window.title(f"{park.park_name} Details")
            detail_window.geometry("800x600")

            details = f"Rides: \n" + "\n".join([ride.ride_name for ride in park.rides]) + "\n\n" \
                      f"Restaurants: \n" + "\n".join([rest.name for rest in park.restaurants]) + "\n\n" \
                      f"Shops: \n" + "\n".join([shop.name for shop in park.shops]) + "\n\n" \
                      f"Elements: \n" + "\n".join([elem.name for elem in park.elements])

            tk.Label(detail_window, text=details, justify="center", font=("Helvetica", 12)).pack(pady=20, padx=20)

        for park in disney_parks:
            tk.Button(park_window, text=park.park_name, command=lambda p=park: show_park_details(p)).pack(pady=10)

    def show_magic_band_management():
        band_window = tk.Toplevel(emp_root)
        band_window.title("Magic Band Management")
        band_window.geometry("800x600")

        tk.Label(band_window, text="Magic Band Management", font=("Helvetica", 14)).pack(pady=10)

        def view_usage_report():
            report = magic_band_system.generate_usage_report()
            tk.Label(band_window, text=report, font=("Helvetica", 12)).pack(pady=10)

        def provide_new_band():
            tk.Label(band_window, text="Provide a New Magic Band (Simulated)", font=("Helvetica", 12)).pack(pady=10)

        def register_band():
            tk.Label(band_window, text="Register a Magic Band (Simulated)", font=("Helvetica", 12)).pack(pady=10)

        tk.Button(band_window, text="View Usage Report", command=view_usage_report).pack(pady=5)
        tk.Button(band_window, text="Provide New Band", command=provide_new_band).pack(pady=5)
        tk.Button(band_window, text="Register Band", command=register_band).pack(pady=5)

    def show_ride_management():
        ride_window = tk.Toplevel(emp_root)
        ride_window.title("Ride Management")
        ride_window.geometry("800x600")

        tk.Label(ride_window, text="Select a Park to View Ride Info", font=("Helvetica", 14)).pack(pady=10)

        def show_ride_details(park):
            ride_detail_window = tk.Toplevel(ride_window)
            ride_detail_window.title(f"{park.park_name} Rides")
            ride_detail_window.geometry("800x600")

            for ride in park.rides:
                tk.Button(ride_detail_window, text=ride.ride_name, command=lambda r=ride: tk.Label(ride_detail_window, text=r.get_ride_info(), justify="left", font=("Helvetica", 10)).pack(pady=5)).pack(pady=5)

        for park in disney_parks:
            tk.Button(ride_window, text=park.park_name, command=lambda p=park: show_ride_details(p)).pack(pady=5)

    def show_restaurant_management():
        restaurant_window = tk.Toplevel(emp_root)
        restaurant_window.title("Restaurant Management")
        restaurant_window.geometry("800x600")

        tk.Label(restaurant_window, text="Select a Park to View Restaurants", font=("Helvetica", 14)).pack(pady=10)

        def show_restaurant_details(park):
            rest_detail_window = tk.Toplevel(restaurant_window)
            rest_detail_window.title(f"{park.park_name} Restaurants")
            rest_detail_window.geometry("800x600")

            for restaurant in park.restaurants:
                tk.Button(rest_detail_window, text=restaurant.name, command=lambda r=restaurant: tk.Label(rest_detail_window, text=r.get_restaurant_info(), justify="center", font=("Helvetica", 10)).pack(pady=10)).pack(pady=5)

        for park in disney_parks:
            tk.Button(restaurant_window, text=park.park_name, command=lambda p=park: show_restaurant_details(p)).pack(pady=10)

    def show_shop_management():
        shop_window = tk.Toplevel(emp_root)
        shop_window.title("Shop Management")
        shop_window.geometry("800x600")

        tk.Label(shop_window, text="Select a Park to View Shops", font=("Helvetica", 14)).pack(pady=10)

        def show_shop_details(park):
            shop_detail_window = tk.Toplevel(shop_window)
            shop_detail_window.title(f"{park.park_name} Shops")
            shop_detail_window.geometry("800x600")

            for shop in park.shops:
                tk.Button(shop_detail_window, text=shop.name, command=lambda s=shop: tk.Label(shop_detail_window, text=s.get_shop_info(), justify="center", font=("Helvetica", 10)).pack(pady=10)).pack(pady=5)

        for park in disney_parks:
            tk.Button(shop_window, text=park.park_name, command=lambda p=park: show_shop_details(p)).pack(pady=10)

    def show_element_management():
        element_window = tk.Toplevel(emp_root)
        element_window.title("Park Elements")
        element_window.geometry("800x600")

        tk.Label(element_window, text="Select a Park to View Elements", font=("Helvetica", 14)).pack(pady=10)

        def show_element_details(park):
            element_detail_window = tk.Toplevel(element_window)
            element_detail_window.title(f"{park.park_name} Elements")
            element_detail_window.geometry("800x600")

            details = "\n".join([elem.name for elem in park.elements])
            tk.Label(element_detail_window, text=details, justify="center", font=("Helvetica", 12)).pack(pady=20)

        for park in disney_parks:
            tk.Button(element_window, text=park.park_name, command=lambda p=park: show_element_details(p)).pack(pady=10)

    # Employee Interface Layout
    tk.Label(emp_root, text="Disney Employee Interface", font=("Helvetica", 18)).pack(pady=20)
    tk.Button(emp_root, text="Park Overview", command=show_park_overview, width=20, height=2).pack(pady=10)
    tk.Button(emp_root, text="Magic Band Info", command=show_magic_band_management, width=20, height=2).pack(pady=10)
    tk.Button(emp_root, text="Ride Info", command=show_ride_management, width=20, height=2).pack(pady=10)
    tk.Button(emp_root, text="Restaurant Info", command=show_restaurant_management, width=20, height=2).pack(pady=10)
    tk.Button(emp_root, text="View Shops", command=show_shop_management, width=20, height=2).pack(pady=10)
    tk.Button(emp_root, text="View Elements", command=show_element_management, width=20, height=2).pack(pady=10)

    emp_root.mainloop()

# Main Program Execution
main_screen()