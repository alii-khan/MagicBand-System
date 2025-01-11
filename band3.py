import random

class MagicBandSystem:
    def __init__(self):
        self.registered_bands = []
        self.guests = []
        self.parks = []
        self.transactions = []
        self.hotel_rooms = set()
        self.shop = Shop("Disney Store", "Mickey Mouse Plush Toy", 20)
        self.restaurant = Restaurant("Disney Diner", "Cheeseburger Combo", 15)

    def register_new_guest(self, name, age):
        guest_id = f"G{len(self.guests) + 1}"
        new_guest = Guest(guest_id, name, age)
        magic_band = MagicBand(f"MB{len(self.registered_bands) + 1}", new_guest)
        new_guest.link_magic_band(magic_band)
        self.guests.append(new_guest)
        self.registered_bands.append(magic_band)
        return new_guest, magic_band

    def purchase_park_tickets(self, band_id, park_name):
        band = self.get_band_by_id(band_id)
        if band:
            band.purchase_park_ticket(park_name)
            return True
        return False

    def get_band_by_id(self, band_id):
        for band in self.registered_bands:
            if band.band_id == band_id:
                return band
        return None

    def book_hotel_room(self, guest):
        room_number = len(self.hotel_rooms) + 101
        self.hotel_rooms.add(room_number)
        return room_number

    def record_transaction(self, band_id, amount, description, location):
        band = self.get_band_by_id(band_id)
        if band:
            transaction = Transaction(len(self.transactions) + 1, band_id, amount, description, location)
            self.transactions.append(transaction)
            band.add_transaction(transaction)
            return transaction
        return None


class MagicBand:
    def __init__(self, band_id, guest):
        self.band_id = band_id
        self.guest = guest
        self.balance = 0
        self.linked_tickets = []
        self.purchase_history = []

    def purchase_park_ticket(self, park_name):
        self.linked_tickets.append(park_name)

    def add_transaction(self, transaction):
        self.purchase_history.append(transaction)


class Guest:
    def __init__(self, guest_id, name, age):
        self.guest_id = guest_id
        self.name = name
        self.age = age
        self.magic_band = None

    def link_magic_band(self, band):
        self.magic_band = band


class Park:
    def __init__(self, park_name):
        self.park_name = park_name
        self.rides = []
        self.shops = []
        self.restaurants = []
        self.elements = []

    def add_ride(self, ride):
        self.rides.append(ride)

    def add_shop(self, shop):
        self.shops.append(shop)

    def add_restaurant(self, restaurant):
        self.restaurants.append(restaurant)

    def add_element(self, element):
        self.elements.append(element)


class Ride:
    def __init__(self, ride_name, height_requirement, capacity):
        self.ride_name = ride_name
        self.height_requirement = height_requirement
        self.capacity = capacity
        self.queue = []

    def add_to_queue(self, band):
        self.queue.append(band.band_id)

    def process_queue(self):
        if self.queue:
            self.queue.pop(0)


class Shop:
    def __init__(self, name, item_name, price):
        self.name = name
        self.item_name = item_name
        self.price = price


class Restaurant:
    def __init__(self, name, food_item, price):
        self.name = name
        self.food_item = food_item
        self.price = price


class Transaction:
    def __init__(self, transaction_id, band_id, amount, description, location):
        self.transaction_id = transaction_id
        self.band_id = band_id
        self.amount = amount
        self.description = description
        self.location = location


class Element:
    def __init__(self, element_id, name, interaction_type, location):
        self.element_id = element_id
        self.name = name
        self.interaction_type = interaction_type
        self.location = location
        self.interaction_log = []

    def interact(self, band_id):
        self.interaction_log.append(f"Band {band_id} interacted with {self.name}")


import tkinter as tk
from tkinter import messagebox

