class Ride: # EDITED BY ALI KHAN > ADDED TOTAL VISTORS IN ***RIDE INFO***
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
Total Visitors: {self.total_visitors} 
""" # EDITED BY ALI KHAN > ADDED TOTAL VISTORS IN ***RIDE INFO***

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