class MagicBandUI:
    def __init__(self, system):
        self.system = system
        self.root = tk.Tk()
        self.root.title("Disney Guest Portal")
        self.root.geometry("500x600")
        self.create_main_menu()

    def create_main_menu(self):
        tk.Label(self.root, text="Disney Guest Portal", font=("Arial", 16)).pack(pady=10)

        buttons = [
            ("Register New Guest", self.register_guest_menu),
            ("Purchase Park Tickets", self.purchase_tickets_menu),
            ("Add Credit Card / Payments", self.add_credit_card_menu),
            ("Purchase Food", self.purchase_food_menu),
            ("Purchase Item", self.purchase_item_menu),
            ("Book Hotel Room", self.book_hotel_room_menu),
            ("View Ride Queue", self.view_ride_queue_menu),
            ("View Transaction History", self.view_transaction_history_menu),
        ]

        for text, command in buttons:
            tk.Button(self.root, text=text, command=command, width=30).pack(pady=5)

    def register_guest_menu(self):
        window = tk.Toplevel(self.root)
        window.title("Register New Guest")
        tk.Label(window, text="Name:").grid(row=0, column=0)
        name_entry = tk.Entry(window)
        name_entry.grid(row=0, column=1)
        tk.Label(window, text="Age:").grid(row=1, column=0)
        age_entry = tk.Entry(window)
        age_entry.grid(row=1, column=1)

        def register_guest():
            name = name_entry.get()
            age = age_entry.get()
            if name and age.isdigit():
                guest, band = self.system.register_new_guest(name, int(age))
                messagebox.showinfo("Success", f"Guest {name} registered with MagicBand ID {band.band_id}")
            else:
                messagebox.showerror("Error", "Invalid input!")

        tk.Button(window, text="Register", command=register_guest).grid(row=2, column=0, columnspan=2)
        
        
    def add_credit_card_menu(self):
        window = tk.Toplevel(self.root)
        window.title("Add Credit Card / Payment")

        tk.Label(window, text="Enter MagicBand ID:").grid(row=0, column=0)
        band_entry = tk.Entry(window)
        band_entry.grid(row=0, column=1)

        tk.Label(window, text="Enter Amount to Load:").grid(row=1, column=0)
        amount_entry = tk.Entry(window)
        amount_entry.grid(row=1, column=1)

        def add_credit():
            band_id = band_entry.get()
            amount = amount_entry.get()
            if band_id and amount.isdigit():
                band = self.system.get_band_by_id(band_id)
                if band:
                    band.balance += int(amount)
                    messagebox.showinfo("Success", f"${amount} added to MagicBand {band_id}. New Balance: ${band.balance}")
                else:
                    messagebox.showerror("Error", "MagicBand not found!")
            else:
                messagebox.showerror("Error", "Invalid input!")

        tk.Button(window, text="Add Payment", command=add_credit).grid(row=2, column=0, columnspan=2)
        
    def purchase_food_menu(self):
        window = tk.Toplevel(self.root)
        window.title("Purchase Food")

        tk.Label(window, text="Enter MagicBand ID:").grid(row=0, column=0)
        band_entry = tk.Entry(window)
        band_entry.grid(row=0, column=1)

        tk.Label(window, text="Select Restaurant:").grid(row=1, column=0)
        restaurant_var = tk.StringVar(value="Restaurant A")
        tk.OptionMenu(window, restaurant_var, *[r.name for r in self.system.restaurants]).grid(row=1, column=1)

        tk.Label(window, text="Select Food Item:").grid(row=2, column=0)
        item_var = tk.StringVar(value="Item 1")
        food_menu = []  # Placeholder for dynamically loading food items from restaurants

        def update_food_menu(*args):
            selected_restaurant = restaurant_var.get()
            for restaurant in self.system.restaurants:
                if restaurant.name == selected_restaurant:
                    food_menu.clear()
                    food_menu.extend(restaurant.menu.keys())
                    item_var.set(food_menu[0] if food_menu else "No Items Available")
                    break

        restaurant_var.trace("w", update_food_menu)
        tk.OptionMenu(window, item_var, *food_menu).grid(row=2, column=1)

        def purchase_food():
            band_id = band_entry.get()
            selected_item = item_var.get()
            restaurant_name = restaurant_var.get()

            band = self.system.get_band_by_id(band_id)
            if not band:
                messagebox.showerror("Error", "MagicBand not found!")
                return

            for restaurant in self.system.restaurants:
                if restaurant.name == restaurant_name:
                    if selected_item in restaurant.menu:
                        item_price = restaurant.menu[selected_item]
                        if band.balance >= item_price:
                            band.balance -= item_price
                            transaction = Transaction(
                                transaction_id=len(band.purchase_history) + 1,
                                band_id=band_id,
                                amount=item_price,
                                item_description=selected_item,
                                location=restaurant.name,
                            )
                            band.purchase_history.append(transaction)
                            messagebox.showinfo("Success", f"Purchased {selected_item} for ${item_price}. New Balance: ${band.balance}.")
                        else:
                            messagebox.showerror("Error", "Insufficient balance!")
                    else:
                        messagebox.showerror("Error", "Item not found in menu!")
                    return

            messagebox.showerror("Error", "Restaurant not found!")

        tk.Button(window, text="Purchase", command=purchase_food).grid(row=3, column=0, columnspan=2)




    def purchase_tickets_menu(self):
        # Implementation similar to the "register_guest_menu"
        pass

    # Define the other UIs similarly...

    def run(self):
        self.root.mainloop()


# Initialize System and Run UI
system = MagicBandSystem()
app = MagicBandUI(system)
app.run()
